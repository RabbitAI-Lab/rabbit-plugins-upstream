## Description:

Captures pipeline leaks, objection patterns, pricing errors, forecast misses, competitor shifts, and deal velocity drops to enable continuous sales improvement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jose-compu](https://clawhub.ai/user/jose-compu)

### License/Terms of Use:

MIT-0

## Use Case:

Sales teams, revenue operations staff, and agent users use this skill to capture recurring deal risks, objection patterns, pricing errors, forecast misses, competitor shifts, and sales tooling requests in structured markdown logs. The skill also guides promotion of recurring patterns into reviewed sales assets such as battle cards, objection scripts, pricing playbooks, and qualification frameworks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional hooks can persistently remind the agent in later sessions beyond a clearly project-limited scope.

Mitigation: Use project-local hooks, avoid global or user-level hook installation, and enable only the lower-overhead UserPromptSubmit reminder unless Bash output detection is needed.

Risk: Sales logs may contain sensitive customer information, exact contract values, transcripts, or confidential deal terms.

Mitigation: Keep sensitive content out of shared logs, anonymize company names where needed, and use deal-size ranges instead of exact values.

Risk: Promoted learnings or extracted skills could introduce incorrect sales guidance if accepted automatically.

Mitigation: Review generated skills and proposed promotions before use or sharing, and require explicit approval before applying changes to persistent sales assets.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/jose-compu/skills/self-improving-sales)
- [OpenClaw Integration](references/openclaw-integration.md)
- [Hook Setup Guide](references/hooks-setup.md)
- [Entry Examples](references/examples.md)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates or appends project-local .learnings markdown files; optional hooks emit reminder text.]

## Skill Version(s):

1.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
