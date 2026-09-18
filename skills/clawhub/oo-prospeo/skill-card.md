## Description:

Prospeo enables agents to search, enrich, and read Prospeo account data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to let an agent inspect Prospeo connector schemas and run company enrichment, person enrichment, company search, people search, search suggestion, and account information actions through an OOMOL-connected Prospeo account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes one-line remote installer commands for the oo CLI.

Mitigation: Review the setup path before installation and prefer a verified, pinned, or signed oo CLI source.

Risk: Connector actions access Prospeo data through the signed-in OOMOL account.

Mitigation: Use the live connector schema before each action and confirm the intended account, payload, and effect before any action marked write or destructive.

## Reference(s):

- [ClawHub Prospeo skill page](https://clawhub.ai/oomol/skills/oo-prospeo)
- [Prospeo homepage](https://prospeo.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live oo connector schemas before each action; normal connector usage is read-focused.]

## Skill Version(s):

1.0.3 (source: evidence release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
