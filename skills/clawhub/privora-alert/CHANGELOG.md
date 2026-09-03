# Changelog

Hand-written. The top entry below IS the changelog `publish.sh` reads and
sends to ClawHub (`read_top_changelog_entry` in `publish.sh` takes everything
between the first and second `## ` heading) — there is no heuristic
git-diff-based generator here, unlike `agent-skill/publish.sh`. Add a new
`## vX.Y.Z · YYYY-MM-DD` entry at the top for every release; never edit an
already-published entry.

## v1.0.4 · 2026-08-31

Packaging-narrowing fix (#1037, #1038) — no change to the 11-step flow, the
20-skill set, or any other documented behavior.

- **Stopped shipping `lg_agent_list.sh`** (#1037). This package's documented
  flow never calls it (grep-verified against SKILL.md); shipping it gave a
  `realtime-alerting` token unfiltered discovery of every skill visible to it
  — not just this package's 20 — which ClawScan flagged as SDI-1/SDI-2 and
  rated the published `1.0.3` package `DO_NOT_INSTALL` (score 66 / HIGH).
- **`scripts/lg_agent_exec.sh` now ships with a generated `allowed-skills.txt`**
  derived at packaging time from the `realtime-alerting` preset (18 scopes →
  20 skill ids, `lib/skill-catalog.js`'s new `resolvePresetSkillIds`) — the
  shared wrapper refuses any skill id outside that set. This is a
  **packaging-honesty control, not a security control**: it is client-side
  and trivially bypassable (edit/delete the file, or call
  `POST /agent/skills/execute` directly). The actual, non-bypassable boundary
  remains server-side scope enforcement, unaffected by this file's presence
  or contents. One canonical copy of `lg_agent_exec.sh` still serves both
  `privora-alert` and `privora-cn-quant` (no forked script) — `privora-cn-quant`
  ships no allowlist file, so its copy is unaffected and behaves exactly as
  before.
- **Republish also picks up two shared-script fixes this package has not
  shipped since 2026-08-11** (#1038): the Windows/MSYS2 non-ASCII payload
  corruption fix (#920, `784a1ee8`) and the approval-reason repair + curl-trap
  doc cleanup (#927, `92c55ce0`). Non-ASCII payloads (Chinese
  `messageTemplate` / channel names / thresholds) are this package's normal
  path, not an edge case, so this closes a real corruption window for
  Windows users following the documented flow.

Does not claim any change to the ClawScan rating — that depends on an actual
post-publish re-scan (TP4 should reduce given the wrapper's own scope, but is
not guaranteed to clear, since the shipped script source remains generically
capable code).

## v1.0.3 · 2026-08-11

Keep 股价预警 in the title / DISPLAY_NAME, not just keywords (fast-follow to
1.0.2). 股价预警 is the one term browser + anonymous-probe testing confirmed
this package already ranks #1-and-unique for — a proven, current win — whereas
黄金 / 基金 are SEO-supported strategic bets still unproven on this package's
own side until the listing ranks. Demoting a confirmed winner out of the
highest-weight field (the ClawHub-rendered name) to chase unproven terms is
asymmetric; the title holds multiple terms (the umbrella lists five asset
classes), so 黄金 / 基金 lead for new reach while 股价预警 holds the existing
win. No skill behavior or other metadata changed.

## v1.0.2 · 2026-08-11

Positioning + discoverability reweight (LM review). No skill behavior changed.

- **Primary framing changed from "实时告警" to "实时监控"** — continuous
  threshold-watching is the product, webhook/飞书/微信 notification is the
  mechanism under it, matching what `metric_alert_poll` (process 3196)
  actually does (§6). "监控" is also the dominant search framing in this
  category (competitor products use "XX监控" naming) and the umbrella
  package already ranks #1 for it; this package previously diluted the
  same query across two compound phrases instead of leading with the
  bare term.
- 黄金 leads (黄金实时监控 / 黄金监控) — backed by a real anonymous-readable,
  same-day-fresh dashboard ("SGE 黄金白银市场"), not just a ranking bet.
- 基金 second (基金净值监控) — **deliberately without "实时"**: no
  anonymous-readable fund dashboard exists today and anonymous fund
  samples are stale; the monitoring capability is real, the freshness
  claim is not yet demonstrable to a cold visitor.
- `股价预警` kept (not demoted with bare `A股`) — confirmed #1-and-only
  ranking for this exact package; A股 as a bare market tag stays capped
  and last, unrelated ranking profile.
- §0 now bridges "监控" (search term) to "指标告警" (the in-product page
  name, `alertsPage.title` in `locales/zh-CN.json`) so a converted user
  isn't confused on arrival.

## v1.0.1 · 2026-08-11

Discoverability-only release — no skill behavior changed. Reworked the ClawHub
listing metadata (title / description / keywords / display name) so the package
surfaces for the natural-language phrases a user actually types for this
scenario. Keywords went from 10 to 20, adding the missing high-intent terms
(股价预警 / 价格预警 / 股价跌破提醒 / 阈值监控) and English coverage
(metric alert / threshold alert / price alert / webhook notification) that the
first release had none of. Dropped the `dashboard alert` keyword: it
contradicted the package's own design — alerts bind to a resource field, never
to a dashboardId (§1) — so it set a false expectation. Display name and doc
title no longer disagree; both now lead with 实时告警 / 股价预警 · 飞书/微信 Webhook.

## v1.0.0 · 2026-08-10

First release. Scenario-shaped package (PR-4 of the agent-skill 场景化重构):
one skill — 「资产字段跌破/突破阈值就通知我」 — start to finish, instead of the
97-skillId umbrella reference manual (`privora-cn-quant`).

- 11-step flow, one running example (贵州茅台 `600519` `close_price` 跌破
  1500), from "have you got a webhook channel" through a persisted, armed
  alert rule.
- Ships the **create-disabled → test → patch → toggle** sequence for
  forward-looking thresholds (the case the underlying `metric.alert.test`
  dry-run cannot prove directly, because `isTest` bypasses the gates but
  never the comparison itself): create the rule disabled with a
  deliberately-already-crossed placeholder threshold, prove the whole
  webhook/template/channel chain with a real `metric.alert.test` delivery,
  then `metric.alert.patch` in the user's real threshold and `metric.alert.toggle`
  to arm it — with no window where a placeholder threshold is live.
  `metric.alert.create` now accepts `enabled:false` for this
  (catalog addendum landing in the same PR).
- §5 documents the six silent gates (disabled / snooze / silenceMinutes /
  maxFiresPerDay / maxStaleSeconds / data-dedup) as the design they are, each
  with its own symptom + diagnostic call + fix — no "see troubleshooting"
  appendix.
- 20 skillIds only (the `realtime-alerting` preset's reachable set), no
  `delete`. Full 97-skillId reference stays in `privora-cn-quant` for anyone
  who needs more than this one scenario.
