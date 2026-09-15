## Description:

Sauce Labs (saucelabs.com). Use this skill for ANY Sauce Labs request - reading, creating, and updating data. Whenever a task involves Sauce Labs, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and QA engineers use this skill to operate Sauce Labs through an OOMOL-connected account, including listing builds and jobs, retrieving build and virtual-device job details, listing job assets, and updating job metadata after confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include direct execution of remote installer scripts without verification.

Mitigation: Review installer source before use and prefer official, version-pinned, checksum- or signature-verified installation steps.

Risk: The skill can update Sauce Labs job name, tags, visibility, or pass status.

Mitigation: Confirm the exact update payload and expected effect with the user before running write actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-saucelabs)
- [Sauce Labs homepage](https://saucelabs.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Sauce Labs icon](https://static.oomol.com/logo/third-party/saucelabs.svg)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include Sauce Labs connector action names, schema inspection commands, JSON payload guidance, and confirmation prompts for write actions.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
