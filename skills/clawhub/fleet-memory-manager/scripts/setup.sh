#!/usr/bin/env bash
set -euo pipefail

usage() {
  printf '%s\n' \
    'Usage: setup.sh --workspace /absolute/private/workspace [--apply]' \
    '' \
    'Default mode is a dry run. --apply creates only missing files and never' \
    'overwrites or patches existing workspace content.'
}

workspace=''
apply='false'

while [ "$#" -gt 0 ]; do
  case "$1" in
    --workspace)
      [ "$#" -ge 2 ] || { usage >&2; exit 2; }
      workspace="$2"
      shift 2
      ;;
    --apply)
      apply='true'
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      printf 'Unknown argument: %s\n' "$1" >&2
      usage >&2
      exit 2
      ;;
  esac
done

[ -n "$workspace" ] || { usage >&2; exit 2; }
case "$workspace" in
  /*) ;;
  *) printf 'Workspace must be an absolute path.\n' >&2; exit 2 ;;
esac
[ -d "$workspace" ] || { printf 'Workspace does not exist: %s\n' "$workspace" >&2; exit 2; }

workspace="$(cd "$workspace" && pwd -P)"
case "$workspace" in
  /|/Users|/home|/root)
    printf 'Refusing broad workspace path: %s\n' "$workspace" >&2
    exit 2
    ;;
esac

skill_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd -P)"
templates_dir="$skill_dir/templates"
today="$(date +%Y-%m-%d)"

printf 'Fleet Memory Manager setup\n'
printf 'Workspace: %s\n' "$workspace"
printf 'Mode: %s\n\n' "$([ "$apply" = 'true' ] && printf 'apply' || printf 'dry-run')"

create_from_template() {
  source_file="$templates_dir/$1"
  destination="$workspace/$2"
  if [ -e "$destination" ]; then
    printf 'UNCHANGED existing %s\n' "$destination"
  elif [ "$apply" = 'true' ]; then
    cp "$source_file" "$destination"
    printf 'CREATED %s\n' "$destination"
  else
    printf 'WOULD CREATE %s\n' "$destination"
  fi
}

if [ -e "$workspace/memory" ] && [ ! -d "$workspace/memory" ]; then
  printf 'Cannot create memory directory; a non-directory exists at %s/memory\n' "$workspace" >&2
  exit 2
fi

if [ -d "$workspace/memory" ]; then
  printf 'UNCHANGED existing %s/memory\n' "$workspace"
elif [ "$apply" = 'true' ]; then
  mkdir "$workspace/memory"
  printf 'CREATED %s/memory\n' "$workspace"
else
  printf 'WOULD CREATE %s/memory\n' "$workspace"
fi

create_from_template 'MEMORY.md' 'MEMORY.md'
create_from_template 'USER.md' 'USER.md'
create_from_template 'AGENTS.md' 'AGENTS.md'
create_from_template 'HEARTBEAT.md' 'HEARTBEAT.md'

daily_file="$workspace/memory/$today.md"
if [ -e "$daily_file" ]; then
  printf 'UNCHANGED existing %s\n' "$daily_file"
elif [ "$apply" = 'true' ]; then
  {
    printf '# %s\n\n' "$today"
    printf 'Retention: review or delete after %s.\n\n' "$(date -v+30d +%Y-%m-%d 2>/dev/null || date -d '+30 days' +%Y-%m-%d 2>/dev/null || printf '30 days')"
    printf '## Task state\n\n- Add only work-relevant facts needed for continuity.\n\n'
    printf '## Decisions\n\n- None recorded.\n\n'
    printf '## Next session\n\n- Review the new memory templates before enabling them.\n'
  } > "$daily_file"
  printf 'CREATED %s\n' "$daily_file"
else
  printf 'WOULD CREATE %s\n' "$daily_file"
fi

printf '\nNo existing files were modified. No schedule was created.\n'
if [ "$apply" != 'true' ]; then
  printf 'Review this preview, then rerun with --apply if the user consents.\n'
else
  printf 'Review every created file before enabling memory loading.\n'
fi
