## Description:

Yotta Anti Shallow is a prompt-only rules skill that asks agents to analyze before acting, state uncertainty, and self-check when tasks require rigor or reach complex L3+ scope.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers, analysts, writers, and agent users apply this skill to reduce shallow or overconfident responses on complex tasks by requiring upfront analysis, uncertainty disclosure, and completion self-checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill broadly changes agent response behavior and may add analysis or confirmation pauses to complex tasks.

Mitigation: Install it only for agents and workflows where this review posture is desired, and disable the rules in sessions where a concise result-only response is appropriate.

Risk: The included installers can copy the skill into multiple agent skill directories.

Mitigation: Prefer explicit --agent or --dir installation and review the target directory before installing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-anti-shallow)
- [npm package @yottameta/yotta-anti-shallow](https://www.npmjs.com/package/@yottameta/yotta-anti-shallow)
- [Project repository listed by artifact metadata](https://github.com/YottaMeta/yotta-anti-shallow)
- [Agent Skills standard](https://agentskills.io/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown or plain text with structured analysis, confidence, and self-check sections]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prompt-only behavior guidance; no resident service or runtime API output.]

## Skill Version(s):

1.3.4 (source: SKILL.md frontmatter, package.json, CHANGELOG, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
