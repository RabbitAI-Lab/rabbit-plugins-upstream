## Description:

Waitwhile (waitwhile.com). Use this skill for ANY Waitwhile request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Waitwhile through an OOMOL-connected account, including customer lookup, creation, update, deletion, and location listing. It guides agents to inspect the live connector schema before running Waitwhile actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup may install the oo CLI by piping a remote installer script into a shell.

Mitigation: Require explicit user approval before installation and prefer a verified or package-manager-based CLI install path when available.

Risk: Write and destructive Waitwhile actions can create, overwrite, or delete customer data.

Mitigation: Confirm the exact action, target, payload, and expected effect with the user before running state-changing connector commands.

## Reference(s):

- [Waitwhile homepage](https://waitwhile.com)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-waitwhile)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses from connector actions are JSON objects containing data and execution metadata.]

## Skill Version(s):

1.0.0 (source: evidence release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
