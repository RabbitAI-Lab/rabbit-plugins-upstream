---
name: content-compliance-review
description: Review planned social-media content before publication for legal, platform-policy, account-safety, privacy, copyright, advertising, and audience-safety risks across scripts, captions, titles, comments, images, cover art, video frames, and audio. Use when a user asks for content compliance review, pre-publication risk checking, platform rule comparison, moderation-risk diagnosis, or safer revisions for one or more publishing platforms.
---

# Content Compliance Review

Review content conservatively, explain the evidence, and make the next edit concrete. Treat the result as decision support, not a guarantee of approval or legal advice.

## Review workflow

1. Identify the target platforms, intended audience, account type, commercial relationship, jurisdiction, publication date, and supplied media. Do not block a first-pass review when some context is missing; state assumptions and mark affected findings as uncertain.
2. Minimize sensitive data before analysis. Ask the user to redact passwords, identity numbers, payment details, private contact details, unpublished customer data, faces or voices lacking consent, and account recovery information. Never ask for login credentials or attempt to evade platform enforcement.
3. Inventory every review surface: spoken words, on-screen text, title, caption, hashtags, links, calls to action, claims, demonstrations, cover image, background objects, music, logos, comments, and metadata. If a medium cannot be inspected, say exactly what remains unchecked.
4. Read [references/common-risks.md](references/common-risks.md). For each target platform, read its core file and list every matching domain overlay under `references/platforms/<platform>-*.md`; load each overlay relevant to the content. For example, review Douyin medical content with both `douyin.md` and `douyin-medical.md`, and content involving minors with both `douyin.md` and `douyin-minors.md`. Distinguish WeChat Channels from WeChat Official Accounts; when the user only says “微信” and the content may be reused on both, read both rule files and state the assumption. For commercial content, sponsorship, product promotion, affiliate links, or purchase paths in mainland China, also read [references/laws/china-advertising.md](references/laws/china-advertising.md). Use [references/rule-schema.md](references/rule-schema.md) when adding or maintaining rules.
5. Separate four evidence layers:
   - applicable law or regulation;
   - current official platform policy;
   - campaign, category, or account-specific requirement;
   - practitioner heuristic or observed moderation pattern.
6. For time-sensitive conclusions, verify against current primary sources when web access is available. Record the source URL and verification date. If current verification is unavailable, label the conclusion `待核实` and never present an old rule or heuristic as confirmed policy.
7. Assess the content in context. Do not flag a word merely because it appears in a keyword list. Consider the complete claim, visuals, audience, placement, disclaimers, and likely interpretation.
8. Produce the report using the required format below. Prefer the smallest change that removes the risk while preserving the user's meaning. Do not help disguise prohibited content, bypass review, or migrate abuse to another account.

## Risk levels

- `禁止发布`: Clear severe violation, illegality, direct safety risk, fraud, credential exposure, or an attempt to bypass enforcement. Recommend stopping publication and, where appropriate, qualified legal or safety review.
- `高风险`: Strong basis for removal, restriction, account penalty, material consumer harm, or a misleading commercial claim. Require revision and human review.
- `中风险`: Context-dependent or remediable issue that may reduce distribution, confuse users, or breach a narrower rule. Recommend a specific edit.
- `低风险`: Minor ambiguity or presentation concern. Offer an optional improvement.
- `待核实`: Missing context, stale evidence, inaccessible media, conflicting rules, or uncertain applicability. State what evidence would resolve it.

Assign a level to each finding, not only to the whole submission. Never infer that “未发现明显风险” means “保证通过”.

## Required report

Respond in the user's language and include:

1. **结论**: `暂不发布 / 修改后再审 / 可发布但需人工确认 / 未发现明显风险` plus one-sentence reasoning.
2. **审查范围**: platforms and each inspected or uninspected surface.
3. **问题清单**: for every finding, give risk level, exact location or timecode, risky content, likely issue, evidence layer, source and date when available, and the consequence.
4. **修改建议**: give a minimal safe revision. Preserve claims only when the user can substantiate them. Do not fabricate qualifications, test data, permissions, citations, or disclaimers.
5. **平台差异**: show differences when multiple platforms are requested; do not collapse them into a single universal rule.
6. **待确认事项**: list unresolved facts, missing media, consent, licensing, substantiation, or stale rules.
7. **边界提示**: state that the review cannot guarantee publication, reach, or immunity from enforcement and is not a substitute for professional legal advice in high-stakes cases.

For long content, prioritize all `禁止发布` and `高风险` items, then summarize repeated lower-risk patterns with representative examples.

## Media handling

- For images and cover art, inspect visible text, logos, people, products, UI screenshots, QR codes, medical or financial depictions, dangerous demonstrations, and background details.
- For video, inspect the spoken track, subtitles, representative frames, transitions, end cards, music, and calls to action. Use timecodes when available.
- For audio, review the transcript plus music, impersonation, consent, and disclosure concerns. Mark transcription uncertainty.
- Do not perform face identification, infer sensitive traits, or expose private information. Review only what is necessary for publication safety.

## Maintaining the rule library

Store detailed rules in `references/platforms/<platform>.md`; keep general risk principles in `references/common-risks.md`. Give every rule a stable ID and the metadata required by [references/rule-schema.md](references/rule-schema.md).

When the user supplies a new rule:

1. Preserve the original wording in a short quotation only when necessary and permitted; otherwise summarize it accurately.
2. Mark its authority as `official`, `law`, `campaign`, `heuristic`, or `unknown`.
3. Add the source URL or user-provided provenance, publication or observation date, verification date, applicable content surfaces, and status.
4. Keep conflicting or superseded rules with explicit status instead of silently overwriting history.
5. Run `python3 scripts/validate_rules.py` from the skill directory after changes.
