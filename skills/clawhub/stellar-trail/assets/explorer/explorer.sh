#!/usr/bin/env bash
# ============================================================================
# explorer.sh — LAUNCHER Task Files Explorer (pengganti fungsional popup
# "All files in task").
#
# Rantai: preview platform -> ingress :81 -> 127.0.0.1:3000 -> explorer.py
#
# PRIORITAS PORT 3000: bila ada package.json (proyek Next.js), Next.js yang
# berhak atas port 3000 dan explorer BERDIRI DOWN (guard di bawah) — explorer
# tidak boleh merusak proyek web platform.
#
# Dipanggil dari tiga jalur (sama seperti watcher):
#   1. Boot container -> dev.sh v1.2 (hook /start.sh)
#   2. watcher.sh v1.1 -> auto-heal tiap 30 detik bila healthz gagal
#   3. Manual
#
# PERINTAH:
#   bash explorer.sh --ensure   # idempoten: hidup bila belum, no-op bila sudah
#   bash explorer.sh --status   # cek kesehatan + log tail
#   bash explorer.sh --stop     # matikan explorer
# ============================================================================
PROJECT="${STELLAR_PROJECT:-/home/z/my-project}"
ZDIR="$PROJECT/.zscripts"
PY="$ZDIR/explorer.py"
UI="$ZDIR/explorer-ui/index.html"
LOG="$ZDIR/explorer.log"
PIDFILE="$ZDIR/explorer.pid"
PORT=3000
HEALTH="http://127.0.0.1:${PORT}/healthz"

alive() { curl -fsS -m 2 "$HEALTH" >/dev/null 2>&1; }

case "$1" in
--status)
    echo "=== TASK FILES EXPLORER @ :$PORT ==="
    if alive; then
        echo "kesehatan: OK  ($HEALTH)"
        echo "api      : http://127.0.0.1:$PORT/api/files"
    else
        echo "kesehatan: MATI"
    fi
    echo "pid file : $(cat "$PIDFILE" 2>/dev/null || echo '-')"
    echo "--- explorer.log (10 terakhir) ---"
    tail -10 "$LOG" 2>/dev/null || echo "(kosong)"
    exit 0
    ;;
--stop)
    if [ -f "$PIDFILE" ]; then
        kill "$(cat "$PIDFILE")" 2>/dev/null \
            && echo "[explorer] dihentikan (pid $(cat "$PIDFILE"))"
        rm -f "$PIDFILE"
    fi
    pkill -f "$PY" 2>/dev/null
    exit 0
    ;;
--ensure | *)
    if alive; then exit 0; fi
    if [ -f "$PROJECT/package.json" ]; then
        echo "[explorer] package.json ada -> Next.js pemilik :$PORT, explorer stand-down" >&2
        exit 0
    fi
    if [ ! -f "$PY" ] || [ ! -f "$UI" ]; then
        echo "[explorer] file server/UI tidak lengkap ($PY / $UI)" >&2
        exit 1
    fi
    # port dipakai proses lain yang bukan explorer? jangan direbut
    if (exec 3<>/dev/tcp/127.0.0.1/$PORT) 2>/dev/null; then
        exec 3>&- 3<&-
        echo "[explorer] port $PORT dipakai proses lain (bukan explorer) — stand down" >&2
        exit 1
    fi
    echo "[$(date '+%F %T')] explorer.sh start (double-fork orphan)" >> "$LOG"
    ( setsid python3 "$PY" "$PORT" >> "$LOG" 2>&1 & )
    sleep 1
    if alive; then
        echo "[explorer] HIDUP di :$PORT (pid $(cat "$PIDFILE" 2>/dev/null))"
    else
        echo "[explorer] WARN: belum sehat setelah start — cek $LOG" >&2
    fi
    exit 0
    ;;
esac
