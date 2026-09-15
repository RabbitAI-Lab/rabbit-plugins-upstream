## Description:

Mintlify (mintlify.com). Use this skill for ANY Mintlify request - reading, creating, and updating data. Whenever a task involves Mintlify, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and documentation maintainers use this skill to inspect Mintlify deployment status and trigger production or preview documentation deployments through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup guidance asks users or agents to execute remote installer scripts for the oo CLI.

Mitigation: Review the installer path before use and prefer a versioned, signed, or checksum-verified installation method.

Risk: Mintlify deployment actions can change project state.

Mitigation: Confirm the exact payload and intended effect before running production or preview deployment actions.

## Reference(s):

- [ClawHub Mintlify Skill](https://clawhub.ai/oomol/skills/oo-mintlify)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Mintlify Homepage](https://www.mintlify.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce oo CLI commands and action payloads for Mintlify connector operations.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
