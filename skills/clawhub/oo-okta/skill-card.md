## Description:

Operate Okta through an OOMOL-connected account to read, create, update, delete, and manage Okta users, groups, memberships, and lifecycle actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, IT operators, and identity administrators use this skill to inspect Okta connector schemas and run Okta user, group, membership, and lifecycle actions through the OOMOL oo CLI. It is intended for connected Okta environments where credentials are managed server-side.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes pipe-to-shell installer commands from remote URLs.

Mitigation: Use a signed or package-managed installation method where possible, or independently verify the CLI installer before execution.

Risk: The skill can perform high-impact Okta identity changes, including write and destructive user and group operations.

Mitigation: Require explicit user confirmation for every write or destructive action, including the exact target, payload, and expected effect.

## Reference(s):

- [ClawHub Okta skill page](https://clawhub.ai/oomol/skills/oo-okta)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Okta homepage](https://www.okta.com/)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, API Calls, Guidance]

**Output Format:** [Markdown with inline bash, PowerShell, text, and JSON command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include Okta connector responses containing data and meta.executionId values.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
