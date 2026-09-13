#!/usr/bin/env bash
# Focused tests for wordpress-ultimate safety gates. Runs against a COPY of the
# scripts in a throwaway skill dir — the real skill's .env is never read.
set -uo pipefail
SRC=/home/globalcaos/.openclaw/workspace/skills/wordpress-ultimate
T=$(mktemp -d /tmp/wp-skill.XXXXXX)
mkdir -p "$T/scripts"
cp "$SRC/scripts/wp.sh" "$SRC/scripts/wp-upload.sh" "$SRC/scripts/wp-credentials.sh" "$T/scripts/"
printf 'WP_URL=https://example.com\nWP_USER=t@example.com\nWP_APP_PASSWORD=aaaa bbbb cccc dddd\n' > "$T/.env"
chmod 600 "$T/.env"
WP="$T/scripts/wp.sh"
pass=0; fail=0
ok(){ printf '  \033[32mPASS\033[0m %s\n' "$1"; pass=$((pass+1)); }
no(){ printf '  \033[31mFAIL\033[0m %s\n       %s\n' "$1" "$2"; fail=$((fail+1)); }

run(){ local desc="$1" expect="$2" want="$3"; shift 4
  local out rc
  out=$(WP_DRY_RUN=1 "$WP" "$@" 2>&1); rc=$?
  if [[ "$expect" == block ]]; then
    if [[ $rc -eq 0 ]]; then no "$desc" "expected refusal, exited 0: $out"; return; fi
  else
    if [[ $rc -ne 0 ]]; then no "$desc" "expected success, exited $rc: $out"; return; fi
  fi
  if [[ -n "$want" && ! "$out" =~ $want ]]; then no "$desc" "output missing /$want/: $out"; return; fi
  ok "$desc"
}

echo "== route canonicalisation: the gate must see what the server will resolve =="
run "POST //plugins BLOCKED (was a bypass: gate saw '/plugins')" block "site-administration write" -- POST "//plugins" '{"slug":"x"}'
run "POST ///plugins BLOCKED"                        block "site-administration write" -- POST "///plugins" '{"slug":"x"}'
run "POST %70lugins BLOCKED (percent-encoded)"       block "site-administration write" -- POST "%70lugins" '{"slug":"x"}'
run "POST PLUGINS BLOCKED (case)"                    block "site-administration write" -- POST "PLUGINS" '{"slug":"x"}'
run "POST plugins/ BLOCKED (trailing slash)"         block "site-administration write" -- POST "plugins/" '{"slug":"x"}'
run "POST posts/../plugins REFUSED (traversal)"      block "relative path segment"      -- POST "posts/../plugins" '{"slug":"x"}'
run "POST plugins BLOCKED (baseline regression)"     block "site-administration write" -- POST "plugins" '{"slug":"x"}'
run "POST //users BLOCKED"                           block "site-administration write" -- POST "//users" '{"x":1}'
run "PUT //settings BLOCKED"                         block "site-administration write" -- PUT  "//settings" '{"x":1}'

echo "== admin reads stay free, and the URL is normalised =="
run "GET plugins allowed"                            allow "wp-json/wp/v2/plugins"      -- GET "plugins"
run "GET //plugins normalises the sent URL"          allow "wp/v2/plugins"              -- GET "//plugins"
out=$(WP_DRY_RUN=1 "$WP" GET "//plugins" 2>&1)
if [[ "$out" == *"wp/v2//plugins"* ]]; then no "no double slash in sent URL" "$out"; else ok "no double slash in sent URL"; fi

echo "== publish / draft / delete gates (regression) =="
run "POST posts status=publish gated"                block "Publishing is gated"        -- POST "posts" '{"title":"x","status":"publish"}'
run "PUT posts/42 gated"                             block "Editing live posts"         -- PUT  "posts/42" '{"title":"x"}'
run "PUT //posts/42 gated (was a bypass)"            block "Editing live posts"         -- PUT  "//posts/42" '{"title":"x"}'
run "DELETE posts/42?force=true blocked"             block "Permanent DELETE"           -- DELETE "posts/42?force=true"
run "DELETE posts/42?force=TRUE blocked (case)"      block "Permanent DELETE"           -- DELETE "posts/42?force=TRUE"
run "DELETE posts/42 (trash) allowed"                allow ""                           -- DELETE "posts/42"
out=$(WP_DRY_RUN=1 WP_ALLOW_PUBLISH=1 "$WP" POST posts '{"title":"x"}' 2>&1)
if [[ $? -eq 0 ]]; then ok "POST posts allowed with flag"; else no "POST posts allowed with flag" "$out"; fi

echo "== query strings survive normalisation =="
out=$(WP_DRY_RUN=1 "$WP" GET 'posts?search=a//b&per_page=5' 2>&1)
if [[ "$out" == *'search=a//b&per_page=5'* ]]; then ok "query value 'a//b' not mangled"; else no "query value 'a//b' not mangled" "$out"; fi

echo "== off switch =="
out=$(WP_DRY_RUN=1 WP_READONLY=1 "$WP" POST posts '{"t":1}' 2>&1); rc=$?
if [[ $rc -ne 0 && "$out" == *"WP_READONLY is set"* ]]; then ok "WP_READONLY=1 blocks POST"; else no "WP_READONLY=1 blocks POST" "$out"; fi
out=$(WP_DRY_RUN=1 WP_READONLY=1 "$WP" GET posts 2>&1); rc=$?
if [[ $rc -eq 0 ]]; then ok "WP_READONLY=1 still allows GET"; else no "WP_READONLY=1 still allows GET" "$out"; fi

echo "== implicit <skill>/.env now gets the SAME validation as WP_ENV_FILE =="
chmod 644 "$T/.env"
out=$(WP_DRY_RUN=1 "$WP" GET posts 2>&1); rc=$?
if [[ $rc -ne 0 && "$out" == *"group/world readable"* ]]; then ok "mode 0644 <skill>/.env refused (was unchecked)"; else no "mode 0644 <skill>/.env refused" "rc=$rc $out"; fi
chmod 600 "$T/.env"
mv "$T/.env" "$T/real.env"; ln -s "$T/real.env" "$T/.env"
out=$(WP_DRY_RUN=1 "$WP" GET posts 2>&1); rc=$?
if [[ $rc -ne 0 && "$out" == *"must not be a symlink"* ]]; then ok "symlinked <skill>/.env refused (was unchecked)"; else no "symlinked <skill>/.env refused" "rc=$rc $out"; fi
rm -f "$T/.env"; mv "$T/real.env" "$T/.env"; chmod 600 "$T/.env"

echo "== no secret on argv anywhere =="
if grep -qE 'curl[^|]*-u "\$\{?WP_USER' "$T/scripts/wp-upload.sh"; then no "wp-upload.sh has no curl -u" "found -u"; else ok "wp-upload.sh has no curl -u"; fi
if grep -q 'netrc-file' "$T/scripts/wp-upload.sh"; then ok "wp-upload.sh uses --netrc-file"; else no "wp-upload.sh uses --netrc-file" "not found"; fi
for f in wp.sh wp-upload.sh; do
  if grep -q 'wp-credentials.sh' "$T/scripts/$f"; then ok "$f sources the shared loader"; else no "$f sources the shared loader" "not found"; fi
done

echo "== netrc trap: no credential file survives a failure =="
if grep -q 'trap wp_netrc_cleanup' "$T/scripts/wp-credentials.sh"; then ok "netrc cleanup is trapped on EXIT/HUP/INT/TERM"; else no "netrc cleanup is trapped" "no trap"; fi

find "$T" -mindepth 1 -delete 2>/dev/null; rmdir "$T" 2>/dev/null
echo; echo "wordpress-ultimate: $pass passed, $fail failed"
[[ $fail -eq 0 ]]
