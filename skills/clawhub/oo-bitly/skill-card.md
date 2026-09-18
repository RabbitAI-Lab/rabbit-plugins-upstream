## Description:

Use this skill for Bitly requests including reading, creating, and updating data through the OOMOL-connected Bitly connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect Bitly action schemas, retrieve Bitlink, group, and user details, list groups, create short links, and update existing Bitlinks with confirmation for write actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes unverified remote install commands for the oo CLI that can execute changing code on the user's machine.

Mitigation: Review the installer path before installing and prefer a signed or otherwise verifiable oo CLI release.

Risk: Bitly write actions can change existing links or account-visible data.

Mitigation: Inspect the live action schema, check the exact payload and intended account changes, and obtain user confirmation before running write actions.

## Reference(s):

- [ClawHub Bitly skill page](https://clawhub.ai/oomol/skills/oo-bitly)
- [Bitly homepage](https://bitly.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill directs the agent to inspect live connector schemas before constructing requests and to confirm state-changing Bitly updates with the user.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
