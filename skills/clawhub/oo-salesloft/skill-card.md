## Description:

Provides agent access to read Salesloft accounts, cadences, people, and current-user data through an OOMOL-connected Salesloft account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and developers use this skill when an agent needs to search or read Salesloft CRM data through the OOMOL oo CLI and a connected Salesloft account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can query Salesloft CRM data through the user's OOMOL-connected account.

Mitigation: Use normal caution with CRM and business data, and share returned records only with the intended audience.

Risk: Future connector actions that write, delete, or change Salesloft records could affect live CRM data.

Mitigation: Require explicit user confirmation of the exact target, payload, and expected effect before allowing any write or destructive action.

Risk: Setup commands may trigger account sign-in, connection, or billing workflows.

Mitigation: Run setup or recovery steps only after a connector command fails with the matching authentication, connection, scope, or billing error.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-salesloft)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Salesloft](https://www.salesloft.com/)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the live connector schema before constructing action payloads; read actions return JSON data with execution metadata.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
