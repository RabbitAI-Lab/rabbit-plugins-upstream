## Description:

Security-first skill vetting for AI agents. Use before installing any skill from ClawdHub, GitHub, or other sources. Checks for red flags, permission scope, and suspicious patterns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xtdnpl](https://clawhub.ai/user/xtdnpl)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, agents, and reviewers use this skill to evaluate AI agent skills before installation by checking source trust, code behavior, permissions, red flags, and installation risk.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill provides advisory security judgments that may be overly conservative for unknown or low-signal skill sources.

Mitigation: Treat the report as review guidance and confirm high-impact installation decisions with a human reviewer.

Risk: The skill may suggest network commands for checking GitHub-hosted skills.

Mitigation: Run network checks only when the target source is expected and the command destination is understood.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/xtdnpl/skills/skill-vetter)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown report with optional shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces advisory security review findings, permission summaries, risk classification, verdict, and notes.]

## Skill Version(s):

1.0.0 (source: frontmatter and server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
