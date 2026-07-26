#!/usr/bin/env bash
# Deploy the football hub to igamingreviews.org/terrace/hub/
# Needs SFTP credentials from Hostinger hPanel (Files -> FTP Accounts).
# Usage: TERRACE_SFTP_USER=u123456 TERRACE_SFTP_PASS=secret bash deploy_terrace.sh
set -euo pipefail

HOST="${TERRACE_SFTP_HOST:-ftp.igamingreviews.org}"
USER="${TERRACE_SFTP_USER:?set TERRACE_SFTP_USER}"
PASS="${TERRACE_SFTP_PASS:?set TERRACE_SFTP_PASS}"
REMOTE_DIR="${TERRACE_REMOTE_DIR:-public_html/terrace/hub}"
SRC="/tmp/terrace-hub-pkg"

command -v sshpass >/dev/null || { echo "need sshpass installed"; exit 1; }

echo "Deploying $SRC -> $HOST:$REMOTE_DIR"
sshpass -p "$PASS" sftp -oStrictHostKeyChecking=accept-new "$USER@$HOST" <<SFTP
mkdir $REMOTE_DIR
mkdir $REMOTE_DIR/assets
cd $REMOTE_DIR
lcd $SRC
put index.html
put data.js
put README.md
put fetch_league.py
cd assets
lcd assets
put style.css
put app.js
SFTP

echo "Done. Verify: https://igamingreviews.org/terrace/hub/"
