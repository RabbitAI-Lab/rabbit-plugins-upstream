#!/bin/bash
# ============================================================
# WatchItAI - macOS Permissions Preflight Helper
#
# Checks and requests required macOS permissions:
#   1. Screen Recording (for screen sharing / capture)
#   2. Accessibility (for mouse / keyboard control)
#   3. Input Monitoring (for key event listening)
#
# Usage:
#   bash scripts/ensure_macos_permissions.sh
#   bash scripts/ensure_macos_permissions.sh --silent
#
# Combine with capture/control to reduce sandbox prompts:
#   bash scripts/ensure_macos_permissions.sh && bash run.sh test-mouse
# ============================================================

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
SILENT=false

for arg in "$@"; do
  case "$arg" in
    --silent) SILENT=true ;;
  esac
done

# Route Swift module cache to TMPDIR to avoid sandbox module-cache prompts
export SWIFT_MODULE_CACHE="$TMPDIR/watchitai-swift-module-cache"
mkdir -p "$SWIFT_MODULE_CACHE"
export XCSOAR_SWIFTC_FLAGS="-module-cache-path $SWIFT_MODULE_CACHE"

$SILENT || echo "🔐 WatchItAI macOS Permissions Preflight"
$SILENT || echo ""

# ------------------------------------------------------------
# 1. Screen Recording Permission
# ------------------------------------------------------------
check_screen_recording() {
  $SILENT || echo "📹 Checking Screen Recording permission..."

  # Try a tiny screencapture to /dev/null to trigger the prompt if not granted
  local test_file="$TMPDIR/watchitai_screen_test.png"
  screencapture -x -R0,0,1,1 "$test_file" 2>/dev/null || true

  # Check if we actually got an image (permission granted = file exists and >0)
  if [ -f "$test_file" ] && [ -s "$test_file" ]; then
    rm -f "$test_file"
    $SILENT || echo "   ✅ Screen Recording: granted"
    return 0
  else
    rm -f "$test_file"
    $SILENT || echo "   ⚠️  Screen Recording: not granted (prompt may appear)"
    $SILENT || echo "      Go to System Settings → Privacy & Security → Screen Recording"
    $SILENT || echo "      and enable permission for your terminal / Trae."
    return 1
  fi
}

# ------------------------------------------------------------
# 2. Accessibility Permission (for mouse/keyboard control)
# ------------------------------------------------------------
check_accessibility() {
  $SILENT || echo "🖱️  Checking Accessibility permission..."

  # Use AppleScript System Events to test accessibility
  local result
  result=$(osascript -e 'tell application "System Events" to get name of first process' 2>&1) || true

  if echo "$result" | grep -q "System Events"; then
    # Got a process name = permission granted
    $SILENT || echo "   ✅ Accessibility: granted"
    return 0
  elif echo "$result" | grep -q "Error"; then
    $SILENT || echo "   ⚠️  Accessibility: not granted (prompt may appear)"
    $SILENT || echo "      Go to System Settings → Privacy & Security → Accessibility"
    $SILENT || echo "      and enable permission for your terminal / Trae."
    return 1
  else
    $SILENT || echo "   ✅ Accessibility: granted"
    return 0
  fi
}

# ------------------------------------------------------------
# 3. Input Monitoring Permission
# ------------------------------------------------------------
check_input_monitoring() {
  $SILENT || echo "⌨️  Checking Input Monitoring permission..."

  # Input monitoring is harder to check programmatically
  # We assume it's needed for keyboard event listening
  if [ -d "/Library/Application Support/com.apple.TCC" ] 2>/dev/null; then
    # Can't directly check without special entitlements; just inform user
    $SILENT || echo "   ℹ️  Input Monitoring: cannot auto-check"
    $SILENT || echo "      If keyboard control doesn't work, go to:"
    $SILENT || echo "      System Settings → Privacy & Security → Input Monitoring"
  fi
  return 0
}

# ------------------------------------------------------------
# Main
# ------------------------------------------------------------
main() {
  local screen_ok=0
  local access_ok=0

  check_screen_recording || screen_ok=1
  $SILENT || echo ""

  check_accessibility || access_ok=1
  $SILENT || echo ""

  check_input_monitoring
  $SILENT || echo ""

  if [ "$screen_ok" -eq 0 ] && [ "$access_ok" -eq 0 ]; then
    $SILENT || echo "✅ All critical permissions are granted."
    exit 0
  else
    $SILENT || echo "⚠️  Some permissions are missing. Features may not work correctly."
    $SILENT || echo "   Grant the required permissions and re-run this script."
    exit 1
  fi
}

main "$@"
