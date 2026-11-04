## Description:

ego-lite Windows browser automation skill that lets an AI agent control a browser with natural-language tasks for logged-in workflows, scraping, form filling, and parallel Space-based sessions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[clawhub-master](https://clawhub.ai/user/clawhub-master)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to automate Windows browser tasks such as operating logged-in SaaS, CRM, and internal systems, completing repetitive click-and-form workflows, and running multi-site scraping tasks. It is most useful when semantic page snapshots and isolated browser Spaces help the agent act without taking over the user's regular tabs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can let an agent act inside existing logged-in browser sessions.

Mitigation: Use separate browser profiles or isolated accounts for sensitive sites, supervise actions on financial or administrative systems, and pause for confirmation before high-impact actions.

Risk: The skill supports live-page JavaScript execution during browser automation.

Mitigation: Review generated automation scripts before running them on sensitive pages and restrict use to sites where agent-driven DOM access is acceptable.

Risk: Site-specific learning files may retain operational details from prior browser tasks.

Mitigation: Review learnings files before reuse or sharing, and avoid storing sensitive account, workflow, or private site details in those notes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/clawhub-master/skills/ego-browser)
- [learnings README](artifact/learnings/README.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with JavaScript, bash, and PowerShell snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce browser automation scripts, semantic page snapshots, JSON-formatted task results, and site-specific learning notes.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
