#!/bin/bash
# step5: PPSSPP 优化：拷贝 PSP ROM 到应用可读目录 + ppsspp.ini（拉伸满屏/关虚拟键）+ PSP metadata launch 行（幂等）
source "$(dirname "$0")/kpa_env.sh"
require_device

GOLD="$KPA_SKILL_DIR/assets/golden"
PPS_FILES="$INT/Android/data/$PPS_PKG/files"

# 5.1 ppsspp.ini（含 DisplayStretch 满屏、ShowTouchControls=False）
if sh "test -f $PPS_FILES/PSP/SYSTEM/ppsspp.ini && grep -q 'DisplayStretch' $PPS_FILES/PSP/SYSTEM/ppsspp.ini"; then
  echo "SKIP  ppsspp.ini 已是优化配置"
else
  sh "mkdir -p $PPS_FILES/PSP/SYSTEM"
  bak "$PPS_FILES/PSP/SYSTEM/ppsspp.ini" .bakKPA3
  "$ADB" push "$GOLD/ppsspp.ini.txt" "$PPS_FILES/PSP/SYSTEM/ppsspp.ini" || die "ppsspp.ini 推送失败"
  echo "OK    ppsspp.ini 已部署（满屏拉伸 + 关闭虚拟键）"
fi

# 5.2 PSP ROM 拷贝（TF 卡 ROM 与 PPSSPP 目录不互通，是 Android 分区存储限制，必须双份）
if sh "test -f $TF/Roms/PSP/metadata.pegasus.txt" | grep -q ""; then :; fi
sh "ls $TF/Roms/PSP/ 2>/dev/null | grep -iE '\\.(iso|cso|pbp)$'" > /tmp/kpa_psp_roms.txt
n=$(wc -l < /tmp/kpa_psp_roms.txt | tr -d ' ')
if [ "$n" = "0" ]; then
  echo "SKIP  TF 卡没有 PSP ROM"
else
  copied=0
  while IFS= read -r rom; do
    [ -z "$rom" ] && continue
    if ! sh "test -f '$PPS_FILES/$rom'"; then
      echo "COPY  $rom（大文件，请耐心）"
      "$ADB" pull "$TF/Roms/PSP/$rom" "/tmp/kpa_psp_tmp" >/dev/null 2>&1 && \
      "$ADB" push "/tmp/kpa_psp_tmp" "$PPS_FILES/$rom" >/dev/null && \
      sh "chmod 666 '$PPS_FILES/$rom'"
      rm -f /tmp/kpa_psp_tmp
      copied=$((copied+1))
    fi
  done < /tmp/kpa_psp_roms.txt
  echo "OK    PSP ROM 双份部署完成（本次新拷 $copied 个；双份是必须的，勿删除）"
fi
rm -f /tmp/kpa_psp_roms.txt

# 5.3 PSP metadata launch 行（逐游戏指向 PPSSPP 拷贝路径）
cat > /tmp/kpa_step5_device.sh <<'EOS'
#!/system/bin/sh
TF="${1:-/storage/6AF3-384F}"
m="$TF/Roms/PSP/metadata.pegasus.txt"
files="/storage/emulated/0/Android/data/org.ppsspp.ppsspp/files"
[ -f "$m" ] || exit 0
grep -q '^launch:' "$m" && exit 0
cp "$m" "$m.bakKPA3"
awk -v files="$files" -v tf="$TF" '
  /^file: / { fname=$2 }
  {
    if ($1=="file:" && fname!="") {
      if (system("test -f \"" files "/" fname "\"")==0)
        print "launch: am start --user 0 -a android.intent.action.VIEW -d \"file://" files "/" fname "\" -n org.ppsspp.ppsspp/.PpssppActivity";
      else
        print "launch: am start --user 0 -a android.intent.action.VIEW -d \"file://" tf "/Roms/PSP/" fname "\" -n org.ppsspp.ppsspp/.PpssppActivity";
      fname=""
      next
    }
    if ($1=="launch:") next
    print
  }' "$m.bakKPA3" > "$m.tmp" && mv "$m.tmp" "$m"
echo "RESULT psp_launch_added=1"
EOS
"$ADB" push /tmp/kpa_step5_device.sh /sdcard/kpa_step5_device.sh >/dev/null
sh "sh /sdcard/kpa_step5_device.sh $TF"
sh "rm -f /sdcard/kpa_step5_device.sh" >/dev/null
rm -f /tmp/kpa_step5_device.sh
echo "step5 done"
