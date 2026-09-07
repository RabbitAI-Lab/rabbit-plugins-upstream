## Description:

Kling AI (klingai.com). Use this skill for ANY Kling AI request - reading, creating, and updating data. Whenever a task involves Kling AI, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate Kling AI through an OOMOL-connected account, including retrieving video-generation task state and submitting Kling AI V3 video-generation jobs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes unverified remote installer commands.

Mitigation: Review the oo CLI installer independently and use a vendor-documented, version-pinned, verified installation path; do not let an agent run curl-to-shell or PowerShell iex installer commands automatically.

Risk: Submitting a Kling AI video-generation task changes account state and may consume credits.

Mitigation: Confirm the exact video-generation payload and intended effect before execution, and connect only the Kling AI account intended for the task.

## Reference(s):

- [Kling AI homepage](https://klingai.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-kling)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May trigger oo CLI connector calls that return JSON data and execution metadata.]

## Skill Version(s):

1.0.0 (source: skill metadata and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
