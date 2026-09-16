## Description:

Linkup (linkup.so) routes Linkup search and webpage-reading requests through the OOMOL oo connector instead of direct API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to fetch webpages, search the web, retrieve sourced answers, request structured search data, and check Linkup credit balance through an OOMOL-connected Linkup account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands for the oo CLI, which creates a high-impact installation risk if run automatically.

Mitigation: Review the oo CLI installation source and prefer an official, version-pinned, signed or checksum-verified install method; do not let the agent run the remote installer pipeline automatically.

Risk: Actions depend on the live connector schema and connected account state, so stale payload assumptions or missing account connection can cause failed or incorrect runs.

Mitigation: Inspect the live connector schema before building payloads and use setup, connection, or billing steps only after a command fails for the matching reason.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-linkup)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Linkup Homepage](https://www.linkup.so)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects containing data and meta.executionId when actions are run with --json.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
