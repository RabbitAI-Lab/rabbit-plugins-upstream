#!/usr/bin/env bash
# HubSpot runtime boundary: use broker-seeded cached OAuth credentials only.
set -eu

script_dir="$(cd "$(dirname "$0")" && pwd)"
bundle_dir="$(cd "${script_dir}/.." && pwd)"
config_path="${bundle_dir}/mcporter.json"
command_name="${1:?mcporter command required}"
shift
server_name="maverick-hubspot-mcp"

reject() {
  echo "mcporter-readonly.sh: $*" >&2
  exit 2
}

required_mcporter_version="0.12.3"
actual_mcporter_version="$(mcporter --version 2>/dev/null)" || \
  reject "mcporter ${required_mcporter_version} is required"
[[ "${actual_mcporter_version}" == "${required_mcporter_version}" ]] || \
  reject "mcporter ${required_mcporter_version} is required; found ${actual_mcporter_version}"

case "${command_name}" in
  list)
    if [[ "$#" -ne 2 || "$1" != "${server_name}" || "$2" != "--schema" ]]; then
      reject "list requires exactly: ${server_name} --schema"
    fi
    exec mcporter --config "${config_path}" list --no-oauth "${server_name}" --schema
    ;;
  call)
    output_args=()
    if [[ "${1:-}" == "--output" ]]; then
      [[ "$#" -ge 3 ]] || reject "--output requires a format and tool selector"
      case "$2" in
        text|markdown|json|raw) ;;
        *) reject "unsupported output format: $2" ;;
      esac
      output_args=(--output "$2")
      shift 2
    fi

    selector="${1:-}"
    [[ -n "${selector}" ]] || reject "call requires a reviewed HubSpot tool selector"
    shift

    case "${selector}" in
      "${server_name}.get_user_details" | \
      "${server_name}.search_crm_objects" | \
      "${server_name}.get_crm_objects" | \
      "${server_name}.search_properties" | \
      "${server_name}.get_properties" | \
      "${server_name}.search_owners" | \
      "${server_name}.get_campaign_contacts_by_type" | \
      "${server_name}.get_campaign_analytics" | \
      "${server_name}.get_campaign_asset_types" | \
      "${server_name}.get_campaign_asset_metrics" | \
      "${server_name}.search_conversations" | \
      "${server_name}.get_conversation_channel_metadata") ;;
      *) reject "tool selector is not in the reviewed read-only allowlist: ${selector}" ;;
    esac

    for argument in "$@"; do
      case "${argument}" in
        -*) reject "mcporter flags are not accepted as tool arguments: ${argument}" ;;
      esac
    done

    exec mcporter --config "${config_path}" call --no-oauth \
      "${output_args[@]}" "${selector}" "$@"
    ;;
  *)
    reject "only list and call are allowed"
    ;;
esac
