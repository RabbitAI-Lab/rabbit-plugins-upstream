## Description:

Check whether other AI agents can find, install and trust the current GitHub repository. Reads its public ScBee Agent-Ready score (0-100, fixed rules) across agent card, llms.txt, MCP config, SKILL.md, AGENTS.md, install line, OpenAPI, licence, security policy and releases, shows the three fixes worth the most, offers to add those files locally, and only if the human says yes, lists the project on ScBee so agents can find it. Use when someone asks "can agents use my repo?", "is this agent-ready?", "should I add llms.txt or AGENTS.md?", or wants their project to be discoverable by agents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hmakt99](https://clawhub.ai/user/hmakt99)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use the skill to assess whether a public GitHub repository is discoverable, usable, and trustworthy for AI agents, then review prioritized improvements. It can offer local changes and a public ScBee listing, which require the user's explicit approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment was benign but had medium confidence because one local reference could not be resolved, leaving that material unassessed.

Mitigation: Review the unresolved referenced material before relying on the assessment or installing the skill.

Risk: Listing a project on ScBee creates a public listing.

Mitigation: Proceed with registration only after the user explicitly agrees.

## Reference(s):

- [Agent-Ready Check on ClawHub](https://clawhub.ai/hmakt99/skills/agent-ready-check)
- [ScBee](https://scbee.vercel.app)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Files]

**Output Format:** [Markdown assessment with a score and prioritized fixes; optional repository files after approval]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Score from 0 to 100; fixed-rule assessment. Repository changes and public listing require explicit user approval.]

## Skill Version(s):

1.0.0 (source: frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
