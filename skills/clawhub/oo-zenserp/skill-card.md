## Description:

Zenserp enables agents to run Google Search, Image Search, Maps local search, and News search through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to retrieve Zenserp search results through an OOMOL-connected account while avoiding direct handling of raw API credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes remote installer commands for the oo CLI, which should not be run automatically by an agent.

Mitigation: Install the oo CLI only after inspecting and verifying the installer source, or use a safer trusted package channel.

Risk: Connector calls use an OOMOL-connected account and may consume Zenserp or OOMOL credits.

Mitigation: Inspect the live connector schema before running actions and stop on billing or credit errors until the account owner resolves them.

## Reference(s):

- [ClawHub Zenserp skill listing](https://clawhub.ai/oomol/skills/oo-zenserp)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Zenserp homepage](https://zenserp.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include returned data and a meta.executionId when actions run successfully.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
