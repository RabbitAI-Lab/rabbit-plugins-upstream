## Description:

This skill helps agents inspect MongoDB Atlas projects and clusters through the OOMOL MongoDB Atlas Administration connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to list MongoDB Atlas projects, inspect project details, list clusters, and retrieve cluster details from a connected OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: MongoDB Atlas project and cluster metadata is routed through a third-party connector service.

Mitigation: Use the skill only when sharing that metadata with OOMOL's connector service is acceptable for the target account and environment.

Risk: The setup guidance includes remote installer commands that are not pinned or independently verified.

Mitigation: Install the oo CLI through a verified package source or inspect and pin the installer before running it.

Risk: Future connector actions could change MongoDB Atlas state if write or destructive actions are added.

Mitigation: Keep usage to the listed read-only actions unless a future version clearly documents write actions and requires confirmation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-mongo-db-atlas-administration)
- [MongoDB Atlas homepage](https://www.mongodb.com/products/platform/atlas-database)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON-shaped connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include data and execution metadata when actions run with JSON output.]

## Skill Version(s):

1.0.2 (source: evidence release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
