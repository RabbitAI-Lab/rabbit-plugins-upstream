#!/usr/bin/env bash
set -euo pipefail

script_dir=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
tmp=$(mktemp -d)
trap 'rm -rf "${tmp}"' EXIT
export MOCK_LOG="${tmp}/api.log"

cat >"${tmp}/glab" <<'MOCK'
#!/usr/bin/env bash
set -euo pipefail
[[ "${1:-}" == api ]] || exit 2
shift

if [[ "${1:-}" == -X ]]; then
  printf '%s\n' "$*" >>"${MOCK_LOG}"
  cat >"${MOCK_LOG}.body"
  printf '{}\n'
  exit
fi

endpoint=$1
case "${endpoint}" in
  user) printf '{"id":99,"username":"robot"}\n' ;;
  projects/example%2Fproject) printf '{"id":1,"default_branch":"main"}\n' ;;
  projects/example%2Fproject/merge_requests/7)
    sha=abc
    if [[ "${MOCK_CHANGED:-false}" == true ]]; then
      count=$(grep -c '^mr-read$' "${MOCK_LOG}" 2>/dev/null || true)
      printf 'mr-read\n' >>"${MOCK_LOG}"
      ((count == 0)) || sha=changed
    fi
    printf '{"iid":7,"state":"opened","sha":"%s","author":{"id":99,"username":"robot"},"assignees":[{"id":99,"username":"robot"}],"reviewers":[{"id":77,"username":"existing"}]}\n' "${sha}"
    ;;
  projects/example%2Fproject/members/all\?per_page=100)
    if [[ "${MOCK_OWNER_ONLY:-false}" == true ]]; then
      printf '[{"id":99,"username":"robot","access_level":30,"state":"active","locked":false},{"id":3,"username":"xrow","access_level":50,"state":"active","locked":false}]\n'
    elif [[ "${MOCK_INCOMPLETE:-false}" == true ]]; then
      printf '[{"id":2,"username":"andyxrow","access_level":40,"state":"active"}]\n'
    else
      printf '[{"id":99,"username":"robot","access_level":30,"state":"active","locked":false},{"id":2,"username":"andyxrow","access_level":40,"state":"active","locked":false},{"id":3,"username":"xrow","access_level":50,"state":"active","locked":false}]\n'
    fi
    ;;
  projects/example%2Fproject/merge_requests/7/closes_issues\?per_page=100)
    case "${MOCK_LINKED:-none}" in
      one) printf '[{"id":19,"iid":19,"author":{"id":2,"username":"andyxrow"}}]\n' ;;
      two) printf '[{"id":19,"iid":19,"author":{"id":2,"username":"andyxrow"}},{"id":20,"iid":20,"author":{"id":3,"username":"xrow"}}]\n' ;;
      *) printf '[]\n' ;;
    esac
    ;;
  projects/example%2Fproject/repository/tree\?*)
    if [[ "${MOCK_AGENTS:-false}" == true ]]; then
      printf '[{"path":"AGENTS.md"}]\n'
    else
      printf '[]\n'
    fi
    ;;
  projects/example%2Fproject/repository/files/AGENTS.md/raw\?*)
    printf '| reviewers | [xrow](https://gitlab.com/xrow) |\n'
    ;;
  projects/example%2Fproject/members/all/2)
    printf '{"id":2,"username":"andyxrow","access_level":40,"state":"active","locked":false}\n'
    ;;
  *) exit 2 ;;
esac
MOCK
chmod +x "${tmp}/glab"

run() {
  PATH="${tmp}:${PATH}" "${script_dir}/select-reviewer.sh" "$@"
}

MOCK_LINKED=one MOCK_AGENTS=true run example/project 7 >"${tmp}/linked.json"
jq -e '.reviewer.username == "andyxrow" and .rule == "linked-work-item-author"' "${tmp}/linked.json" >/dev/null

MOCK_AGENTS=true run example/project 7 >"${tmp}/configured.json"
jq -e '.reviewer.username == "xrow" and .rule == "configured-reviewer"' "${tmp}/configured.json" >/dev/null

run example/project 7 >"${tmp}/maintainer.json"
jq -e '.reviewer.username == "andyxrow" and .rule == "maintainer-fallback"' "${tmp}/maintainer.json" >/dev/null

MOCK_OWNER_ONLY=true run example/project 7 >"${tmp}/owner.json"
jq -e '.reviewer.username == "xrow" and .rule == "owner-fallback"' "${tmp}/owner.json" >/dev/null

if MOCK_LINKED=two run example/project 7 >/dev/null 2>&1; then
  echo "ambiguous linked authors unexpectedly passed" >&2
  exit 1
fi
if MOCK_INCOMPLETE=true run example/project 7 >/dev/null 2>&1; then
  echo "incomplete membership unexpectedly passed" >&2
  exit 1
fi

: >"${MOCK_LOG}"
MOCK_LINKED=one run --apply example/project 7 >"${tmp}/applied.json"
jq -e '.applied == true and .dry_run == false' "${tmp}/applied.json" >/dev/null
jq -e '.reviewer_ids == [2,77]' "${MOCK_LOG}.body" >/dev/null

: >"${MOCK_LOG}"
if MOCK_LINKED=one MOCK_CHANGED=true run --apply example/project 7 >/dev/null 2>&1; then
  echo "changed merge request unexpectedly passed" >&2
  exit 1
fi
! grep -q '^PUT ' "${MOCK_LOG}"

echo "gitlab-agent reviewer selection tests passed"
