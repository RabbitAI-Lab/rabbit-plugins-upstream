#!/bin/bash
# 1-kommando deploy: byg → genstart → verificér
# Brug: bash deploy.sh <service-navn> [arbejdsmappe]
SVC="${1:?Service-navn mangler}"
DIR="${2:-/home/openclaw/.openclaw/workspace/$SVC}"
echo "1) Byg/forbered"
cd "$DIR" || exit 1
# TODO: din build-kommando (pip install, npm build, etc.)
echo "2) Genstart service"
if systemctl list-units --type=service 2>/dev/null | grep -q "$SVC"; then
  sudo systemctl restart "$SVC" && echo "  systemd: genstartet"
else
  pkill -f "$SVC" 2>/dev/null; sleep 2
  nohup python3 "$DIR/server.py" >/tmp/$SVC.log 2>&1 &
  echo "  nohup: genstartet (pid $!)"
fi
sleep 3
echo "3) Verificér"
curl -s --max-time 5 http://localhost:8791/health 2>/dev/null | head -c 150 || echo "  (ingen /health — tjek log)"
echo
echo "4) Log: tail /tmp/$SVC.log"
