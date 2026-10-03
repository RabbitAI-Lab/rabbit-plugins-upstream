## Description:

A human–AI collaboration protocol for planning, verifying, and handing off complex or cross-session work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

People and their AI agents use this skill to structure complex tasks with context briefs, approval before consequential changes, checkable milestones, evidence-based review, and cross-session handovers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation can make this protocol active at session start across multiple agents.

Mitigation: Use --dry-run to inspect installation targets and avoid -g unless broad installation is intended.

Risk: Installing through npm introduces package-source and version-change exposure.

Mitigation: Install only from a trusted source and review or pin the npm version when stability matters.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/yottameta/skills/yotta-partner)
- [Project homepage](https://github.com/YottaMeta/yotta-partner)
- [Collaboration protocol and templates](references/collaboration_protocol.md)
- [Exception and recovery guide](references/exception_playbook.md)
- [Worked examples](references/walkthroughs.md)
- [Frequently asked questions](references/faq.md)

## Skill Output:

**Output Type(s):** [Guidance, Text, Markdown]

**Output Format:** [Markdown plans, checklists, and handover notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include context briefs, acceptance criteria, and verifiable milestone summaries.]

## Skill Version(s):

0.2.2 (source: skill frontmatter, release metadata, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
