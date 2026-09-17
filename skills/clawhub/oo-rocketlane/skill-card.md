## Description:

Rocketlane helps agents search and read Rocketlane projects, tasks, and users through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to retrieve Rocketlane project, task, and user data without handling raw Rocketlane credentials directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer commands that execute scripts from OOMOL-controlled URLs.

Mitigation: Review the installer before use and prefer a verified, pinned, or package-manager installation method where available.

Risk: The OOMOL connection may expose Rocketlane project, task, and user data according to the scopes granted to the connected account.

Mitigation: Confirm the Rocketlane data scopes available to the OOMOL connection before using the skill.

## Reference(s):

- [Rocketlane ClawHub skill page](https://clawhub.ai/oomol/skills/oo-rocketlane)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [Rocketlane homepage](https://www.rocketlane.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs read-only get and list actions after live schema inspection.]

## Skill Version(s):

1.0.3 (source: server evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
