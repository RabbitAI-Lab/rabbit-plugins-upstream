## Description:

Databar.ai lets agents use an OOMOL-connected account to read, create, and update Databar.ai tables and enrichment tasks through the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill when an agent needs to inspect Databar.ai account data, list or read tables, create tables, insert rows, discover enrichments, or submit enrichment and waterfall tasks through an OOMOL-managed connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote install scripts for the oo CLI.

Mitigation: Review the setup commands and install source before running them, and use first-time setup only when a command fails due to a missing CLI, authentication, or connection issue.

Risk: The skill can perform Databar.ai write actions such as creating tables, inserting rows, and submitting enrichment or waterfall tasks.

Mitigation: Require explicit user confirmation of the exact payload and expected effect before running any action tagged write or destructive.

Risk: Connector schemas can change outside the skill artifact.

Mitigation: Fetch the live action schema with oo connector schema before constructing a payload.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-databar-ai)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Databar.ai Homepage](https://databar.ai/)
- [oo CLI Repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include Databar.ai read results, task identifiers, status data, setup guidance, and confirmation prompts for write actions.]

## Skill Version(s):

1.0.3 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
