## Description:

Cincopa enables agents to search and read Cincopa account data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agent users use this skill to inspect Cincopa action schemas and list asset tags, assets, galleries, and gallery items through an OOMOL-connected Cincopa account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that pipe downloaded scripts directly into a shell.

Mitigation: Review the setup path before installing; if the oo CLI is not already trusted, prefer a verified installer or documented package source instead of running the remote installer blindly.

## Reference(s):

- [Cincopa homepage](https://www.cincopa.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub Cincopa skill](https://clawhub.ai/oomol/skills/oo-cincopa)

## Skill Output:

**Output Type(s):** [shell commands, JSON, guidance]

**Output Format:** [Markdown with inline shell commands and JSON-oriented guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read actions return JSON data with a meta.executionId value.]

## Skill Version(s):

1.0.3 (source: server release metadata, target metadata, and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
