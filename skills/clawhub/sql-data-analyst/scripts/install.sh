#!/bin/sh
set -eu

fail() {
    printf 'error:%s\n' "$1" >&2
    exit 1
}

script_path=$0
[ ! -L "$script_path" ] || fail install_target_invalid
script_dir=$(CDPATH= cd -P -- "$(dirname -- "$script_path")" && pwd) || fail install_target_invalid
package_dir=$(CDPATH= cd -P -- "$script_dir/.." && pwd) || fail install_target_invalid
runtime_dir="$package_dir/runtime"
venv_dir="$runtime_dir/.venv"

[ "$package_dir" != "/" ] || fail install_target_invalid
[ -d "$package_dir" ] && [ ! -L "$package_dir" ] || fail install_target_invalid
[ -d "$runtime_dir" ] && [ ! -L "$runtime_dir" ] || fail install_target_invalid

current_uid=$(id -u) || fail install_target_invalid
owner_id() {
    if [ "$(uname -s)" = "Darwin" ]; then
        stat -f '%u' "$1"
    else
        stat -c '%u' "$1"
    fi
}

valid_previous_venv() {
    previous_candidate=$1
    case "$previous_candidate" in
        "$runtime_dir"/.venv.previous.[A-Za-z0-9][A-Za-z0-9][A-Za-z0-9][A-Za-z0-9][A-Za-z0-9][A-Za-z0-9]) ;;
        *) return 1 ;;
    esac
    [ -d "$previous_candidate" ] && [ ! -L "$previous_candidate" ] || return 1
    [ "$(owner_id "$previous_candidate")" = "$current_uid" ] || return 1
}

[ "$(owner_id "$package_dir")" = "$current_uid" ] || fail install_target_not_owned
[ "$(owner_id "$runtime_dir")" = "$current_uid" ] || fail install_target_not_owned

recovery_candidate=
recovery_count=0
for candidate in "$runtime_dir"/.venv.previous.*; do
    if [ ! -e "$candidate" ] && [ ! -L "$candidate" ]; then
        continue
    fi
    recovery_count=$((recovery_count + 1))
    [ "$recovery_count" -eq 1 ] || fail install_target_invalid
    recovery_candidate=$candidate
done
if [ "$recovery_count" -eq 1 ]; then
    valid_previous_venv "$recovery_candidate" || fail install_target_invalid
    if [ -e "$venv_dir" ] || [ -L "$venv_dir" ]; then
        fail install_target_invalid
    fi
    mv "$recovery_candidate" "$venv_dir" || fail install_target_invalid
fi

venv_existing=0
if [ -e "$venv_dir" ] || [ -L "$venv_dir" ]; then
    [ -d "$venv_dir" ] && [ ! -L "$venv_dir" ] || fail install_target_invalid
    [ "$(owner_id "$venv_dir")" = "$current_uid" ] || fail install_target_not_owned
    venv_existing=1
fi

release_file="$package_dir/RELEASE"
manifest_file="$package_dir/SHA256SUMS"
trusted_keys_file="$runtime_dir/src/sql_data_analyst_local/trusted_keys.json"
settings_file="$runtime_dir/src/sql_data_analyst_local/settings.py"
requirements_file="$runtime_dir/requirements.lock"

for required_file in "$release_file" "$manifest_file" "$trusted_keys_file" "$settings_file" "$requirements_file"; do
    [ -f "$required_file" ] && [ ! -L "$required_file" ] || fail release_unstamped
done

if command -v sha256sum >/dev/null 2>&1; then
    sha256_file() {
        sha256sum "$1" | awk '{print $1}'
    }
elif command -v shasum >/dev/null 2>&1; then
    sha256_file() {
        shasum -a 256 "$1" | awk '{print $1}'
    }
else
    fail sha256_unavailable
fi

manifest_entries=0
manifest_has_release=0
manifest_has_keys=0
manifest_has_settings=0
manifest_has_requirements=0
while IFS= read -r manifest_line || [ -n "$manifest_line" ]; do
    [ -n "$manifest_line" ] || continue
    expected_sha=${manifest_line%%  *}
    relative_path=${manifest_line#*  }
    [ "$expected_sha  $relative_path" = "$manifest_line" ] || fail release_checksum_invalid
    case "$expected_sha" in
        *[!a-f0-9]*|'') fail release_checksum_invalid ;;
    esac
    [ "${#expected_sha}" -eq 64 ] || fail release_checksum_invalid
    case "$relative_path" in
        ''|/*|../*|*/../*|*/..) fail release_checksum_invalid ;;
        *[!A-Za-z0-9._/-]*) fail release_checksum_invalid ;;
    esac
    target_file="$package_dir/$relative_path"
    [ -f "$target_file" ] && [ ! -L "$target_file" ] || fail release_checksum_invalid
    actual_sha=$(sha256_file "$target_file") || fail release_checksum_invalid
    [ "$actual_sha" = "$expected_sha" ] || fail release_checksum_invalid
    case "$relative_path" in
        RELEASE) manifest_has_release=1 ;;
        runtime/src/sql_data_analyst_local/trusted_keys.json) manifest_has_keys=1 ;;
        runtime/src/sql_data_analyst_local/settings.py) manifest_has_settings=1 ;;
        runtime/requirements.lock) manifest_has_requirements=1 ;;
    esac
    manifest_entries=$((manifest_entries + 1))
done < "$manifest_file"
[ "$manifest_entries" -gt 0 ] || fail release_unstamped
[ "$manifest_has_release" -eq 1 ] || fail release_checksum_invalid
[ "$manifest_has_keys" -eq 1 ] || fail release_checksum_invalid
[ "$manifest_has_settings" -eq 1 ] || fail release_checksum_invalid
[ "$manifest_has_requirements" -eq 1 ] || fail release_checksum_invalid

find "$package_dir" \( -type f -o -type l \) -print | while IFS= read -r target_path; do
    relative_path=${target_path#"$package_dir"/}
    case "$relative_path" in
        SHA256SUMS) continue ;;
        runtime/.venv/*)
            [ "$venv_existing" -eq 1 ] || exit 1
            continue
            ;;
    esac
    case "$relative_path" in
        ''|/*|../*|*/../*|*/..|*[!A-Za-z0-9._/-]*) exit 1 ;;
    esac
    awk -v wanted="$relative_path" '
        substr($0, 67) == wanted { matches += 1 }
        END { exit matches == 1 ? 0 : 1 }
    ' "$manifest_file" || exit 1
done || fail release_checksum_invalid

stamp_version=
package_version=
platform_api_origin=
trusted_keys_sha256=
while IFS='=' read -r release_key release_value || [ -n "$release_key$release_value" ]; do
    case "$release_key" in
        stamp_version) [ -z "$stamp_version" ] || fail release_unstamped; stamp_version=$release_value ;;
        package_version) [ -z "$package_version" ] || fail release_unstamped; package_version=$release_value ;;
        platform_api_origin) [ -z "$platform_api_origin" ] || fail release_unstamped; platform_api_origin=$release_value ;;
        trusted_keys_sha256) [ -z "$trusted_keys_sha256" ] || fail release_unstamped; trusted_keys_sha256=$release_value ;;
        '') [ -z "$release_value" ] || fail release_unstamped ;;
        *) fail release_unstamped ;;
    esac
done < "$release_file"

[ "$stamp_version" = "1" ] && [ "$package_version" = "1.0.0" ] || fail release_unstamped
valid_release_origin() {
    release_origin=$1
    case "$release_origin" in
        https://*) release_authority=${release_origin#https://} ;;
        *) return 1 ;;
    esac
    if [ "${release_authority%/}" != "$release_authority" ]; then
        release_authority=${release_authority%/}
    fi
    [ -n "$release_authority" ] || return 1
    case "$release_authority" in
        */*|*'?'*|*'#'*|*'@'*|*' '*|*"	"*) return 1 ;;
        \[*\]*) return 1 ;;
    esac
    release_host=${release_authority%%:*}
    [ -n "$release_host" ] || return 1
    if [ "$release_host" != "$release_authority" ]; then
        release_port=${release_authority#*:}
        [ "$release_authority" = "$release_host:$release_port" ] || return 1
        case "$release_port" in
            0|[1-9][0-9]*) ;;
            *) return 1 ;;
        esac
        [ "${#release_port}" -le 5 ] || return 1
        [ "$release_port" -le 65535 ] || return 1
    fi
    canonical_host=$(printf '%s' "$release_host" | tr '[:upper:]' '[:lower:]') || return 1
    [ "$release_host" = "$canonical_host" ] || return 1
    release_host=$canonical_host
    if ! printf '%s\n' "$release_host" | awk -F. '
        BEGIN { valid = 1 }
        length($0) == 0 || length($0) > 253 { valid = 0 }
        NF < 2 || $NF !~ /[a-z]/ { valid = 0 }
        {
            for (part = 1; part <= NF; part += 1) {
                label = $part
                if (length(label) == 0 || length(label) > 63 || label !~ /^[a-z0-9-]+$/ || substr(label, 1, 1) !~ /^[a-z0-9]$/ || substr(label, length(label), 1) !~ /^[a-z0-9]$/) { valid = 0 }
            }
        }
        END { exit valid ? 0 : 1 }
    '; then
        return 1
    fi
    case "$release_host" in
        localhost|*.invalid|*.example|*.test) return 1 ;;
    esac
    if printf '%s\n' "$release_host" | awk -F. '
        BEGIN { valid = 1 }
        NF != 4 { valid = 0 }
        {
            for (part = 1; part <= 4; part += 1) {
                if ($part !~ /^[0-9]+$/ || (length($part) > 1 && substr($part, 1, 1) == "0") || $part < 0 || $part > 255) { valid = 0 }
            }
        }
        END { exit valid ? 0 : 1 }
    '; then
        return 1
    fi
    return 0
}
valid_release_origin "$platform_api_origin" || fail release_origin_invalid
case "$trusted_keys_sha256" in
    *[!a-f0-9]*|'') fail release_trust_invalid ;;
esac
[ "${#trusted_keys_sha256}" -eq 64 ] || fail release_trust_invalid

compact_keys=$(tr -d '[:space:]' < "$trusted_keys_file") || fail release_trust_invalid
[ -n "$compact_keys" ] && [ "$compact_keys" != '{}' ] && [ "$compact_keys" != '[]' ] || fail release_trust_invalid
[ "$(sha256_file "$trusted_keys_file")" = "$trusted_keys_sha256" ] || fail release_trust_invalid
grep -Fq "PLATFORM_API_ORIGIN = \"$platform_api_origin\"" "$settings_file" || fail release_origin_invalid
grep -Fq "TRUSTED_KEYS_SHA256 = \"$trusted_keys_sha256\"" "$settings_file" || fail release_trust_invalid

# Do not let the caller's working directory (including an old .venv) enter
# Python's import path while the replacement environment is being built.
cd "$package_dir" || fail install_target_invalid
unset PYTHONHOME PYTHONPATH VIRTUAL_ENV
python_bin=${SQL_DATA_ANALYST_PYTHON:-}
if [ -z "$python_bin" ]; then
    for candidate in python3.13 python3.12; do
        if command -v "$candidate" >/dev/null 2>&1; then
            python_bin=$(command -v "$candidate")
            break
        fi
    done
fi
[ -n "$python_bin" ] && [ -x "$python_bin" ] || fail python_unsupported
python_directory=$(CDPATH= cd -P -- "$(dirname -- "$python_bin")" && pwd) || fail python_unsupported
python_bin="$python_directory/$(basename -- "$python_bin")"
case "$python_bin" in
    "$package_dir"/*) fail python_unsupported ;;
esac
python_version=$("$python_bin" -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")') || fail python_unsupported
case "$python_version" in
    3.12|3.13) ;;
    *) fail python_unsupported ;;
esac

remove_generated_venv() {
    generated_venv=$1
    case "$generated_venv" in
        "$runtime_dir"/.venv.build.[A-Za-z0-9][A-Za-z0-9][A-Za-z0-9][A-Za-z0-9][A-Za-z0-9][A-Za-z0-9]|\
        "$runtime_dir"/.venv.previous.[A-Za-z0-9][A-Za-z0-9][A-Za-z0-9][A-Za-z0-9][A-Za-z0-9][A-Za-z0-9]) ;;
        *) return 1 ;;
    esac
    if [ -e "$generated_venv" ] || [ -L "$generated_venv" ]; then
        [ -d "$generated_venv" ] && [ ! -L "$generated_venv" ] || return 1
        [ "$(owner_id "$generated_venv")" = "$current_uid" ] || return 1
        rm -rf -- "$generated_venv"
    fi
}

cleanup_install() {
    cleanup_status=$?
    trap - 0 1 2 15
    if [ -n "${previous_venv:-}" ] && { [ -e "$previous_venv" ] || [ -L "$previous_venv" ]; }; then
        if ! valid_previous_venv "$previous_venv"; then
            cleanup_status=1
        else
            case "${transaction_state:-}" in
                building|previous_reserved)
                    if [ -e "$venv_dir" ] || [ -L "$venv_dir" ]; then
                        if remove_generated_venv "$previous_venv"; then
                            previous_venv=
                        else
                            cleanup_status=1
                        fi
                    else
                        cleanup_status=1
                    fi
                    ;;
                moving_previous|previous_moved|moving_fresh|replacement_installed)
                    if [ ! -e "$venv_dir" ] && [ ! -L "$venv_dir" ]; then
                        if mv "$previous_venv" "$venv_dir"; then
                            previous_venv=
                        else
                            cleanup_status=1
                        fi
                    elif remove_generated_venv "$previous_venv"; then
                        previous_venv=
                    else
                        cleanup_status=1
                    fi
                    ;;
                *) cleanup_status=1 ;;
            esac
        fi
    fi
    if [ -n "${fresh_venv:-}" ]; then
        if ! remove_generated_venv "$fresh_venv"; then
            cleanup_status=1
        fi
    fi
    exit "$cleanup_status"
}

umask 077
transaction_state=building
previous_venv=
fresh_venv=$(mktemp -d "$runtime_dir/.venv.build.XXXXXX") || fail install_target_invalid
trap cleanup_install 0
trap 'exit 129' 1
trap 'exit 130' 2
trap 'exit 143' 15
[ -d "$fresh_venv" ] && [ ! -L "$fresh_venv" ] || fail install_target_invalid
[ "$(owner_id "$fresh_venv")" = "$current_uid" ] || fail install_target_not_owned

"$python_bin" -m venv "$fresh_venv"
"$fresh_venv/bin/python" -m pip install --disable-pip-version-check --no-input -r "$runtime_dir/requirements.lock"
"$fresh_venv/bin/python" -m pip install --disable-pip-version-check --no-input --no-deps "$runtime_dir"
"$fresh_venv/bin/python" -m sql_data_analyst_local.cli doctor

if [ "$venv_existing" -eq 1 ]; then
    previous_venv=$(mktemp -d "$runtime_dir/.venv.previous.XXXXXX") || fail install_target_invalid
    transaction_state=previous_reserved
    rmdir "$previous_venv" || fail install_target_invalid
    transaction_state=moving_previous
    mv "$venv_dir" "$previous_venv" || fail install_target_invalid
    transaction_state=previous_moved
fi
transaction_state=moving_fresh
if ! mv "$fresh_venv" "$venv_dir"; then
    fail install_target_invalid
fi
fresh_venv=
transaction_state=replacement_installed
if [ -n "$previous_venv" ]; then
    remove_generated_venv "$previous_venv" || fail install_target_invalid
    previous_venv=
fi
transaction_state=complete
trap - 0 1 2 15
