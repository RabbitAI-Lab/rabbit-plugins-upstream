## Description:

Keygen helps agents operate a connected Keygen account through OOMOL's oo CLI for reading, creating, updating, validating, and deleting licensing resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Keygen products, policies, licenses, users, groups, entitlements, machines, components, and process heartbeats from an agent session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform broad Keygen account-changing operations, including license, user, policy, product, machine, component, entitlement, and process changes.

Mitigation: Review requested actions and confirm exact payloads and effects before write or destructive operations, especially on production accounts.

Risk: Some mutating actions may not be tagged as write or destructive in the skill.

Mitigation: Treat untagged actions as potentially mutating until the live schema and intended effect are verified.

Risk: First-time setup includes remote installer commands for the oo CLI.

Mitigation: Avoid running remote installer commands without independent verification or a safer package source.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-keygen)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Keygen Homepage](https://keygen.sh)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May execute oo connector schema and run commands against a connected Keygen account.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
