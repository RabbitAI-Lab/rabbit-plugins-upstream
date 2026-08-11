# Changelog

Hand-written. The top entry below IS the changelog `publish.sh` reads and
sends to ClawHub (`read_top_changelog_entry` in `publish.sh` takes everything
between the first and second `## ` heading) — there is no heuristic
git-diff-based generator here, unlike `agent-skill/publish.sh`. Add a new
`## vX.Y.Z · YYYY-MM-DD` entry at the top for every release; never edit an
already-published entry.

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
