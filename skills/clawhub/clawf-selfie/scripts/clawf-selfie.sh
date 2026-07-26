#!/bin/bash
# clawf-selfie.sh
# Generate a Clawf selfie via aibotclaw.com and send it via OpenClaw
#
# Usage: ./clawf-selfie.sh "<prompt>" "<channel>" ["<caption>"]
#
# Environment variables required:
#   CRS_API_KEY_ID - Your aibotclaw.com API key
#
# Example:
#   CRS_API_KEY_ID=your_key ./clawf-selfie.sh "wearing a santa hat" "#general" "Happy holidays!"

set -euo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

log_info()  { echo -e "${GREEN}[INFO]${NC} $1"; }
log_warn()  { echo -e "${YELLOW}[WARN]${NC} $1"; }
log_error() { echo -e "${RED}[ERROR]${NC} $1"; }

# Check required environment variables
if [ -z "${CRS_API_KEY_ID:-}" ]; then
    log_error "CRS_API_KEY_ID environment variable not set"
    exit 1
fi

# Check for jq
if ! command -v jq &> /dev/null; then
    log_error "jq is required but not installed"
    echo "Install with: brew install jq (macOS) or apt install jq (Linux)"
    exit 1
fi

# Check for openclaw
if ! command -v openclaw &> /dev/null; then
    log_warn "openclaw CLI not found - will attempt direct API call"
    USE_CLI=false
else
    USE_CLI=true
fi

# Parse arguments
PROMPT="${1:-}"
CHANNEL="${2:-}"
CAPTION="${3:-}"
IMAGE_SIZE="${4:-9:16}"
OUTPUT_FORMAT="${5:-jpeg}"

# Read reference image from character.json (falls back to default if not found)
_CHAR_JSON="${OPENCLAW_HOME:-/root/.openclaw}/workspace/character.json"
if [ -f "$_CHAR_JSON" ] && command -v jq &>/dev/null; then
    REFERENCE_IMAGE=$(jq -r '.reference_image_url // empty' "$_CHAR_JSON")
fi
if [ -z "${REFERENCE_IMAGE:-}" ]; then
    REFERENCE_IMAGE="https://cdn.jsdelivr.net/gh/SumeLabs/clawra@main/assets/clawra.png"
fi

if [ -z "$PROMPT" ] || [ -z "$CHANNEL" ]; then
    echo "Usage: $0 <prompt> <channel> [caption] [image_size] [output_format]"
    echo ""
    echo "Arguments:"
    echo "  prompt        - Image description (required)"
    echo "  channel       - Target channel (required) e.g., #general, @user"
    echo "  caption       - Message caption (default: empty)"
    echo "  image_size    - Image ratio (default: 9:16) Options: 1:1, 9:16, 16:9, 3:4, 4:3"
    echo "  output_format - Image format (default: jpeg) Options: jpeg, png"
    echo ""
    echo "Example:"
    echo "  $0 \"wearing a cyberpunk outfit\" \"#art-gallery\" \"Check this out!\""
    exit 1
fi

log_info "Generating selfie via aibotclaw..."
log_info "Prompt: $PROMPT"
log_info "Image size: $IMAGE_SIZE"

# Build JSON payload
JSON_PAYLOAD=$(jq -n \
    --arg api_key "$CRS_API_KEY_ID" \
    --arg ref_image "$REFERENCE_IMAGE" \
    --arg prompt "$PROMPT" \
    --arg image_size "$IMAGE_SIZE" \
    --arg output_format "$OUTPUT_FORMAT" \
    '{crs_api_key_id: $api_key, image_urls: [$ref_image], prompt: $prompt, image_size: $image_size, output_format: $output_format}')

# Call aibotclaw API (can take up to 60s, set timeout to 70s)
API_URL="${CRS_API_URL:-https://aibotclaw.com/api/external/image/generate}"
RESPONSE=$(curl -s -X POST "$API_URL" \
    -H "Content-Type: application/json" \
    --max-time 70 \
    -d "$JSON_PAYLOAD")

# Check success field
SUCCESS=$(echo "$RESPONSE" | jq -r '.success // false')
if [ "$SUCCESS" != "true" ]; then
    ERROR_MSG=$(echo "$RESPONSE" | jq -r '.error // "Unknown error"')
    log_error "Image generation failed: $ERROR_MSG"
    exit 1
fi

# Extract image URL
IMAGE_URL=$(echo "$RESPONSE" | jq -r '.data.result_urls[0] // empty')

if [ -z "$IMAGE_URL" ]; then
    log_error "Failed to extract image URL from response"
    echo "Response: $RESPONSE"
    exit 1
fi

log_info "Image generated successfully!"
log_info "URL: $IMAGE_URL"

# Send via OpenClaw
log_info "Sending to channel: $CHANNEL"

if [ "$USE_CLI" = true ]; then
    openclaw message send \
        --action send \
        --channel "$CHANNEL" \
        --message "$CAPTION" \
        --media "$IMAGE_URL"
else
    GATEWAY_URL="${OPENCLAW_GATEWAY_URL:-http://localhost:18789}"
    GATEWAY_TOKEN="${OPENCLAW_GATEWAY_TOKEN:-}"

    curl -s -X POST "$GATEWAY_URL/message" \
        -H "Content-Type: application/json" \
        ${GATEWAY_TOKEN:+-H "Authorization: Bearer $GATEWAY_TOKEN"} \
        -d "{
            \"action\": \"send\",
            \"channel\": \"$CHANNEL\",
            \"message\": \"$CAPTION\",
            \"media\": \"$IMAGE_URL\"
        }"
fi

log_info "Done! Image sent to $CHANNEL"

echo ""
echo "--- Result ---"
jq -n \
    --arg url "$IMAGE_URL" \
    --arg channel "$CHANNEL" \
    --arg prompt "$PROMPT" \
    '{success: true, image_url: $url, channel: $channel, prompt: $prompt}'
