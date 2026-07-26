#!/data/data/com.termux/files/usr/bin/bash

while true
do
  clear

  echo "===== $(date) ====="

  my-skill trade BTC
  my-skill trade ETH
  my-skill trade SOL

  echo ""
  my-skill status

  sleep 30
done
