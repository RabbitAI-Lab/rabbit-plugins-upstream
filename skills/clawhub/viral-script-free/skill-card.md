## Description:

输入一份口播逐字稿，输出结构地图、开场钩子判定、留存节奏诊断、口语度评分、CTA 强度，并列出按严重度分级的问题清单。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators, marketers, and agent users can use this skill to inspect Chinese spoken-video scripts before publishing. It helps identify missing structure, weak hooks, pacing issues, written-language phrasing, and CTA placement while keeping transcript analysis local.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The free version intentionally shows only summary output and the first three issue titles, so users may miss detailed evidence and recommendations.

Mitigation: Treat the free report as a triage signal and review the original transcript manually before acting on script changes.

Risk: The declared Write permission is broader than the inspected code's documented stdout-only behavior.

Mitigation: Review requested file-write actions before execution and prefer stdout or JSON output unless a file write is explicitly needed.

Risk: The skill checks script structure and expression mechanics, not factual accuracy, legal compliance, platform approval, or business performance.

Mitigation: Use separate human or specialist review for factual, legal, advertising, and platform-policy questions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/viral-script-free)
- [Hook Pattern Rules](references/hook-patterns.md)
- [Platform Rules Reference](references/platform-rules.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance]

**Output Format:** [Console text or JSON diagnostic report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Free version limits visible findings to the first three issues and withholds detailed positions, rule evidence, rewrite advice, golden lines, and blueprint output.]

## Skill Version(s):

1.0.26 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
