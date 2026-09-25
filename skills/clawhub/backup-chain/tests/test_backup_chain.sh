#!/usr/bin/env bash
# backup-chain v1.0.0 functional test suite.
# Runs the protocol against synthetic workspaces: gates, fencing, drills,
# per-member restore, ledger adapters, refusals. No network.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
BC="python3 $HERE/../scripts/backup_chain.py"
PASS=0; FAIL=0
WS_BASE="$(mktemp -d /tmp/backup-chain-test.XXXXXX)"
trap 'rm -rf "$WS_BASE"' EXIT

ok()   { PASS=$((PASS+1)); echo "  PASS: $1"; }
bad()  { FAIL=$((FAIL+1)); echo "  FAIL: $1"; }
check() { # check <desc> <expected_rc> <actual_rc>
  if [ "$2" -eq "$3" ]; then ok "$1 (rc=$3)"; else bad "$1 (expected rc=$2, got rc=$3)"; fi
}
assert_has() { # assert_has <desc> <needle> <haystack>
  case "$3" in *"$2"*) ok "$1";; *) bad "$1 (missing: $2)";; esac
}
latest() { # latest <dir> <prefix>  → BARE filename of the matching tarball
  (cd "$1" 2>/dev/null && ls "${2}"*.tar.gz 2>/dev/null | sed 's|.*/||' | sort | tail -1)
}

echo "== T1 init + members + gated build (gen 1) =="
WS="$WS_BASE/ws"; mkdir -p "$WS"
cd "$WS" || exit 1
echo "alpha" > worklog.md
mkdir -p skills/sk1 download
echo "skill body" > skills/sk1/SKILL.md
echo "deliverable" > download/report.md
$BC init --name demo --output-dir download >/dev/null 2>&1; check "init" 0 $?
$BC init >/dev/null 2>&1; check "re-init refused without --force" 2 $?
$BC member add worklog.md --critical >/dev/null 2>&1; check "member add file" 0 $?
$BC member add skills/ >/dev/null 2>&1; check "member add dir" 0 $?
$BC member add download/ --critical >/dev/null 2>&1; check "member add output dir" 0 $?
OUT1="$($BC build --carries 'first blood' 2>&1)"; RC1=$?
check "build gen1" 0 $RC1
assert_has "drill gate passed" "restore drill: PASS" "$OUT1"
assert_has "roundtrip gate" "manifest roundtrip: OK" "$OUT1"
T1="$(latest "$WS" download/demo-g1)"
[ -n "$T1" ] && ok "tarball exists: $T1" || bad "tarball g1 missing"
[ -f "$WS/download/$T1.sha256" ] && ok "receipt exists" || bad "receipt missing"
[ ! -e "$WS/download/.download" ] && ok "no stray temp files" || bad "stray temp files"

echo "== T2 chain linkage (gen 2 parent == gen 1 sha) =="
OUT2="$($BC build --carries 'second' 2>&1)"; check "build gen2" 0 $?
T2="$(latest "$WS" download/demo-g2)"
PARENT="$(python3 -c "
import tarfile,json
with tarfile.open('$WS/download/$T2') as tf:
    print(json.load(tf.extractfile('backup-manifest.json'))['parent_sha256'])")"
G1SHA="$(cut -d' ' -f1 "$WS/download/$T1.sha256")"
if [ -n "$PARENT" ] && [ -n "$G1SHA" ] && [ "$PARENT" = "$G1SHA" ]; then
  ok "parent hash links to gen1"
else
  bad "parent mismatch: '$PARENT' vs '$G1SHA'"
fi

echo "== T3 verify: receipt MATCH, tamper detected =="
$BC verify "download/$T1" >/dev/null 2>&1; check "verify clean archive" 0 $?
cp "$WS/download/$T1" "$WS/download/tampered.tar.gz"
printf 'X' | dd of="$WS/download/tampered.tar.gz" bs=1 seek=200 conv=notrunc 2>/dev/null
$BC verify "$WS/download/tampered.tar.gz" >/dev/null 2>&1; check "verify tampered fails" 1 $?

echo "== T4 fencing: head restores, stale refuses =="
D="$($BC check "download/$T2" 2>&1)"; check "check head archive rc" 0 $?
assert_has "decision restore" '"decision": "restore"' "$D"
$BC build --carries 'third' >/dev/null 2>&1; check "build gen3" 0 $?
T3="$(latest "$WS" download/demo-g3)"
D="$($BC check "download/$T2" 2>/dev/null)"; RC=$?
check "stale check refused" 2 $RC
assert_has "stale handoff reason" "stale" "$D"

echo "== T5 per-member restore into empty target =="
TGT="$WS_BASE/target5"
R="$($BC restore "download/$T3" --target "$TGT" 2>&1)"; RC=$?
check "restore head" 0 $RC
assert_has "restored verified" "restored:" "$R"
CMP="$(python3 -c "
import hashlib
def s(p):
    h=hashlib.sha256(); h.update(open(p,'rb').read()); return h.hexdigest()
a=s('$TGT/worklog.md'); b=s('$WS/worklog.md')
c=s('$TGT/skills/sk1/SKILL.md'); d=s('$WS/skills/sk1/SKILL.md')
print('MATCH' if a==b and c==d else 'DIFFER')")"
[ "$CMP" = "MATCH" ] && ok "restored bytes identical" || bad "restored bytes differ"
RECHK="$($BC recheck 3)"; assert_has "recheck ok" '"decision": "ok"' "$RECHK"

echo "== T6 stale restore refused =="
$BC restore "download/$T2" --target "$WS_BASE/target6" >/dev/null 2>&1; check "stale restore refused" 2 $?

echo "== T7 overwrite discipline =="
echo "mutated" > "$TGT/worklog.md"
$BC restore "download/$T3" --target "$TGT" >/dev/null 2>&1; check "conflict refused w/o --overwrite" 2 $?
$BC restore "download/$T3" --target "$TGT" --overwrite >/dev/null 2>&1; check "conflict replaced with --overwrite" 0 $?
GOT="$(cat "$TGT/worklog.md")"
[ "$GOT" = "alpha" ] && ok "file actually restored" || bad "file content wrong: $GOT"

echo "== T8 dry-run writes nothing =="
CNT_BEFORE="$(find "$TGT" -type f | wc -l)"
$BC restore "download/$T3" --target "$TGT" --overwrite --dry-run >/dev/null 2>&1; check "dry-run rc" 0 $?
CNT_AFTER="$(find "$TGT" -type f | wc -l)"
[ "$CNT_BEFORE" = "$CNT_AFTER" ] && ok "dry-run wrote nothing" || bad "dry-run changed files"

echo "== T9 ledger registration survives local loss =="
$BC build --carries 'registered' --register >/dev/null 2>&1; check "registered build" 0 $?
assert_has "ledger carries gen4" "gen=4" "$(cat "$WS/.vault/ledger.log")"
mkdir -p "$WS_BASE/stash" && mv "$WS"/download/demo-g*.tar.gz* "$WS_BASE/stash/" 2>/dev/null
NG="$($BC next-gen | head -1)"
case "$NG" in 5\ *|5$'\t'*) ok "next-gen from ledger after total local loss ($NG)";; *) bad "next-gen from ledger after total local loss (got: $NG)";; esac
mv "$WS_BASE/stash"/* "$WS/download/" 2>/dev/null
T4="$(latest "$WS" download/demo-g4)"
V="$($BC verify "$WS/download/$T4" 2>&1)"
assert_has "ledger authenticity MATCH" "ledger:  MATCH" "$V"

echo "== T10 missing critical member refuses build =="
mv "$WS/worklog.md" "$WS_BASE/worklog.md.bak"
$BC build >/dev/null 2>&1; check "build with missing critical member" 1 $?
mv "$WS_BASE/worklog.md.bak" "$WS/worklog.md"

echo "== T11 drill catches corrupted member (crafted manifest) =="
python3 - "$WS_BASE/bad.tar.gz" <<'PYEOF'
import tarfile, json, io, sys
manifest = {"kind":"backup-chain workspace snapshot","protocol":"backup-chain/1",
            "chain_name":"fake","generation":99,"built_at":"2026-01-01T00:00:00Z",
            "parent_sha256":None,"member_count":1,
            "members":{"f.txt":"0"*64}}
with tarfile.open(sys.argv[1], "w:gz") as tf:
    mb = json.dumps(manifest).encode()
    ti = tarfile.TarInfo("backup-manifest.json"); ti.size = len(mb)
    tf.addfile(ti, io.BytesIO(mb))
    data = b"hello"
    ti = tarfile.TarInfo("f.txt"); ti.size = 5
    tf.addfile(ti, io.BytesIO(data))
PYEOF
$BC drill "$WS_BASE/bad.tar.gz" >/dev/null 2>&1; check "drill fails on corrupt member" 1 $?
$BC restore "$WS_BASE/bad.tar.gz" --target "$WS_BASE/t11" >/dev/null 2>&1; check "restore fails on corrupt member" 1 $?

echo "== T12 unreachable command ledger =="
WS2="$WS_BASE/ws2"; mkdir -p "$WS2"; cd "$WS2" || exit 1
echo "data" > f.txt
$BC init --name ws2 --ledger command --read-cmd "false" --append-cmd "false" >/dev/null 2>&1
$BC member add f.txt --critical >/dev/null 2>&1
$BC build --register --allow-cmd-ledger >/dev/null 2>&1; check "build with dead ledger (register fails loudly)" 1 $?
$BC build >/dev/null 2>&1; check "second build proceeds without register" 0 $?
TG2="$(latest "$WS2" download/ws2-g2)"
D="$($BC check "download/$TG2" 2>/dev/null)"
assert_has "fencing SKIPPED (marked, not silent)" '"decision": "skip"' "$D"
assert_has "skip is local-assertable" "local head" "$D"

echo "== T13 restore without config (wiped vault) =="
TGT13="$WS_BASE/target13"
mkdir -p "$TGT13"
mv "$WS2/.vault" "$WS_BASE/vault2.bak"
R="$($BC restore "download/$TG2" --target "$TGT13" 2>&1)"; RC=$?
check "restore with no vault (marked skip)" 0 $RC
assert_has "skip banner shown" "FENCING SKIPPED" "$R"
[ "$(cat "$TGT13/f.txt")" = "data" ] && ok "bytes restored" || bad "restore content wrong"
mv "$WS_BASE/vault2.bak" "$WS2/.vault"

echo "== T14 status =="
cd "$WS" || exit 1
S="$($BC status 2>&1)"; check "status rc" 0 $?
assert_has "status shows local head" "local head:" "$S"
assert_has "status shows ledger head" "head=4" "$S"

echo "== T15 in-root symlinked file nested in a directory member (dereferenced) =="
WS15="$WS_BASE/ws15"; mkdir -p "$WS15/skills" "$WS15/docs"
cd "$WS15" || exit 1
echo "wl" > worklog.md
echo "real content" > "$WS15/docs/target15.txt"
ln -s "../docs/target15.txt" skills/linked.txt
$BC init --name sym >/dev/null 2>&1
$BC member add worklog.md --critical >/dev/null 2>&1
$BC member add skills/ >/dev/null 2>&1
OUT15="$($BC build --carries 'nested in-root symlink' 2>&1)"; RC15=$?
check "build with nested in-root symlinked file" 0 $RC15
assert_has "drill covers the symlinked member" "skills/linked.txt" "$OUT15"
T15="$(latest "$WS15" download/sym-g1)"
RESTORED="$(python3 -c "
import tarfile
with tarfile.open('$WS15/download/$T15') as tf:
    print(tf.extractfile('skills/linked.txt').read().decode().strip())")"
[ "$RESTORED" = "real content" ] && ok "in-root symlinked file archived with real content" \
  || bad "symlinked file content wrong: '$RESTORED'"

echo "== T20 out-of-root nested symlink is refused at the boundary, not archived =="
echo "secret-ish external bytes" > "$WS_BASE/outside20.txt"
ln -s "$WS_BASE/outside20.txt" skills/cache.txt
OUT20="$($BC build --carries 'boundary test' 2>&1)"; RC20=$?
check "build with out-of-root nested symlink still succeeds" 0 $RC20
assert_has "out-of-root link skipped with warning" "skipping symlink escaping project root" "$OUT20"
T20="$(latest "$WS15" download/sym-g2)"
INARCHIVE="$(python3 -c "
import tarfile, json
with tarfile.open('$WS15/download/$T20') as tf:
    m = json.load(tf.extractfile('backup-manifest.json'))
    print('YES' if 'skills/cache.txt' in m['members'] else 'NO')")"
[ "$INARCHIVE" = "NO" ] && ok "out-of-root link NOT in manifest (no external bytes)" || bad "out-of-root link reached the archive"
assert_has "drill still passes with boundary skip" "restore drill: PASS" "$OUT20"
rm -f skills/cache.txt

echo "== T16 broken symlink nested in a directory member (skipped, not a crash) =="
rm -f skills/linked.txt
ln -s "$WS_BASE/does-not-exist-15.txt" skills/broken.txt
OUT16="$($BC build --carries 'nested broken symlink' 2>&1)"; RC16=$?
check "build with nested broken symlink does not crash" 0 $RC16
assert_has "broken symlink skipped with a warning" "skipping broken symlink" "$OUT16"
rm -f skills/broken.txt

echo "== T17 'member add'/'member remove' with no path argument; bad recheck input =="
$BC member add >/dev/null 2>&1; check "member add w/o path is refused, not a crash" 2 $?
$BC member remove >/dev/null 2>&1; check "member remove w/o path is refused, not a crash" 2 $?
$BC recheck not-a-number >/dev/null 2>&1; check "recheck non-integer is refused, not a traceback" 2 $?

echo "== T18 restore --dry-run previews conflicts without requiring --overwrite =="
TGT18="$WS_BASE/target18"; mkdir -p "$TGT18"
echo "different" > "$TGT18/worklog.md"
# sym-g3 = the T16 broken-symlink build (sym-g2 was consumed by T20's boundary test)
T16="$(latest "$WS15" download/sym-g3)"
OUT18="$($BC restore "download/$T16" --target "$TGT18" --dry-run 2>&1)"; RC18=$?
check "dry-run with conflicts succeeds (no --overwrite needed to preview)" 0 $RC18
assert_has "dry-run reports the conflict" "would need --overwrite" "$OUT18"
[ ! -e "$TGT18/skills" ] && ok "dry-run still wrote nothing" || bad "dry-run wrote files"

echo "== T19 non-regular files (FIFO) in a member dir are skipped, not hung on =="
mkdir -p "$WS15/pipes"
mkfifo "$WS15/pipes/pipe.fifo"
$BC member add pipes/ >/dev/null 2>&1
OUT19="$(timeout 60 $BC build --carries 'fifo guard' 2>&1)"; RC19=$?
if [ "$RC19" = "124" ]; then
  bad "build HUNG on FIFO (timeout killed it) — guard regressed"
else
  check "build with FIFO does not hang/crash" 0 $RC19
fi
assert_has "FIFO skipped with warning" "skipping non-regular file" "$OUT19"
assert_has "drill still passes after FIFO skip" "restore drill: PASS" "$OUT19"
$BC member remove pipes/ >/dev/null 2>&1

echo "== T21 restore refuses symlinked dir component beneath --target (audit T09) =="
WS21="$WS_BASE/ws21"; mkdir -p "$WS21/docs"
cd "$WS21" || exit 1
echo "note bytes" > docs/note.txt
$BC init --name sub >/dev/null 2>&1
$BC member add docs/ >/dev/null 2>&1
$BC build --carries 'restore boundary setup' >/dev/null 2>&1; check "ws21 setup build" 0 $?
T21A="$(latest "$WS21" download/sub-g1)"
mkdir -p "$WS_BASE/outside21"
TGT21="$WS_BASE/target21"; mkdir -p "$TGT21"
ln -s "$WS_BASE/outside21" "$TGT21/docs"
D21="$($BC restore "download/$T21A" --target "$TGT21" --dry-run 2>&1)"; RC21D=$?
check "dry-run previews the symlink-component refusal" 0 $RC21D
assert_has "dry-run names the offending component" "WOULD REFUSE" "$D21"
[ ! -e "$WS_BASE/outside21/note.txt" ] && ok "dry-run wrote nothing outside target" || bad "dry-run wrote through the symlink"
$BC restore "download/$T21A" --target "$TGT21" >/dev/null 2>&1; check "real restore refused on symlinked component" 2 $?
R21="$($BC restore "download/$T21A" --target "$TGT21" 2>&1)"
assert_has "refusal explains the fix" "remove or replace the symlink" "$R21"
[ ! -e "$WS_BASE/outside21/note.txt" ] && ok "refused restore wrote nothing outside target" || bad "restore escaped via symlinked dir"
rm -f "$TGT21/docs"

echo "== T22 final-component symlink: conflict, then --overwrite replaces the link itself =="
echo "outside22 bytes" > "$WS_BASE/outside22.txt"
TGT22="$WS_BASE/target22"; mkdir -p "$TGT22/docs"
ln -s "$WS_BASE/outside22.txt" "$TGT22/docs/note.txt"
$BC restore "download/$T21A" --target "$TGT22" >/dev/null 2>&1; check "symlink at final component is a conflict (refused w/o --overwrite)" 2 $?
[ -f "$WS_BASE/outside22.txt" ] && [ "$(cat "$WS_BASE/outside22.txt")" = "outside22 bytes" ] && ok "refused overwrite left link target untouched" || bad "link target was modified"
$BC restore "download/$T21A" --target "$TGT22" --overwrite >/dev/null 2>&1; check "--overwrite replaces the link itself" 0 $?
if [ ! -L "$TGT22/docs/note.txt" ] && [ "$(cat "$TGT22/docs/note.txt")" = "note bytes" ]; then
  ok "link replaced by real verified file"
else
  bad "final component wrong after overwrite (still a link or wrong content)"
fi
[ "$(cat "$WS_BASE/outside22.txt")" = "outside22 bytes" ] && ok "os.replace did not follow the link (external file intact)" || bad "external file clobbered"

echo "== T23 command-adapter execution is loud AND opted-in (1.0.3 warn + 1.0.4 flag) =="
WS3="$WS_BASE/ws3"; mkdir -p "$WS3"; cd "$WS3" || exit 1
echo "data" > f.txt
$BC init --name ws3 --ledger command \
  --read-cmd "cat $WS_BASE/ws3-ledger.ext" \
  --append-cmd "tee -a $WS_BASE/ws3-ledger.ext" >/dev/null 2>&1
$BC member add f.txt >/dev/null 2>&1
S3ERR="$($BC status --allow-cmd-ledger 2>&1 >/dev/null)"
assert_has "read execution warns at runtime" "WARN" "$S3ERR"
assert_has "warning names the executed command key" "read_cmd" "$S3ERR"
assert_has "warning points at the config file" ".vault/config.json" "$S3ERR"
B3ERR="$($BC build --register --allow-cmd-ledger 2>&1 >/dev/null)"; check "build --register with command adapter still works" 0 $?
assert_has "append execution warns at runtime" "append_cmd" "$B3ERR"
[ -s "$WS_BASE/ws3-ledger.ext" ] && ok "append_cmd still received the ledger entry" || bad "append_cmd never got the entry"
S3="$($BC status --allow-cmd-ledger 2>/dev/null)"
assert_has "ledger still parses through the warned read path" "head=1" "$S3"
J3TG="$(latest "$WS3" download/ws3-g1)"
J3="$($BC check "download/$J3TG" --allow-cmd-ledger 2>/dev/null)"
assert_has "check JSON on stdout stays warning-free" '"decision"' "$J3"

echo "== T24 command adapter refuses without explicit opt-in (1.0.4 audit T09, round 3) =="
WS4="$WS_BASE/ws4"; mkdir -p "$WS4"; cd "$WS4" || exit 1
echo "data" > f.txt
CANARY4="$WS_BASE/ws4-canary.txt"
$BC init --name ws4 --ledger command \
  --read-cmd "/bin/echo \"injected; touch $CANARY4\"" \
  --append-cmd "tee -a $WS_BASE/ws4-ledger.ext" >/dev/null 2>&1
$BC member add f.txt >/dev/null 2>&1
S4="$($BC status 2>&1)"; check "status proceeds without opt-in (refusal is marked, not fatal)" 0 $?
assert_has "read path refuses with opt-in guidance" "allow-cmd-ledger" "$S4"
[ -f "$CANARY4" ] && bad "read_cmd executed WITHOUT opt-in" || ok "read_cmd not executed without opt-in"
[ -f "$WS_BASE/ws4-ledger.ext" ] && bad "append side effect without opt-in" || ok "no ledger side effects without opt-in"
B4="$($BC build --register 2>&1)"; check "build --register without opt-in fails loudly" 1 $?
assert_has "register refusal names the opt-in flag" "allow-cmd-ledger" "$B4"
[ -f "$CANARY4" ] && bad "canary created during refused build" || ok "still no execution without opt-in"
S4B="$($BC status --allow-cmd-ledger 2>/dev/null)"
assert_has "opted-in read executes and parses" "command-adapter ledger" "$S4B"
[ -f "$CANARY4" ] && bad "shell metacharacter ';' was interpreted" || ok "argv execution leaves shell metacharacters inert"
$BC build --register --allow-cmd-ledger >/dev/null 2>&1; check "opted-in register appends through tee" 0 $?
[ -s "$WS_BASE/ws4-ledger.ext" ] && ok "append_cmd executed with opt-in" || bad "append_cmd never ran with opt-in"
$BC init --force --name ws4 --ledger command \
  --read-cmd 'cat "unclosed' --append-cmd "tee -a $WS_BASE/ws4-ledger.ext" >/dev/null 2>&1
S4C="$($BC status --allow-cmd-ledger 2>&1)"
assert_has "unparseable command line is a clean refusal (shlex)" "shlex" "$S4C"
rm -f "$CANARY4"

echo
echo "RESULTS: $PASS passed, $FAIL failed"
[ "$FAIL" -eq 0 ] || exit 1
exit 0
