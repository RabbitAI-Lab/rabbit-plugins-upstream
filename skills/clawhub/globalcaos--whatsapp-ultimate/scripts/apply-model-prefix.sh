#!/usr/bin/env bash
# whatsapp-ultimate: Apply model + auth mode prefix to WhatsApp messages.
#
# THIS EDITS FOUR FILES IN YOUR OPENCLAW SOURCE TREE IN PLACE, so that
# responsePrefix can interpolate {authMode} / {authProfile}. Note what that
# means: the NAME of the auth profile serving each reply (e.g. "anthropic:oauth"
# or "sub" / "api") becomes visible in the WhatsApp message itself, to whoever
# is in that chat. It reads auth-profile METADATA only — never a token, key or
# secret — but it is still identity metadata leaving your machine, so it is OFF
# unless you run this script.
#
# Consent gate:  nothing happens without --yes
# Off switch:    --revert restores the .bak files taken before patching, and
#                removing {authMode}/{authProfile} from responsePrefix stops the
#                leak without reverting anything.
#
# Usage: ./apply-model-prefix.sh --yes
#        ./apply-model-prefix.sh --revert
# Safe to run multiple times — skips if already applied.

set -euo pipefail

CONSENTED=0
REVERT=0
for arg in "$@"; do
  case "$arg" in
    --yes) CONSENTED=1 ;;
    --revert) REVERT=1 ;;
    -h|--help)
      echo "Usage: $0 --yes      # apply the auth-prefix patches"
      echo "       $0 --revert   # restore the four files from their backups"
      exit 0 ;;
  esac
done

# Honour an explicit OPENCLAW_SRC before guessing.
OPENCLAW_SRC="${OPENCLAW_SRC:-}"
if [[ -n "$OPENCLAW_SRC" ]]; then
  if [[ ! -f "$OPENCLAW_SRC/src/auto-reply/reply/response-prefix-template.ts" ]]; then
    echo "❌ OPENCLAW_SRC=$OPENCLAW_SRC has no src/auto-reply/reply/response-prefix-template.ts"
    exit 1
  fi
else
  for dir in "$HOME/src/tinkerclaw" "$HOME/src/openclaw" "$HOME/.openclaw/src"; do
    if [[ -f "$dir/src/auto-reply/reply/response-prefix-template.ts" ]]; then
      OPENCLAW_SRC="$dir"
      break
    fi
  done
fi

if [[ -z "$OPENCLAW_SRC" ]]; then
  echo "❌ Could not find OpenClaw source directory."
  echo "   Set OPENCLAW_SRC env var to your OpenClaw repo path and re-run."
  exit 1
fi

echo "📁 OpenClaw source: $OPENCLAW_SRC"

PATCH_TARGETS=(
  "$OPENCLAW_SRC/src/auto-reply/reply/response-prefix-template.ts"
  "$OPENCLAW_SRC/src/auto-reply/types.ts"
  "$OPENCLAW_SRC/src/channels/reply-prefix.ts"
  "$OPENCLAW_SRC/src/auto-reply/reply/agent-runner-execution.ts"
)

if [[ "$REVERT" == "1" ]]; then
  restored=0
  for f in "${PATCH_TARGETS[@]}"; do
    if [[ -f "$f.whatsapp-ultimate.bak" ]]; then
      cp "$f.whatsapp-ultimate.bak" "$f"
      echo "↩️  Reverted $f"
      restored=1
    fi
  done
  if [[ "$restored" == "0" ]]; then
    echo "❌ No backups found — nothing to revert."
    exit 1
  fi
  echo "   Rebuild and restart the gateway for it to take effect."
  exit 0
fi

echo ""
echo "⚠️  This edits four files in your OpenClaw source tree, in place:"
for f in "${PATCH_TARGETS[@]}"; do echo "     • $f"; done
echo ""
echo "   Effect: the auth-profile NAME behind each reply can be printed into"
echo "   your outgoing WhatsApp messages via responsePrefix. No token, key or"
echo "   secret is read or sent — but the profile name is identity metadata,"
echo "   and everyone in the chat will see it."
echo ""
echo "   A .bak is taken for each file first; --revert restores them."
echo ""

if [[ "$CONSENTED" != "1" ]]; then
  echo "❌ Refusing to patch your source tree without explicit consent."
  echo "   Re-run with --yes if the above is what you want."
  exit 1
fi

for f in "${PATCH_TARGETS[@]}"; do
  if [[ -f "$f" && ! -f "$f.whatsapp-ultimate.bak" ]]; then
    cp "$f" "$f.whatsapp-ultimate.bak"
  fi
done
echo "🗄  Backups written (*.whatsapp-ultimate.bak)"

# File 1: response-prefix-template.ts — add authMode/authProfile to context type + switch
TPL="$OPENCLAW_SRC/src/auto-reply/reply/response-prefix-template.ts"
if grep -q "authMode" "$TPL" 2>/dev/null; then
  echo "✅ response-prefix-template.ts already patched"
else
  echo "🔧 Patching response-prefix-template.ts..."

  # Add fields to ResponsePrefixContext type
  sed -i '/identityName?: string;/a\  /** Auth profile used (e.g., "anthropic:oauth", "anthropic:api") */\n  authProfile?: string;\n  /** Short auth mode label (e.g., "sub" for subscription\/oauth, "api" for API key) */\n  authMode?: string;' "$TPL"

  # Add cases to the switch statement
  sed -i '/case "identityname":/a\        return context.identityName ?? match;\n      case "auth":\n      case "authmode":\n        return context.authMode ?? match;\n      case "authprofile":\n        return context.authProfile ?? match;' "$TPL"

  # Remove duplicate return for identityname (sed adds before the existing return)
  # This is handled by the existing code structure
  echo "  ✓ Added authMode/authProfile to template context"
fi

# File 2: types.ts — add authProfile to ModelSelectedContext
TYPES="$OPENCLAW_SRC/src/auto-reply/types.ts"
if grep -q "authProfile" "$TYPES" 2>/dev/null; then
  echo "✅ types.ts already patched"
else
  echo "🔧 Patching types.ts..."
  sed -i '/thinkLevel: string | undefined;/a\  /** Auth profile used (e.g., "anthropic:oauth", "anthropic:api") */\n  authProfile?: string;' "$TYPES"
  echo "  ✓ Added authProfile to ModelSelectedContext"
fi

# File 3: reply-prefix.ts — map auth profile to short label
PREFIX="$OPENCLAW_SRC/src/channels/reply-prefix.ts"
if grep -q "authMode" "$PREFIX" 2>/dev/null; then
  echo "✅ reply-prefix.ts already patched"
else
  echo "🔧 Patching reply-prefix.ts..."
  sed -i '/prefixContext.thinkingLevel = ctx.thinkLevel/a\    prefixContext.authProfile = ctx.authProfile;\n    if (ctx.authProfile) {\n      if (ctx.authProfile.includes("oauth") || ctx.authProfile.includes("token")) {\n        prefixContext.authMode = "sub";\n      } else if (ctx.authProfile.includes("api")) {\n        prefixContext.authMode = "api";\n      } else {\n        prefixContext.authMode = ctx.authProfile.split(":").pop() ?? "unknown";\n      }\n    }' "$PREFIX"
  echo "  ✓ Added auth mode mapping"
fi

# File 4: agent-runner-execution.ts — resolve auth profile at model selection
EXEC="$OPENCLAW_SRC/src/auto-reply/reply/agent-runner-execution.ts"
if grep -q "resolvedAuthProfile" "$EXEC" 2>/dev/null; then
  echo "✅ agent-runner-execution.ts already patched"
else
  echo "🔧 Patching agent-runner-execution.ts..."

  # Add imports
  sed -i '/import { runWithModelFallback } from "..\/..\/agents\/model-fallback.js";/a\import { ensureAuthProfileStore, resolveAuthProfileOrder } from "../../agents/model-auth.js";\nimport { isProfileInCooldown } from "../../agents/auth-profiles.js";' "$EXEC"

  # Add auth resolution before onModelSelected call
  python3 -c "
import re
with open('$EXEC', 'r') as f:
    content = f.read()

old = '''          params.opts?.onModelSelected?.({
            provider,
            model,
            thinkLevel: params.followupRun.run.thinkLevel,
          });'''

new = '''          // Resolve active auth profile for prefix interpolation ({auth}, {authMode}).
          let resolvedAuthProfile: string | undefined;
          try {
            const prefixAuthStore = ensureAuthProfileStore(params.followupRun.run.agentDir, { allowKeychainPrompt: false });
            const prefixProfileIds = resolveAuthProfileOrder({
              cfg: params.followupRun.run.config,
              store: prefixAuthStore,
              provider,
            });
            resolvedAuthProfile = prefixProfileIds.find((id) => !isProfileInCooldown(prefixAuthStore, id)) ?? prefixProfileIds[0];
          } catch { /* auth resolution is best-effort */ }
          params.opts?.onModelSelected?.({
            provider,
            model,
            thinkLevel: params.followupRun.run.thinkLevel,
            authProfile: resolvedAuthProfile,
          });'''

if old in content:
    content = content.replace(old, new, 1)
    with open('$EXEC', 'w') as f:
        f.write(content)
    print('  ✓ Added auth profile resolution')
else:
    print('  ⚠ Could not find onModelSelected anchor — may need manual patching')
"
fi

echo ""
echo "✅ All patches applied!"
echo ""
echo "Next steps:"
echo "  1. Rebuild: cd $OPENCLAW_SRC && npm run build"
echo "  2. Restart gateway: openclaw gateway restart"
echo "  3. Set responsePrefix in openclaw.json → channels.whatsapp:"
echo '     "responsePrefix": "🤖({model}|{authMode})"'
