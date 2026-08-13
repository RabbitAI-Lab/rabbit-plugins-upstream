## Description:

Productlane operates a connected Productlane workspace through OOMOL's oo CLI connector for reading, creating, updating, and deleting Productlane data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent inspect Productlane schemas and perform authenticated Productlane company and contact workflows through an OOMOL-connected account. It supports read actions, write actions, and soft-delete actions with confirmation guidance for state-changing operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create or update Productlane companies and contacts in the connected workspace.

Mitigation: Confirm the exact payload and intended effect with the user before running write-tagged actions.

Risk: The skill can soft-delete Productlane companies and contacts by ID.

Mitigation: Confirm the target identifier and obtain explicit approval before running destructive-tagged actions.

Risk: The skill depends on the user's OOMOL account connection and local oo CLI availability.

Mitigation: Install or reconnect only when an action fails with a matching setup, authentication, scope, credential, app, or billing error.

## Reference(s):

- [Productlane homepage](https://productlane.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Productlane skill listing](https://clawhub.ai/oomol/skills/oo-productlane)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses from connector actions include a data object and meta.executionId when returned by the oo CLI.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
