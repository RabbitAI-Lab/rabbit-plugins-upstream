## Description:

MemberVault lets an agent operate MemberVault data through OOMOL's oo CLI connector, including listing courses and adding, removing, or deleting users with confirmation safeguards.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage MemberVault accounts through an OOMOL-connected account, including reading course data and performing user access changes after inspecting live action schemas.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer scripts that can execute shell code during installation.

Mitigation: Install the oo CLI only from a verified package or signed/versioned release, and avoid pipe-to-shell installer commands when possible.

Risk: MemberVault write and destructive actions can add users, remove product access, or permanently delete user data.

Mitigation: Require explicit user confirmation of the target, payload, and expected effect before running add, remove, or delete actions.

Risk: Auth, connection, scope, credential, or billing failures can push users into setup and account-management flows.

Mitigation: Use first-time setup steps only after matching command failures and keep account connection or billing actions user-directed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-membervault)
- [MemberVault homepage](https://membervault.co/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with oo CLI shell commands and JSON payload examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector runs return JSON responses with data and meta.executionId.]

## Skill Version(s):

1.0.2 (source: evidence release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
