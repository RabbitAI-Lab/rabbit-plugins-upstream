#!/usr/bin/env bash
# air_chart.sh — air-chart main entry
# Natural-language query -> OpenAQ station pick -> data cleaning -> SVG chart
#
# Usage:
#   air_chart.sh --city Beijing --param pm25 --period 7d
#   air_chart.sh --city Tokyo --city Seoul --param pm25 --period 7d     # multi-city compare
#   air_chart.sh --city Beijing --param pm25 --param pm10 --period 48h  # multi-parameter
#   air_chart.sh --city Delhi --param pm10 --snapshot                   # station snapshot
#   air_chart.sh --city Beijing --param pm25 --period 7d --demo         # demo data (no API key)
# Options: --city/-c --param/-p --period/-t --snapshot --theme --lang en|zh --out/-o --demo
# Language: auto-detected from system locale (zh -> Chinese), override with --lang.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=./openaq_client.sh
source "$SCRIPT_DIR/openaq_client.sh"

# ---------- 参数默认值 ----------
CITIES=(); PARAMS=("pm25"); PERIOD="7d"; SNAPSHOT=0; THEME="light"; OUT=""; DEMO=0
LANG_OPT=""

usage() { sed -n '2,15p' "${BASH_SOURCE[0]}"; }

while (( $# )); do
  case "$1" in
    -c|--city) CITIES+=("$2"); shift 2 ;;
    -p|--param) PARAMS+=("$2"); shift 2 ;;
    -t|--period) PERIOD="$2"; shift 2 ;;
    --snapshot) SNAPSHOT=1; shift ;;
    --theme) THEME="$2"; shift 2 ;;
    --lang) LANG_OPT="$2"; shift 2 ;;
    -o|--out) OUT="$2"; shift 2 ;;
    --demo) DEMO=1; shift ;;
    -h|--help) usage; exit 0 ;;
    *) printf '[air-chart] ERROR: 未知参数 %s\n' "$1" >&2; usage >&2; exit 1 ;;
  esac
done

# ---------- 语言 (默认按系统 locale 自动检测, --lang 覆盖) ----------
detect_lang() {
  local l="${LANG_OPT:-${LC_ALL:-${LC_MESSAGES:-${LANG:-}}}}"
  [[ "$l" == zh* ]] && printf 'zh' || printf 'en'
}
AIR_CHART_LANG="$(detect_lang)"
export AIR_CHART_LANG

# 文案表 (key: en/zh)
declare -A T_EN T_ZH
T_EN[err_no_city]="Please specify at least one city via --city."
T_ZH[err_no_city]="请至少通过 --city 指定一个城市。"
T_EN[err_too_many_cities]="Multi-city comparison supports at most 4 cities."
T_ZH[err_too_many_cities]="多城对比最多支持 4 个城市。"
T_EN[err_bad_param]='Unsupported parameter "%s" (choose from: %s).'
T_ZH[err_bad_param]='不支持的指标 "%s" (可选: %s)。'
T_EN[err_multi_param]="Multi-city comparison supports only one --param."
T_ZH[err_multi_param]="多城对比模式仅支持单指标, 请只传一个 --param。"
T_EN[err_bad_period]='Unsupported period "%s" (choose from: 24h 48h 7d 14d 30d).'
T_ZH[err_bad_period]='不支持的时间跨度 "%s" (可选: 24h 48h 7d 14d 30d)。'
T_EN[err_no_series]="Nothing to plot. Check the city/parameter/period, or use --demo to preview."
T_ZH[err_no_series]="没有任何序列可绘制。请检查城市名/指标/时间范围, 或使用 --demo 预览效果。"
T_EN[warn_no_active]="WARN: no active monitoring station within 25km of %s (no update in 24-72h)."
T_ZH[warn_no_active]="WARN: %s 附近 25km 内没有活性监测站点 (24-72h 内无数据更新)。"
T_EN[warn_no_sensor]="WARN: active stations of %s have no %s sensor data, skipped."
T_ZH[warn_no_sensor]="WARN: %s 的活性站点中暂无 %s 传感器数据, 已跳过。"
T_EN[warn_no_data]="WARN: no valid data points for %s %s in the selected period."
T_ZH[warn_no_data]="WARN: %s %s 在时间范围内无有效数据点。"
T_EN[warn_no_snapshot]="WARN: no active %s stations near %s for snapshot."
T_ZH[warn_no_snapshot]="WARN: %s 附近没有可用于快照的活性 %s 站点。"
T_EN[warn_no_latest]="WARN: latest data unavailable for all stations."
T_ZH[warn_no_latest]="WARN: 站点最新数据均不可用。"
T_EN[note_who_skipped]="NOTE: sensor units differ from the dictionary default; WHO guideline line skipped to avoid dimensional confusion."
T_ZH[note_who_skipped]="NOTE: 站点传感器单位与默认单位不一致, 已跳过 WHO 基准线以避免量纲误导。"
T_EN[demo_note]="demo mode (real API not called)"
T_ZH[demo_note]="演示数据模式 (未请求真实 API)"
T_EN[ref_grade]="(reference-grade)"
T_ZH[ref_grade]="(参考级)"
T_EN[summary]="Data summary:"
T_ZH[summary]="数据摘要:"
T_EN[chart_saved]="Chart saved:"
T_ZH[chart_saved]="图表已生成:"
T_EN[snapshot_saved]="Snapshot saved:"
T_ZH[snapshot_saved]="快照已生成:"
T_EN[station]="Station"
T_ZH[station]="站点"
T_EN[latest]="latest"
T_ZH[latest]="最新"
T_EN[title_compare]="%s comparison · last %s"
T_ZH[title_compare]="%s 走势对比 · 最近 %s"
T_EN[sub_compare]="Source: OpenAQ · multi-city same-parameter · station local time"
T_ZH[sub_compare]="数据来源 OpenAQ · 多城市同指标对比 · 站点当地时间"
T_EN[title_single]="%s %s trend · last %s"
T_ZH[title_single]="%s %s 趋势 · 最近 %s"
T_EN[sub_multi_param]="Source: OpenAQ · multi-parameter single city · station local time"
T_ZH[sub_multi_param]="数据来源 OpenAQ · 单城市多指标对比 · 站点当地时间"
T_EN[sub_single]="Source: OpenAQ · station local time (%s)"
T_ZH[sub_single]="数据来源 OpenAQ · 站点当地时间 (%s)"
T_EN[ylabel_multi]="Concentration (%s)"
T_ZH[ylabel_multi]="浓度 (%s)"
T_EN[title_snapshot]="%s %s real-time snapshot by station"
T_ZH[title_snapshot]="%s 各监测点 %s 实时快照"
T_EN[sub_snapshot]="Source: OpenAQ · %s · active stations within 25km"
T_ZH[sub_snapshot]="数据来源 OpenAQ · %s · 25km 半径内活性站点"
T_EN[demo_tag]=" (demo)"
T_ZH[demo_tag]=" (演示)"
T_EN[demo_mode_tag]=" · demo mode"
T_ZH[demo_mode_tag]=" · 演示模式"
T_EN[sub_snapshot_demo]="Source: OpenAQ · demo mode · active stations within 25km"
T_ZH[sub_snapshot_demo]="数据来源 OpenAQ · 演示模式 · 25km 半径内活性站点"

t() { # t <key> — 取当前语言文案
  if [[ "$AIR_CHART_LANG" == "zh" ]]; then printf '%s' "${T_ZH[$1]:-${T_EN[$1]}}"; else printf '%s' "${T_EN[$1]}"; fi
}

VALID_PARAMS="$(param_slugs)"
# 从 data/parameters.tsv 静态字典加载指标元数据 (列: 3名称 4单位 5WHO基准 6上限 7色 8深色色)
declare -A WHO_BASELINE PARAM_LABEL PARAM_UNITS PARAM_CAP PARAM_COLOR PARAM_COLOR_DARK
while IFS=$'\t' read -r slug pid pname punits pwho pcap pcolor pcolord; do
  [[ "$slug" == \#* || -z "$slug" ]] && continue
  WHO_BASELINE[$slug]="$pwho"; PARAM_LABEL[$slug]="$pname"; PARAM_UNITS[$slug]="$punits"
  PARAM_CAP[$slug]="$pcap"; PARAM_COLOR[$slug]="$pcolor"; PARAM_COLOR_DARK[$slug]="$pcolord"
done < "$PARAMS_TSV"

# 默认参数修正: --param 显式传入时去掉默认值
if (( ${#PARAMS[@]} > 1 )) && [[ "${PARAMS[0]}" == "pm25" ]]; then PARAMS=("${PARAMS[@]:1}"); fi
[[ ${#CITIES[@]} -eq 0 ]] && { printf '[air-chart] ERROR: %s\n' "$(t err_no_city)" >&2; exit 1; }
[[ ${#CITIES[@]} -gt 4 ]] && { printf '[air-chart] ERROR: %s\n' "$(t err_too_many_cities)" >&2; exit 1; }
for p in "${PARAMS[@]}"; do
  [[ " $VALID_PARAMS " == *" $p "* ]] || { printf '[air-chart] ERROR: '"$(t err_bad_param)"'\n' "$p" "$VALID_PARAMS" >&2; exit 1; }
done
if (( ${#CITIES[@]} > 1 && ${#PARAMS[@]} > 1 )); then
  printf '[air-chart] ERROR: %s\n' "$(t err_multi_param)" >&2; exit 1
fi

case "$PERIOD" in
  24h) GRAN="hours"; HOURS=24 ;;
  48h) GRAN="hours"; HOURS=48 ;;
  7d)  GRAN="days";  HOURS=$((7 * 24)) ;;
  14d) GRAN="days";  HOURS=$((14 * 24)) ;;
  30d) GRAN="days";  HOURS=$((30 * 24)) ;;
  *) printf '[air-chart] ERROR: '"$(t err_bad_period)"'\n' "$PERIOD" >&2; exit 1 ;;
esac

[[ -z "$OUT" ]] && OUT="./air-chart-$(date +%Y%m%d-%H%M%S).svg"

DATE_FROM="$(date -u -d "-$((HOURS + 6)) hours" +%Y-%m-%dT%H:%M:%SZ 2>/dev/null || date -u -v-"$((HOURS + 6))"H +%Y-%m-%dT%H:%M:%SZ)"
DATE_TO="$(date -u +%Y-%m-%dT%H:%M:%SZ)"

WORK="$(mktemp -d)"; trap 'rm -rf "$WORK"' EXIT

# ---------- 演示数据生成 ----------
demo_series() { # <city> <param> <gran> <n> -> 生成 label\tvalue 到 stdout
  local city="$1" param="$2" gran="$3" n="$4" seed
  seed=$(( $(printf '%s' "$city$param" | cksum | awk '{print $1}') % 1000 ))
  # 用城市时区生成当地时间标签
  local tz; tz="$(cut -f5 <<<"$GEO_LINE")"
  awk -v seed="$seed" -v n="$n" -v gran="$gran" -v base="$(date +%s)" -v step="$([[ "$gran" == hours ]] && echo 3600 || echo 86400)" -v tz="$tz" '
  BEGIN {
    amp = (gran == "hours") ? 8 : 20
    mid = (gran == "hours") ? 25 : 45
    for (i = n - 1; i >= 0; i--) {
      ts = base - i * step
      cmd = "TZ=" tz " date -d @" ts " \"+%m-%d" ((gran == "hours") ? " %H:00" : "") "\""
      cmd | getline l; close(cmd)
      x = n - 1 - i
      v = mid + amp * sin((x + seed % 24) / (gran == "hours" ? 3.8 : 2.2)) + amp * 0.35 * sin(x / 1.7 + seed)
      if (v < 0.5) v = 0.5
      printf "%s\t%.1f\n", l, v
    }
  }'
}

# ---------- 主流程 ----------
declare -a RENDER_SPECS=() CITY_NOTES=() SERIES_PARAMS=() SERIES_UNITS=()
FIRST_UNITS=""; FIRST_TZ=""; GLOBAL_MAX=""

fetch_city_series() { # <city> -> 为每个 param 生成 series 文件, 输出到 RENDER_SPECS
  local city="$1"
  GEO_LINE="$("$SCRIPT_DIR/geo_resolve.sh" "$city")" || exit $?
  local lat lon tz
  lat="$(cut -f3 <<<"$GEO_LINE")"; lon="$(cut -f4 <<<"$GEO_LINE")"; tz="$(cut -f5 <<<"$GEO_LINE")"
  local geo_name; geo_name="$(cut -f1 <<<"$GEO_LINE")"
  [[ -z "${FIRST_GEO_NAME:-}" ]] && FIRST_GEO_NAME="$geo_name"

  local locations
  locations="$(openaq_find_locations "$lat" "$lon" 25000)"
  local active
  active="$(openaq_filter_active "$locations" 24)"
  if [[ "$(jq '(.results // []) | length' <<<"$active")" == "0" ]]; then
    # 24h 无活性站点, 放宽到 72h 再试一次
    active="$(openaq_filter_active "$locations" 72)"
  fi
  if [[ "$(jq '(.results // []) | length' <<<"$active")" == "0" ]]; then
    printf '[air-chart] '"$(t warn_no_active)"'\n' "$city" >&2
    return 1
  fi

  for param in "${PARAMS[@]}"; do
    local picked
    picked="$(openaq_pick_sensor "$active" "$param")"
    if [[ -z "$picked" ]]; then
      printf '[air-chart] '"$(t warn_no_sensor)"'\n' "$city" "${PARAM_LABEL[$param]}" >&2
      continue
    fi
    local sensor_id units stz sname monitor
    sensor_id="$(cut -f1 <<<"$picked")"; units="$(cut -f2 <<<"$picked")"
    stz="$(cut -f3 <<<"$picked")"; sname="$(cut -f4 <<<"$picked")"; monitor="$(cut -f5 <<<"$picked")"
    [[ -z "$units" || "$units" == "null" ]] && units="${PARAM_UNITS[$param]}"
    [[ -z "$FIRST_UNITS" ]] && { FIRST_UNITS="$units"; FIRST_TZ="$stz"; }

    local raw clean
    raw="$(openaq_fetch_series "$sensor_id" "$GRAN" "$DATE_FROM" "$DATE_TO")"
    clean="$WORK/${geo_name}.${param}.tsv"
    awk -v gran="$GRAN" -v cap="${PARAM_CAP[$param]}" -v stats="$WORK/${geo_name}.${param}.stats" \
        -f "$SCRIPT_DIR/data_transform.awk" <<<"$raw" > "$clean"
    if [[ ! -s "$clean" ]]; then
      printf '[air-chart] '"$(t warn_no_data)"'\n' "$city" "${PARAM_LABEL[$param]}" >&2
      continue
    fi
    RENDER_SPECS+=("${geo_name} ${PARAM_LABEL[$param]}:${clean}")
    SERIES_PARAMS+=("$param"); SERIES_UNITS+=("$units")
    local st_min st_max st_avg st_cnt
    st_cnt="$(awk -F'\t' '$1=="count"{print $2}' "$WORK/${geo_name}.${param}.stats")"
    st_min="$(awk -F'\t' '$1=="min"{print $2}' "$WORK/${geo_name}.${param}.stats")"
    st_max="$(awk -F'\t' '$1=="max"{print $2}' "$WORK/${geo_name}.${param}.stats")"
    st_avg="$(awk -F'\t' '$1=="avg"{print $2}' "$WORK/${geo_name}.${param}.stats")"
    if [[ -n "$st_max" && ( -z "$GLOBAL_MAX" || "$(awk -v a="$GLOBAL_MAX" -v b="$st_max" 'BEGIN{print (b>a)?1:0}')" == "1" ) ]]; then GLOBAL_MAX="$st_max"; fi
    CITY_NOTES+=("  - ${geo_name} · ${PARAM_LABEL[$param]} · $(t station): ${sname}$( [[ "$monitor" == "true" ]] && echo " $(t ref_grade)") · n=${st_cnt} min=${st_min} max=${st_max} avg=$(printf '%.1f' "$st_avg") ${units}")
  done
}

fetch_city_snapshot() { # <city> <param> -> 渲染柱状图所需 items
  local city="$1" param="$2"
  GEO_LINE="$("$SCRIPT_DIR/geo_resolve.sh" "$city")" || exit $?
  local lat lon tz geo_name
  lat="$(cut -f3 <<<"$GEO_LINE")"; lon="$(cut -f4 <<<"$GEO_LINE")"; tz="$(cut -f5 <<<"$GEO_LINE")"
  geo_name="$(cut -f1 <<<"$GEO_LINE")"

  local locations active
  locations="$(openaq_find_locations "$lat" "$lon" 25000)"
  active="$(openaq_filter_active "$locations" 24)"
  [[ "$(jq '(.results // []) | length' <<<"$active")" == "0" ]] && active="$(openaq_filter_active "$locations" 72)"
  local sensors
  sensors="$(openaq_pick_all_sensors "$active" "$param" | head -6)"
  if [[ -z "$sensors" ]]; then
    printf '[air-chart] '"$(t warn_no_snapshot)"'\n' "$city" "${PARAM_LABEL[$param]}" >&2
    return 1
  fi
  local items=() units=""
  while IFS=$'\t' read -r sensor_id u s_tz s_name monitor; do
    [[ -z "$sensor_id" ]] && continue
    local latest v utc_ts
    latest="$(openaq_fetch_latest "$sensor_id")"
    [[ -z "$latest" ]] && continue
    v="$(cut -f3 <<<"$latest")"; utc_ts="$(cut -f1 <<<"$latest")"
    [[ -z "$units" ]] && units="$u"
    items+=("${s_name}:${v}")
    CITY_NOTES+=("  - ${s_name}$( [[ "$monitor" == "true" ]] && echo " $(t ref_grade)") · $(t latest): ${v} ${u} @ ${utc_ts} UTC")
  done <<<"$sensors"
  [[ ${#items[@]} -eq 0 ]] && { printf '[air-chart] %s\n' "$(t warn_no_latest)" >&2; return 1; }
  [[ -z "$units" || "$units" == "null" ]] && units="${PARAM_UNITS[$param]}"
  FIRST_UNITS="$units"
  local who="${WHO_BASELINE[$param]}"
  # WHO 线仅在与字典默认单位一致时叠加, 防止量纲误导; 达标绿/超标红
  local who_args=()
  if [[ "$units" == "${PARAM_UNITS[$param]}" ]]; then
    local snap_max whoc
    snap_max="$(printf '%s\n' "${items[@]#*:}" | sort -g | tail -1)"
    whoc="#EF4444"
    [[ "$(awk -v a="${snap_max:-0}" -v b="$who" 'BEGIN{print (b>a)?1:0}')" == "1" ]] && whoc="#10B981"
    who_args=(--who "$who" --who-label "WHO 24h: $who ${PARAM_UNITS[$param]}" --who-color "$whoc")
  fi
  local snap_color="${PARAM_COLOR[$param]}"; [[ "$THEME" == "dark" ]] && snap_color="${PARAM_COLOR_DARK[$param]}"
  "$SCRIPT_DIR/render_draw.sh" bar \
    --title "$(printf "$(t title_snapshot)" "$geo_name" "${PARAM_LABEL[$param]}")" \
    --subtitle "$(printf "$(t sub_snapshot)" "$(TZ="$tz" date '+%Y-%m-%d %H:%M %Z')")" \
    --ylabel "$units" \
    --items "${items[@]}" --colors "$snap_color" \
    ${who_args[@]+"${who_args[@]}"} \
    --theme "$THEME" --width 960 --height $((120 + 60 * ${#items[@]})) \
    --out "$OUT"
}

# ---------- 执行 ----------
if (( ! DEMO )); then
  openaq_require_key
fi

if (( SNAPSHOT )); then
  snap_param="${PARAMS[0]}"
  snap_color="${PARAM_COLOR[$snap_param]}"; [[ "$THEME" == "dark" ]] && snap_color="${PARAM_COLOR_DARK[$snap_param]}"
  snap_units="${PARAM_UNITS[$snap_param]}"
  snap_who="${WHO_BASELINE[$snap_param]}"
  if (( DEMO )); then
    # 演示快照
    demo_city="${CITIES[0]}"
    if [[ "$AIR_CHART_LANG" == "zh" ]]; then
      items=("朝阳公园:32.4" "奥体中心:45.1" "万寿西宫:51.8" "通州:58.2" "昌平:26.9" "大兴:63.5")
    else
      items=("Chaoyang Park:32.4" "Olympic Center:45.1" "Wanshou Xigong:51.8" "Tongzhou:58.2" "Changping:26.9" "Daxing:63.5")
    fi
    FIRST_UNITS="µg/m³"
    CITY_NOTES=("  - $(t demo_note)")
    snap_max=63.5
    [[ "$(awk -v a="$snap_max" -v b="$snap_who" 'BEGIN{print (b>a)?1:0}')" == "1" ]] && snap_whoc="#10B981" || snap_whoc="#EF4444"
    "$SCRIPT_DIR/render_draw.sh" bar \
      --title "$(printf "$(t title_snapshot)" "$demo_city" "${PARAM_LABEL[$snap_param]}")$(t demo_tag)" \
      --subtitle "$(t sub_snapshot_demo)" \
      --ylabel "$snap_units" --items "${items[@]}" --colors "$snap_color" \
      --who "$snap_who" --who-label "WHO 24h: $snap_who $snap_units" --who-color "$snap_whoc" --theme "$THEME" \
      --width 960 --height 480 --out "$OUT"
  else
    fetch_city_snapshot "${CITIES[0]}" "${PARAMS[0]}"
  fi
  printf '\n[air-chart] %s %s\n%s\n' "$(t snapshot_saved)" "$OUT" "${CITY_NOTES[*]}"
  exit 0
fi

for city in "${CITIES[@]}"; do
  if (( DEMO )); then
    GEO_LINE="$("$SCRIPT_DIR/geo_resolve.sh" "$city")" || exit $?
    geo_name="$(cut -f1 <<<"$GEO_LINE")"
    [[ -z "${FIRST_GEO_NAME:-}" ]] && FIRST_GEO_NAME="$geo_name"
    for param in "${PARAMS[@]}"; do
      clean="$WORK/${geo_name}.${param}.tsv"
      demo_series "$city" "$param" "$GRAN" "$((HOURS / ($( [[ "$GRAN" == hours ]] && echo 1 || echo 24 ))))" > "$clean"
      FIRST_UNITS="${PARAM_UNITS[$param]}"; FIRST_TZ="$(cut -f5 <<<"$GEO_LINE")"
      RENDER_SPECS+=("${geo_name} ${PARAM_LABEL[$param]}:${clean}")
      SERIES_PARAMS+=("$param"); SERIES_UNITS+=("${PARAM_UNITS[$param]}")
      dmax="$(awk -F'\t' '$2!=""{if($2>m)m=$2}END{print m+0}' "$clean")"
      if [[ -z "$GLOBAL_MAX" || "$(awk -v a="$GLOBAL_MAX" -v b="$dmax" 'BEGIN{print (b>a)?1:0}')" == "1" ]]; then GLOBAL_MAX="$dmax"; fi
    done
    CITY_NOTES+=("  - ${geo_name}: $(t demo_note)")
  else
    fetch_city_series "$city" || true
  fi
done

if (( ${#RENDER_SPECS[@]} == 0 )); then
  printf '[air-chart] ERROR: %s\n' "$(t err_no_series)" >&2
  exit 5
fi

param0="${PARAMS[0]}"
city_count=${#CITIES[@]}
# 仅拼接用户请求的指标名
param_labels=""
for p in "${PARAMS[@]}"; do param_labels+="${param_labels:+ / }${PARAM_LABEL[$p]}"; done
ylabel="${PARAM_LABEL[$param0]} (${FIRST_UNITS})"
if (( city_count > 1 )); then
  title="$(printf "$(t title_compare)" "${PARAM_LABEL[$param0]}" "$PERIOD")"
  subtitle="$(t sub_compare)"
else
  gname="${FIRST_GEO_NAME:-${CITIES[0]}}"
  title="$(printf "$(t title_single)" "$gname" "$param_labels" "$PERIOD")"
  if (( ${#PARAMS[@]} > 1 )); then
    subtitle="$(t sub_multi_param)"
    ylabel="$(printf "$(t ylabel_multi)" "$FIRST_UNITS")"
  else
    subtitle="$(printf "$(t sub_single)" "$FIRST_TZ")"
  fi
fi

# WHO 基准线: 仅当所有序列单位与字典默认单位一致时叠加 (防止 ppm vs µg/m³ 量纲误导)
who_args=()
if [[ -n "${WHO_BASELINE[$param0]:-}" ]]; then
  units_match=1
  for i in "${!SERIES_PARAMS[@]}"; do
    [[ "${SERIES_UNITS[$i]}" == "${PARAM_UNITS[${SERIES_PARAMS[$i]}]}" ]] || units_match=0
  done
  if (( units_match )); then
    whoc="#EF4444"
    [[ -n "$GLOBAL_MAX" && "$(awk -v a="$GLOBAL_MAX" -v b="${WHO_BASELINE[$param0]}" 'BEGIN{print (b>a)?1:0}')" == "1" ]] && whoc="#10B981"
    who_args=(--who "${WHO_BASELINE[$param0]}" --who-label "WHO 24h: ${WHO_BASELINE[$param0]} ${PARAM_UNITS[$param0]}" --who-color "$whoc")
  else
    printf '[air-chart] NOTE: %s\n' "$(t note_who_skipped)" >&2
  fi
fi

# 序列配色: 单城用指标专属色板 (对齐 openaq-explorer), 多城用城市对比色板 (默认)
colors_opt=()
if (( city_count == 1 )); then
  colors_csv=""
  for p in "${SERIES_PARAMS[@]}"; do
    c="${PARAM_COLOR[$p]}"; [[ "$THEME" == "dark" ]] && c="${PARAM_COLOR_DARK[$p]}"
    colors_csv+="${colors_csv:+,}$c"
  done
  colors_opt=(--colors "$colors_csv")
fi

"$SCRIPT_DIR/render_draw.sh" line \
  --title "$title" --subtitle "$subtitle" \
  --ylabel "$ylabel" \
  --series "${RENDER_SPECS[@]}" \
  ${colors_opt[@]+"${colors_opt[@]}"} \
  ${who_args[@]+"${who_args[@]}"} \
  --theme "$THEME" --out "$OUT"

printf '\n[air-chart] %s %s\n' "$(t chart_saved)" "$OUT"
if (( ${#CITY_NOTES[@]} )); then
  printf '[air-chart] %s\n%s\n' "$(t summary)" "${CITY_NOTES[*]}"
fi
