## Description:

Passcreator (passcreator.com). Use this skill for ANY Passcreator request - reading, creating, and updating data. Whenever a task involves Passcreator, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate Passcreator through an OOMOL-connected account, including listing templates and passes, inspecting template fields, and creating wallet passes from template-specific JSON payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create Passcreator wallet passes through the connected account.

Mitigation: Confirm the exact create_pass payload and intended effect with the user before running the write action.

Risk: The skill depends on access to the user's OOMOL-connected Passcreator account.

Mitigation: Install and use it only when that account access is intended, and run one-time CLI or authentication setup only from a trusted environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-passcreator)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Passcreator homepage](https://www.passcreator.com/)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include Passcreator connector results with data and meta.executionId fields.]

## Skill Version(s):

1.0.0 (source: release evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
