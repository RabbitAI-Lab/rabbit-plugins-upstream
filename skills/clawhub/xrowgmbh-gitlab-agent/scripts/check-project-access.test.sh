#!/usr/bin/env bash
set -euo pipefail

skill_dir=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
check_script="${skill_dir}/scripts/check-project-access.sh"
test_dir=$(mktemp -d)
trap 'rm -rf "${test_dir}"' EXIT

cat >"${test_dir}/glab" <<'MOCK'
#!/usr/bin/env bash
set -euo pipefail
[[ "${1:-}" == "api" ]] || exit 2
case "${2:-}" in
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
  *) exit 2 ;;
esac
MOCK
chmod +x "${test_dir}/glab"

PATH="${test_dir}:${PATH}" "${check_script}" xrow-public/ci-tools xrow >/dev/null

if MOCK_CREATED_BY=mallory PATH="${test_dir}:${PATH}" "${check_script}" xrow-public/ci-tools xrow >/dev/null 2>&1; then
  echo "mismatched creator unexpectedly passed" >&2
  exit 1
fi

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

echo "security gate tests passed"
