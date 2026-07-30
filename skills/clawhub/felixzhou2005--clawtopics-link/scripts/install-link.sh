#!/usr/bin/env bash
set -euo pipefail
export LC_ALL=C
export LANG=C

version="0.1.0"
base_url="https://openclaw.tekoai.com/clawtopics-link/releases/v${version}"
verify_only=false

if [[ "${1:-}" == "--verify-only" && "$#" -eq 1 ]]; then
  verify_only=true
elif [[ "$#" -ne 0 ]]; then
  echo "Usage: install-link.sh [--verify-only]" >&2
  exit 2
fi

case "$(uname -s)" in
  Darwin) operating_system="darwin" ;;
  Linux) operating_system="linux" ;;
  *)
    echo "Unsupported operating system. Use install-link.ps1 on Windows." >&2
    exit 1
    ;;
esac

case "$(uname -m)" in
  x86_64|amd64) architecture="amd64" ;;
  arm64|aarch64) architecture="arm64" ;;
  *)
    echo "Unsupported CPU architecture." >&2
    exit 1
    ;;
esac

case "${operating_system}/${architecture}" in
  darwin/amd64)
    expected_sha256="0397caec7919974fc03f598e08a1b117b2abb32c485d06ba8343cdab24c08a72"
    expected_size="3005083"
    ;;
  darwin/arm64)
    expected_sha256="07f40ac5c7ff8dcc114f616eb320fac62a339e435f87ebf03add37f144bd357d"
    expected_size="2784469"
    ;;
  linux/amd64)
    expected_sha256="283fcb9a830a3e86729f4f33757a8021ad413a1fc07507ea09f2d13520e23f11"
    expected_size="2976818"
    ;;
  linux/arm64)
    expected_sha256="acd261255b100f37e7a57f2238980ee790a55067c140cc169761039014692547"
    expected_size="2701281"
    ;;
esac

artifact="clawtopics-link_${version}_${operating_system}_${architecture}.tar.gz"
url="${base_url}/${artifact}"
temporary_dir="$(mktemp -d "${TMPDIR:-/tmp}/clawtopics-link.XXXXXXXX")"
case "$temporary_dir" in
  */clawtopics-link.*) ;;
  *)
    echo "Refusing unsafe temporary directory." >&2
    exit 1
    ;;
esac
trap 'rm -rf -- "$temporary_dir"' EXIT
archive_path="${temporary_dir}/${artifact}"

curl \
  --fail \
  --silent \
  --show-error \
  --proto '=https' \
  --tlsv1.2 \
  --max-redirs 0 \
  --output "$archive_path" \
  "$url"

actual_size="$(wc -c <"$archive_path" | tr -d '[:space:]')"
if [[ "$actual_size" != "$expected_size" ]]; then
  echo "Artifact size verification failed." >&2
  exit 1
fi

if command -v sha256sum >/dev/null 2>&1; then
  actual_sha256="$(sha256sum "$archive_path" | awk '{print $1}')"
elif command -v shasum >/dev/null 2>&1; then
  actual_sha256="$(shasum -a 256 "$archive_path" | awk '{print $1}')"
elif command -v openssl >/dev/null 2>&1; then
  actual_sha256="$(openssl dgst -sha256 "$archive_path" | awk '{print $NF}')"
else
  echo "No supported SHA-256 verification tool is available." >&2
  exit 1
fi

if [[ "$actual_sha256" != "$expected_sha256" ]]; then
  echo "Artifact SHA-256 verification failed." >&2
  exit 1
fi

archive_listing="$(tar -tzf "$archive_path")"
if [[ "$archive_listing" != "clawtopics-link" ]]; then
  echo "Artifact contains an unexpected path." >&2
  exit 1
fi
tar -xzf "$archive_path" -C "$temporary_dir"
chmod 700 "$temporary_dir/clawtopics-link"

actual_version="$("$temporary_dir/clawtopics-link" version)"
if [[ "$actual_version" != "$version" ]]; then
  echo "Link version verification failed." >&2
  exit 1
fi

if [[ "$verify_only" == "true" ]]; then
  echo "Verified ClawTopics Link ${version} for ${operating_system}/${architecture}."
  exit 0
fi

if [[ -z "${HOME:-}" || "$HOME" == "/" ]]; then
  echo "A valid user home directory is required." >&2
  exit 1
fi
if [[ "$operating_system" == "darwin" ]]; then
  destination="${HOME}/Library/Application Support/ClawTopics Link/bootstrap/clawtopics-link"
else
  destination="${XDG_DATA_HOME:-${HOME}/.local/share}/clawtopics-link/bootstrap/clawtopics-link"
fi

mkdir -p "$(dirname "$destination")"
chmod 700 "$(dirname "$destination")"
staged_destination="${destination}.new.$$"
cp "$temporary_dir/clawtopics-link" "$staged_destination"
chmod 700 "$staged_destination"
mv "$staged_destination" "$destination"

echo "Installed verified ClawTopics Link ${version}: ${destination}"
