## Description:

Enables agents to read, create, and update Contentstack Content Management data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to manage Contentstack content types and entries through an OOMOL-connected account, including listing, retrieval, creation, and update workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands are presented for first-time setup without checksum or signature verification.

Mitigation: Review setup commands before installing and prefer a verified, version-pinned, checksum- or signature-validated oo CLI installation method.

Risk: Create and update actions can change Contentstack data.

Mitigation: Confirm the exact Contentstack payload and expected effect with the user before running write actions.

## Reference(s):

- [Contentstack Content Management Skill](https://clawhub.ai/oomol/skills/oo-contentstack-content-management)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Contentstack](https://www.contentstack.com/)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
