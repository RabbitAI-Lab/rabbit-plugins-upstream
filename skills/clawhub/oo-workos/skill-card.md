## Description:

WorkOS helps agents manage WorkOS data through an OOMOL-connected oo CLI workflow for reading, creating, updating, and deleting users, organizations, and memberships.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to administer WorkOS AuthKit users, organizations, and organization memberships from an agent through OOMOL's oo CLI. It supports read actions and confirmed write or destructive actions against a connected WorkOS account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes a remote installer command for the oo CLI, which can execute code from a URL during setup.

Mitigation: Review and verify the OOMOL CLI installation method before running it; prefer a documented package or verified installer path.

Risk: Write and destructive actions can change WorkOS users, organizations, or organization memberships.

Mitigation: Confirm the exact payload, target, and expected effect with the user before running write or destructive WorkOS actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-workos)
- [WorkOS Homepage](https://workos.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the oo CLI to inspect live connector schemas and run WorkOS connector actions.]

## Skill Version(s):

1.0.3 (source: artifact metadata and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
