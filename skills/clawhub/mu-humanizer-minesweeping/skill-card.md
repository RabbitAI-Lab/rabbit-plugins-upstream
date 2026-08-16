## Description:

Evidence-conserving writing naturalizer and written-risk scanner that helps users rewrite Chinese, English, or mixed-language prose more naturally while preserving facts and flagging sensitive wording for review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[muippt](https://clawhub.ai/user/muippt)

### License/Terms of Use:

MIT

## Use Case:

Writers, editors, communications teams, and agent users apply this skill to polish announcements, business updates, brand copy, public-facing drafts, and bilingual prose while preserving facts, numbers, scope, and qualifiers. It can also scan natural-language text for written-language risk signals and return review-only guidance for high-sensitivity wording.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Suggested rewrites or risk-scan findings could affect legal, policy, factual, or public-communications meaning if accepted without review.

Mitigation: Review all diffs and high-sensitivity findings before publication; the skill is designed to preserve anchors and mark sensitive content for human review.

Risk: Company, team, or personal rule files may expose secrets, private business details, or personal data if users add them carelessly.

Mitigation: Keep optional rules local, avoid secrets and private business details, and confirm changes before writing or sharing rule files.

Risk: The written-risk mapping may miss risks outside its encoded rules, especially English written-taboo coverage and complex high-stakes contexts.

Mitigation: Use professional editorial, legal, policy, or factual review for high-stakes publications and treat scanner results as review support rather than final clearance.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/muippt/skills/mu-humanizer-minesweeping)
- [README](artifact/README.md)
- [中文 README](artifact/README_CN.md)
- [AI expression patterns](artifact/references/zh-patterns.md)
- [English expression patterns](artifact/references/en-patterns.md)
- [AI-TIC pattern rules](artifact/references/ai-tics.md)
- [Edit policy](artifact/references/edit-policy.md)
- [Fidelity audit](artifact/references/fidelity-audit.md)
- [Written taboo rules](artifact/references/written-taboo-rules.md)
- [Custom rules template](artifact/references/custom-rules-template.yaml)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Configuration]

**Output Format:** [Markdown diff reports with rewritten text, untreated signals, audit results, risk-scan findings, and lightweight process metrics]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Does not output AI-detection scores, does not directly write back to source documents, and treats high-sensitivity matches as review-only items.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact files report public skill version 6.7.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
