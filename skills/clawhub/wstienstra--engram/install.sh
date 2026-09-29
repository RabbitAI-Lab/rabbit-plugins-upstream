#!/usr/bin/env bash
#
# Engram install.sh — install the Engram memory engine into a workspace.
#
# Flow: PREFLIGHT → STAGE → INIT → SMOKE → MIGRATE (dry-run) → next steps
#
# Usage:
#   ./install.sh [workspace_dir]    # default: the parent of this script's dir
#
# The installer never overwrites an existing engram/ directory and never
# rewrites your markdown. Migration runs as a dry-run and stops there; you
# review the report and apply it yourself.
#
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE="${1:-$(dirname "$SCRIPT_DIR")}"

RED='\033[0;31m'; GREEN='\033[0;32m'; YELLOW='\033[1;33m'; BLUE='\033[0;34m'; NC='\033[0m'
info()  { echo -e "${BLUE}i${NC}  $*"; }
ok()    { echo -e "${GREEN}ok${NC} $*"; }
warn()  { echo -e "${YELLOW}!${NC}  $*"; }
err()   { echo -e "${RED}x${NC}  $*"; }

echo "Engram installer"
info "Workspace: $WORKSPACE"
echo ""

# ── 1. PREFLIGHT ────────────────────────────────────────────────────────────
echo -e "${BLUE}── 1. PREFLIGHT ──${NC}"

PY_VER=$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
PY_MAJOR=${PY_VER%%.*}; PY_MINOR=${PY_VER##*.}
if [ "$PY_MAJOR" -ge 3 ] && [ "$PY_MINOR" -ge 10 ]; then
    ok "Python $PY_VER (3.10 or newer)"
else
    err "Python $PY_VER found. Engram needs 3.10 or newer."
    exit 1
fi

# Everything below this line is optional. Engram runs keyword-only without it.
PIP_OK=true
python3 -c "import numpy" 2>/dev/null && ok "numpy: installed" || { warn "numpy: missing. Semantic search needs it."; PIP_OK=false; }
python3 -c "import onnxruntime" 2>/dev/null && ok "onnxruntime: installed" || { warn "onnxruntime: missing. Semantic search needs it."; PIP_OK=false; }
python3 -c "import flashrank" 2>/dev/null && ok "flashrank: installed (cross-encoder rerank)" || warn "flashrank: missing. Recall falls back to lexical rerank."

HAS_OLLAMA=false
if command -v ollama &>/dev/null; then
    if ollama list 2>/dev/null | grep -q "nomic-embed-text"; then
        ok "ollama: running with nomic-embed-text"
        HAS_OLLAMA=true
    else
        warn "ollama: installed, but nomic-embed-text is not pulled. Engram will use ONNX."
        info "  To use ollama embeddings: ollama pull nomic-embed-text (about 275 MB)"
    fi
else
    warn "ollama: not installed. Engram will use ONNX, or keyword-only if ONNX is missing too."
fi

if [ "$PIP_OK" = false ] && [ "$HAS_OLLAMA" = false ]; then
    warn "No semantic search available. Installing in keyword-only mode."
    warn "Recall still works. It ranks by keywords and tags instead of meaning."
fi

AVAIL_KB=$(df "$WORKSPACE" 2>/dev/null | tail -1 | awk '{print $4}')
if [ -n "$AVAIL_KB" ] && [ "$AVAIL_KB" -lt 1048576 ]; then
    err "Less than 1 GB of disk space free ($(( AVAIL_KB / 1024 )) MB)."
    exit 1
fi
ok "Disk space: $(( AVAIL_KB / 1024 )) MB free"
echo ""

# ── 2. STAGE ────────────────────────────────────────────────────────────────
echo -e "${BLUE}── 2. STAGE ──${NC}"

ENGRAM_DIR="$WORKSPACE/engram"
SCRIPTS_DIR="$WORKSPACE/scripts"

if [ -d "$ENGRAM_DIR" ] && { [ -f "$ENGRAM_DIR/engram.py" ] || [ -f "$ENGRAM_DIR/engram.db" ]; }; then
    err "An engram/ directory already exists at $ENGRAM_DIR."
    err "Engram never overwrites an existing install. Stopping."
    err "To reinstall, run: python3 $ENGRAM_DIR/engram-uninstall.py"
    exit 1
fi

mkdir -p "$ENGRAM_DIR" "$SCRIPTS_DIR" "$WORKSPACE/logs"

# The runtime file set. engram_extras.py and build.py stay behind on purpose:
# they build engram.py, they are not part of a running install.
info "Copying engine files to $ENGRAM_DIR/"
for f in engram.py bq.py engram-serve.py engram-sleep.py engram-backup.py \
         engram-battery.py engram-migrate.py engram-rewire.py \
         engram-uninstall.py engram-seed-battery.py bpconfig.py embeddings.py \
         engram-maintenance.py engram-hygiene.py engram-aliases.py; do
    if [ -f "$SCRIPT_DIR/engine/$f" ]; then
        cp "$SCRIPT_DIR/engine/$f" "$ENGRAM_DIR/$f"
    else
        err "Missing engine file: $f"
        exit 1
    fi
done

# The cron-driven tools also live in scripts/, where the cron lines point.
for f in engram-backup.py engram-sleep.py engram-battery.py engram-maintenance.py; do
    cp "$SCRIPT_DIR/engine/$f" "$SCRIPTS_DIR/$f"
done

# The alias spec is data, not code, and it is yours. Ship the example; never
# overwrite a real aliases.json on a reinstall.
cp "$SCRIPT_DIR/engine/aliases.example.json" "$ENGRAM_DIR/aliases.example.json"

info "Writing engram/engram.json"
SEMANTIC_MODE=onnx
if [ "$PIP_OK" = false ] && [ "$HAS_OLLAMA" = false ]; then SEMANTIC_MODE=off; fi
python3 - "$WORKSPACE" "$SEMANTIC_MODE" <<'PY'
import json, os, sys
ws, mode = sys.argv[1], sys.argv[2]
cfg = {
    "workspace": ws,
    "db_path": os.path.join(ws, "engram", "engram.db"),
    "engram_dir": os.path.join(ws, "engram"),
    "scripts_dir": os.path.join(ws, "scripts"),
    "logs_dir": os.path.join(ws, "logs"),
    "backups_dir": os.path.join(ws, "backups", "engram"),
    "socket_path": os.path.join(ws, "engram", "engram-serve.sock"),
    "pid_path": os.path.join(ws, "engram", "engram-serve.pid"),
    "embed_model": "multilingual-e5-small",
    "embed_dim": 384,
    "sleep_model": "local",
    "ollama_url": "http://localhost:11434",
    "ollama_embed_model": "nomic-embed-text",
    "semantic_mode": mode,
    "flashrank_model": "ms-marco-TinyBERT-L-2-v2",
}
path = os.path.join(ws, "engram", "engram.json")
json.dump(cfg, open(path, "w"), indent=2)
print("  config:", path, "(semantic_mode:", mode + ")")
PY

chmod +x "$ENGRAM_DIR"/*.py "$SCRIPTS_DIR"/engram-*.py 2>/dev/null || true
ok "Engine staged"
echo ""

# ── 3. INIT ─────────────────────────────────────────────────────────────────
echo -e "${BLUE}── 3. INIT ──${NC}"

cd "$WORKSPACE"
info "Creating engram.db"
python3 "$ENGRAM_DIR/engram.py" calibrate 2>&1 | head -5 || true

if [ ! -f "$ENGRAM_DIR/engram.db" ]; then
    err "engram.db was not created. Init failed."
    exit 1
fi
ok "Fresh engram.db created"

if python3 -c "import onnxruntime" 2>/dev/null; then
    info "Starting the warm daemon (optional)"
    nohup python3 "$ENGRAM_DIR/engram-serve.py" > "$WORKSPACE/logs/engram-serve.log" 2>&1 &
    sleep 2
    if python3 "$ENGRAM_DIR/bq.py" tags >/dev/null 2>&1; then
        ok "Daemon answering"
    else
        warn "Daemon not answering. Engram will call the CLI directly, which is fine."
    fi
else
    info "No ONNX runtime. Skipping the daemon."
fi
echo ""

# ── 4. SMOKE ────────────────────────────────────────────────────────────────
echo -e "${BLUE}── 4. SMOKE ──${NC}"
#
# The first recall against a brand-new database is the one that broke in
# v1.1.x: the schema did not create the columns recall reads, so every fresh
# install crashed on its first question. It is cheap to check, so the
# installer checks it rather than leaving the user to find out.
#
python3 "$ENGRAM_DIR/engram.py" store --name "engram install smoke" --type fact \
    --content "Engram was installed on $(date -u +%Y-%m-%dT%H:%M:%SZ)." >/dev/null
if python3 "$ENGRAM_DIR/engram.py" recall "engram install smoke" --limit 3 >/dev/null; then
    ok "Store and recall both work on a fresh database"
else
    err "The first recall on a fresh database failed. Stopping before migration."
    err "Please report this with the output above: https://github.com/WStienstra/engram/issues"
    exit 1
fi
python3 "$ENGRAM_DIR/engram.py" delete --name "engram install smoke" >/dev/null 2>&1 || true
echo ""

# ── 5. MIGRATE (dry-run) ────────────────────────────────────────────────────
echo -e "${BLUE}── 5. MIGRATE (dry-run) ──${NC}"

info "Reading MEMORY.md, memory/*.md and AGENTS.md"
python3 "$ENGRAM_DIR/engram-migrate.py" --dry-run 2>&1

REPORT_PATH="$WORKSPACE/migration-report.md"
if [ -f "$REPORT_PATH" ]; then
    ok "Migration report: $REPORT_PATH"
else
    warn "No migration report was written. No markdown memory found in this workspace."
fi
echo ""

# ── 6. NEXT STEPS ───────────────────────────────────────────────────────────
echo -e "${BLUE}── 6. NEXT STEPS ──${NC}"
cat <<EOF
Nothing has been migrated yet, and your markdown files are untouched.

  1. Read $REPORT_PATH.
  2. Apply it:    python3 engram/engram-migrate.py --apply
  3. Verify it:   python3 engram/engram-seed-battery.py
  4. Optional — let Engram slim MEMORY.md and add its crons:
                  python3 engram/engram-rewire.py
     This backs up every file it touches to .engram-backup/ first.

Daily use:

  python3 engram/engram.py recall "hosting setup"        ask a question
  python3 engram/engram.py msgctx "<user message>"       context for one message
  python3 engram/engram.py store --name N --type fact --content "..."
  python3 engram/engram.py task add <name> --brief "..." --evidence "<cmd>"
  python3 engram/engram.py startup                       session briefing

Wire msgctx into your agent as a per-message hook. It takes the incoming
message, returns a short block of relevant memory, and stays quiet when it has
nothing worth saying.

To remove Engram: python3 engram/engram-uninstall.py
EOF
