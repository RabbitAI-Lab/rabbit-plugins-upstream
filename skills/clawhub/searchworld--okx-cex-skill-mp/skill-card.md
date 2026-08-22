## Description:

Guides agents through browsing, installing, updating, removing, and verifying AI trading skills from the OKX Skills Marketplace using the OKX CLI or limited MCP alternatives.

This skill is ready for commercial/non-commercial use.

## Publisher:

[searchworld](https://clawhub.ai/user/searchworld)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to discover and manage marketplace skill packages for trading assistants, including search, install, update, removal, download, and signature verification workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Marketplace skills are third-party content that can run locally with the agent's permissions after installation.

Mitigation: Review each skill's SKILL.md, publisher, and intended behavior before installation, and install only skills from trusted sources.

Risk: Force-install bypasses signature verification and can install a package after verification failure.

Mitigation: Avoid force-install unless the user knowingly accepts the failed verification risk.

Risk: The add flow may install a skill into multiple detected agent environments.

Mitigation: Confirm the target agent environments before installation and remove unwanted installs with the documented removal command.

## Reference(s):

- [OKX homepage](https://www.okx.com)
- [ClawHub skill page](https://clawhub.ai/searchworld/skills/okx-cex-skill-mp)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, markdown]

**Output Format:** [Markdown with inline shell commands and command output examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May refer users to JSON output flags for OKX CLI commands when machine-readable results are needed.]

## Skill Version(s):

1.4.4 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
