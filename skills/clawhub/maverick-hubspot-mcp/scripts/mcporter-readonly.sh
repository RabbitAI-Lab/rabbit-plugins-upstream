#!/usr/bin/env bash
# HubSpot runtime boundary: use broker-seeded cached OAuth credentials only.
set -eu

script_dir="$(cd "$(dirname "$0")" && pwd)"
bundle_dir="$(cd "${script_dir}/.." && pwd)"
config_path="${bundle_dir}/mcporter.json"
command_name="${1:?mcporter command required}"
shift

case "${command_name}" in
  list|call)
    exec mcporter --config "${config_path}" "${command_name}" --no-oauth "$@"
    ;;
  *)
    echo "mcporter-readonly.sh: only list and call are allowed" >&2
    exit 2
    ;;
esac
