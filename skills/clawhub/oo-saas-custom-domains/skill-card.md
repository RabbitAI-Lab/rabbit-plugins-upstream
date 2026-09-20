## Description:

SaaS Custom Domains lets an agent manage SaaS Custom Domains resources through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to list, inspect, create, verify, delete, and purge SaaS Custom Domains resources from an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write and destructive actions can create, delete, or purge SaaS Custom Domains resources.

Mitigation: Confirm the exact action, target, payload, and expected effect with the user before execution; require explicit approval for destructive actions.

Risk: Optional oo CLI pipe-to-shell install commands execute remote installer code.

Mitigation: Use the installer only when needed and verify the OOMOL CLI source or follow the install guide before running it.

Risk: Authentication, connection, scope, credential, or billing errors can block connector actions.

Mitigation: Use setup and recovery links only after a matching command failure; do not proactively start login or connection flows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-saas-custom-domains)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [SaaS Custom Domains homepage](https://saascustomdomains.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses schema-first oo CLI actions; write and destructive actions require confirmation before execution.]

## Skill Version(s):

1.0.3 (source: server evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
