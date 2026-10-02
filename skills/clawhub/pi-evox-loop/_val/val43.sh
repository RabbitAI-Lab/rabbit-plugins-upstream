#!/usr/bin/env bash
# val43.sh — #43 受控验证（bash 顶层驱动）
# 沙箱约束：node→node 子进程 EBUSY ⇒ 所有 CLI 调用由 bash 直接发起（bash→node 正常），
# 规避嵌套 spawn。断言全部在 bash 层完成。库隔离于 _val/run43，不触碰真实 ~/.evomap/assets。
set -u

REPO="$(cd "$(dirname "$0")/.." && pwd)"
CODE="$REPO/code"
RUN="$REPO/_val/run43"
PASS=0; FAIL=0; FAILED=""

chk(){ # id desc cond(1/0) detail
  if [ "$3" = "1" ]; then echo "✅ $1 $2${4:+  — $4}"; PASS=$((PASS+1));
  else echo "❌ $1 $2${4:+  — $4}"; FAIL=$((FAIL+1)); FAILED="$FAILED
  - $1 $2"; fi
}
cnt(){ if [ -f "$1" ]; then wc -l < "$1" | tr -d ' '; else echo 0; fi; }
pick(){ printf '%s\n' "$1" | grep -oE '\[#[0-9]+\|[^]]+\]' | sed -E 's/\[#[0-9]+\|([^]]+)\]/\1/' | paste -sd, -; }
has(){ case ",$2," in *",$1,"*) echo 1;; *) echo 0;; esac; }
first_is(){ if [ "$(printf '%s' "$2" | cut -d, -f1)" = "$1" ]; then echo 1; else echo 0; fi; }

recall(){ # store query hitsdir
  EVO_STORE_DIR="$1" EVOX_QUERY="$2" EVOX_TOPN=5 EVOX_HITS_DIR="$3" \
    node "$CODE/evolver-recall.mjs" 2>&1
}

echo "═══════════════ val43 — #43 受控验证（LLM-free · bash 驱动）═══════════════"
node "$REPO/_val/seed43.mjs" || { echo "播种失败"; exit 2; }
echo

echo "── A. P0③ 引导式沉淀（light-cli draft）──"
AOUT=$(EVO_STORE_DIR="$RUN/storeA" node "$CODE/light-cli.mjs" draft \
  --error "UnicodeDecodeError: 'utf-8' codec can't decode byte 0xd6 in position 0: invalid start byte (events.jsonl)" \
  --tool read --context "sum events.jsonl" --strategy "FIX: read events.jsonl with encoding='gbk'" --commit 2>&1)
GA=$(cnt "$RUN/storeA/genes.jsonl")
chk A4 "draft --commit 落库 1 条引导草稿" "$([ "$GA" = "1" ] && echo 1 || echo 0)" "genes=$GA"
chk A5 '草稿 anti_patterns = 单 token 字面量 ["utf-8"]（方案A 词汇对齐）' "$(grep -q '"anti_patterns":\["utf-8"\]' "$RUN/storeA/genes.jsonl" 2>/dev/null && echo 1 || echo 0)"
chk A5b "kebab 负经验标签落 summary（人读，不参与匹配）" "$(grep -q 'assume-default-utf8' "$RUN/storeA/genes.jsonl" 2>/dev/null && echo 1 || echo 0)"
chk A6 "草稿 source=light-manual-guided" "$(grep -q 'light-manual-guided' "$RUN/storeA/genes.jsonl" 2>/dev/null && echo 1 || echo 0)"
chk A7 "草稿台账态=quarantined（待审）" "$(grep -q 'quarantined' "$RUN/storeA/review.jsonl" 2>/dev/null && echo 1 || echo 0)"
chk A8 "未补 FIX 的占位符草稿不落库" "$([ "$(EVO_STORE_DIR="$RUN/storeA2" node "$CODE/light-cli.mjs" draft --error "UnicodeDecodeError: bad" --commit >/dev/null 2>&1; cnt "$RUN/storeA2/genes.jsonl")" = "0" ] && echo 1 || echo 0)"
node "$REPO/_val/e43.mjs" "$RUN" >/dev/null 2>&1
J=$(pick "$(recall "$RUN/storeJ" "gbk utf-8 encoding read" "$RUN/hitsD")")
chk A9 "端到端：引导草稿的 anti token 真使冲突基因被剔除" "$([ "$(has gene_e2e_guided "$J")" = "1" ] && [ "$(has gene_e2e_conflict "$J")" = "0" ] && echo 1 || echo 0)" "$J"
# A1-A3：占位符守卫与 anti_patterns/source 透传（distillManual 直连）
node "$REPO/_val/a43.mjs" > "$RUN/_v43a.txt" 2>&1
chk A1 "占位符 strategy 被拒绝（守卫）" "$(grep -q '^A1 1' "$RUN/_v43a.txt" && echo 1 || echo 0)" "$(head -1 "$RUN/_v43a.txt")"
chk A2 "anti_patterns 落库" "$(grep -q '^A2 1' "$RUN/_v43a.txt" && echo 1 || echo 0)"
chk A3 "generation_meta.source 透传" "$(grep -q '^A3 1' "$RUN/_v43a.txt" && echo 1 || echo 0)"

echo
echo "── B. P1④ 负载均衡偏置 ──"
B=$(recall "$RUN/storeB" "gbk file read error unicode decode" "$RUN/hitsB")
IB=$(pick "$B")
chk B1 "scale-0：GBK 对靶基因排首位" "$(first_is gene_test_gbk "$IB")" "$IB"
chk B2 "scale-0：JSON 对靶基因在列（未误删）" "$(has gene_test_json "$IB")"
chk B3 "scale-0：不对靶基因被排除" "$([ "$(has gene_test_file "$IB")" = "0" ] && echo 1 || echo 0)"

C0=$(pick "$(recall "$RUN/storeC" "alpha bravo" "$RUN/hitsC0")")
chk B4 "scale-0：等分基因按库序（hot 在前，偏置=0）" "$([ "$(first_is gene_test_hot "$C0")" = "1" ] && [ "$(has gene_test_cold "$C0")" = "1" ] && echo 1 || echo 0)" "$C0"
C1=$(pick "$(recall "$RUN/storeC" "alpha bravo" "$RUN/hitsC1")")
chk B5 "P1④ 偏置生效：热门下压/冷门上抬（顺序翻转）" "$([ "$(first_is gene_test_cold "$C1")" = "1" ] && [ "$(has gene_test_hot "$C1")" = "1" ] && echo 1 || echo 0)" "$C1"

echo
echo "── C. P1⑤ 注入冲突守卫 ──"
D=$(pick "$(recall "$RUN/storeD" "gbk utf-8 encoding read" "$RUN/hitsD")")
chk C1 "真冲突（单 token anti_pattern）剔除低分基因" "$([ "$(has gene_test_conf_p "$D")" = "1" ] && [ "$(has gene_test_conf_q "$D")" = "0" ] && echo 1 || echo 0)" "$D"
E=$(pick "$(recall "$RUN/storeE" "gbk utf-8 encoding read" "$RUN/hitsD")")
chk C2 "单基因场景无副作用（不被误删）" "$(has gene_test_conf_p "$E")" "$E"
F=$(pick "$(recall "$RUN/storeF" "gbk utf-8 encoding read" "$RUN/hitsD")")
chk C3 "多词/复合 anti_patterns 不命中（保守·宁缺毋滥；亦为已知限制）" "$([ "$(has gene_test_blind_p "$F")" = "1" ] && [ "$(has gene_test_blind_q "$F")" = "1" ] && echo 1 || echo 0)" "$F"
echo "说明（方案A 词汇对齐已处置，2026-09-23）：geneConflicts 做「anti_pattern 整串 ∈ 对方 token 集」"
echo "    成员判断 ⇒ 只有**单 token** 会触发。已通过词汇对齐解决：引导式沉淀改写入单 token 字面量"
echo "    （A5/A9 验证），kebab 标签转入 summary 供人读。**匹配器本身保持不变**；token 子集/阈值收紧"
echo "    仍推迟（门槛：≥5 条带 anti_patterns 且 ≥1 例真实冲突），详见分析文档 §五。"

echo
echo "── D. 注入与质量契约 ──"
G=$(pick "$(recall "$RUN/storeG" "gbk read encoding" "$RUN/hitsD")")
chk D1 "叙述型 strategy 被召回守卫拦截（§20）" "$([ "$(has gene_test_narr "$G")" = "0" ] && echo 1 || echo 0)" "$G"
H=$(pick "$(recall "$RUN/storeH" "gbk read encoding" "$RUN/hitsD")")
chk D2 "未审核基因不注入（审核门生效）" "$([ "$(has gene_test_gbk "$H")" = "0" ] && echo 1 || echo 0)" "$H"
chk D3 "loadApprovedStrategy 过滤契约在源码确认" "$(grep -q 'function loadApprovedStrategy' "$CODE/pi_evolve.mjs" && grep -q 'isRepairLike(text)' "$CODE/pi_evolve.mjs" && grep -q 'approved\.has(aid)' "$CODE/pi_evolve.mjs" && echo 1 || echo 0)"

echo
echo "── E. 审核语义 last-write-wins（补齐三处遗漏读取侧）──"
D4=$(EVO_STORE_DIR="$RUN/storeI" node "$REPO/_val/d43.mjs" 2>&1)
chk D4 "store.approvedAssetIds：approved→quarantine 后可注入集合剔除该资产（行为）" "$(printf '%s' "$D4" | grep -q '^D4 1' && echo 1 || echo 0)" "$D4"
chk D5 "pi_evolve.loadApprovedStrategy 已改 last-write-wins（静态契约）" "$(grep -q 'for (const \[assetId, state\] of latestState)' "$CODE/pi_evolve.mjs" && echo 1 || echo 0)"
chk D6 "metrics_collect 改按 last-write-wins 计数（静态契约）" "$(grep -q 'countLatest' "$CODE/metrics_collect.mjs" && ! grep -q 'countState(' "$CODE/metrics_collect.mjs" && echo 1 || echo 0)"

echo
echo "── F. P3 遥测（按 agent 观测双宿主注入）──"
EVO_STORE_DIR="$RUN/storeB" EVOX_QUERY="gbk read" EVOX_TOPN=5 EVOX_HITS_DIR="$RUN/hitsB" node "$CODE/evolver-recall.mjs" --agent openclaw >/dev/null 2>&1
TEL=$(tail -1 "$RUN/hitsB/recall_calls.jsonl")
chk D7 "recall_calls 含 agent=openclaw 且 injected>0" "$(printf '%s' "$TEL" | grep -q '"agent":"openclaw"' && printf '%s' "$TEL" | grep -qE '"injected":[1-9]' && echo 1 || echo 0)" "$TEL"
EVO_STORE_DIR="$RUN/storeB" EVOX_QUERY="gbk read" EVOX_HITS_DIR="$RUN/hitsB" node "$CODE/evolver-recall.mjs" >/dev/null 2>&1
TEL2=$(tail -1 "$RUN/hitsB/recall_calls.jsonl")
chk D8 "未传 --agent 记为 unknown（向后兼容）" "$(printf '%s' "$TEL2" | grep -q '"agent":"unknown"' && echo 1 || echo 0)" "$TEL2"

echo
echo "═══════════════════ 汇总 ═══════════════════"
echo "PASS=$PASS  FAIL=$FAIL"
[ "$FAIL" != "0" ] && echo "未通过项：$FAILED"
echo "临时库目录：$RUN（可安全删除）"
exit $([ "$FAIL" = "0" ] && echo 0 || echo 1)
