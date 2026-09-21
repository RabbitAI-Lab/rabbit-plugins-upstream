## Description:

Instabot helps agents read, create, update, soft-delete, and restore Instabot data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Instabot records from an OOMOL-connected account, including user lookup, pagination, creation, update, soft-delete, and restore workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup may direct an agent to execute a remote installer script for the oo CLI.

Mitigation: Review the installer path before use and prefer official installation documentation with verification where possible.

Risk: Create, update, restore, and delete actions can change Instabot data.

Mitigation: Require explicit approval and confirm the exact payload and target before running write or destructive actions.

## Reference(s):

- [Instabot homepage](https://www.instabot.io/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-instabot)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill directs agents to inspect the live connector schema before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
