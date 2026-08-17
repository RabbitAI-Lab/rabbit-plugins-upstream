#!/usr/bin/env bash
set -euo pipefail

skill_dir=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
check_script="${skill_dir}/scripts/check-project-access.sh"
list_script="${skill_dir}/scripts/list-active-items.sh"
test_dir=$(mktemp -d)
trap 'rm -rf "${test_dir}"' EXIT

export MOCK_API_LOG="${test_dir}/api.log"

cat >"${test_dir}/glab" <<'MOCK'
#!/usr/bin/env bash
set -euo pipefail
[[ "${1:-}" == "api" ]] || exit 2
shift

if [[ "${1:-}" == "-X" ]]; then
  printf '%s\n' "$*" >>"${MOCK_API_LOG}"
  printf '%s\n' '{}'
  exit 0
fi

case "${1:-}" in
  user)
    printf '%s\n' '{"id":33363466,"username":"eugene-harold-krabs"}'
    ;;
  projects/*/members/all/33363466)
    [[ "${MOCK_MEMBER_EXISTS:-true}" == "true" ]] || exit 1
    printf '{"username":"eugene-harold-krabs","access_level":%s,"membership_state":"%s"' "${MOCK_ACCESS_LEVEL:-30}" "${MOCK_MEMBERSHIP_STATE:-active}"
    if [[ "${MOCK_CREATOR_PRESENT:-true}" == "true" ]]; then
      printf ',"created_by":{"username":"%s"}' "${MOCK_CREATED_BY:-xrow}"
    fi
    printf '}\n'
    ;;
  issues\?*)
    printf '%s\n' '[{"project_id":1,"iid":1,"title":"active issue","web_url":"https://gitlab.example/a/-/issues/1","labels":["workflow::backlog"],"assignees":[{"username":"eugene-harold-krabs"}]},{"project_id":2,"iid":2,"title":"forbidden issue","web_url":"https://gitlab.example/b/-/issues/2","labels":["workflow::forbidden"],"assignees":[{"username":"eugene-harold-krabs"}]}]'
    ;;
  merge_requests\?*)
    printf '%s\n' '[{"project_id":3,"iid":3,"title":"active MR","web_url":"https://gitlab.example/c/-/merge_requests/3","labels":[],"assignees":[{"username":"eugene-harold-krabs"}]},{"project_id":4,"iid":4,"title":"other assignee","web_url":"https://gitlab.example/d/-/merge_requests/4","labels":[],"assignees":[{"username":"someone-else"}]}]'
    ;;
  *) exit 2 ;;
esac
MOCK
chmod +x "${test_dir}/glab"

PATH="${test_dir}:${PATH}" "${check_script}" xrow-public/ci-tools xrow >/dev/null
[[ ! -s "${MOCK_API_LOG}" ]]

PATH="${test_dir}:${PATH}" "${check_script}" xrow-public/ci-tools xrow issue 7 >/dev/null
grep -Fq 'PUT projects/xrow-public%2Fci-tools/issues/7 -f remove_labels=workflow::forbidden' "${MOCK_API_LOG}"

: >"${MOCK_API_LOG}"
if MOCK_CREATED_BY=mallory PATH="${test_dir}:${PATH}" "${check_script}" xrow-public/ci-tools xrow merge_request 8 >/dev/null 2>&1; then
  echo "mismatched creator unexpectedly passed" >&2
  exit 1
fi
grep -Fq 'PUT projects/xrow-public%2Fci-tools/merge_requests/8 -f add_labels=workflow::forbidden' "${MOCK_API_LOG}"
grep -Fq 'remove_labels=workflow::backlog,workflow::in-progress,workflow::paused,workflow::blocked,workflow::need-human,workflow::review,workflow::stale,workflow::done' "${MOCK_API_LOG}"

if MOCK_CREATOR_PRESENT=false PATH="${test_dir}:${PATH}" "${check_script}" xrow-public/ci-tools xrow >/dev/null 2>&1; then
  echo "missing creator unexpectedly passed" >&2
  exit 1
fi

if MOCK_MEMBERSHIP_STATE=blocked PATH="${test_dir}:${PATH}" "${check_script}" xrow-public/ci-tools xrow >/dev/null 2>&1; then
  echo "inactive membership unexpectedly passed" >&2
  exit 1
fi

if MOCK_MEMBER_EXISTS=false PATH="${test_dir}:${PATH}" "${check_script}" xrow-public/ci-tools xrow >/dev/null 2>&1; then
  echo "missing membership unexpectedly passed" >&2
  exit 1
fi

PATH="${test_dir}:${PATH}" "${list_script}" >"${test_dir}/active.json"
jq -e 'length == 2' "${test_dir}/active.json" >/dev/null
jq -e 'map(.title) == ["active issue", "active MR"]' "${test_dir}/active.json" >/dev/null
jq -e 'all(.[]; .labels | index("workflow::forbidden") | not)' "${test_dir}/active.json" >/dev/null

echo "gitlab-agent script tests passed"
