#!/usr/bin/env bash
# Reverse tunnel: Mac -> server. The server reaches this Mac at 127.0.0.1:<REVERSE_PORT>.
# Required env: REMOTE_HOST (server address). Optional: REMOTE_USER (default ubuntu), REVERSE_PORT (default 2299).
: "${REMOTE_USER:=ubuntu}"
: "${REVERSE_PORT:=2299}"
: "${REMOTE_HOST:?set REMOTE_HOST to your server address}"
S="$REMOTE_USER@$REMOTE_HOST"
LOG="${BRIDGE_DIR:-$HOME/hermes-mac-bridge}/tunnel.log"
while true; do
  echo "[$(date '+%F %T')] starting tunnel -> $S" >> "$LOG"
  ssh -N \
    -o ExitOnForwardFailure=yes \
    -o ServerAliveInterval=30 \
    -o ServerAliveCountMax=3 \
    -o ConnectTimeout=15 \
    -o StrictHostKeyChecking=accept-new \
    -o BatchMode=yes \
    -R "$REVERSE_PORT:127.0.0.1:22" \
    "$S" >>"$LOG" 2>&1
  echo "[$(date '+%F %T')] tunnel exited (rc=$?), retry in 5s" >> "$LOG"
  sleep 5
done
