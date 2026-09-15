## Description:

Kling AI lets agents operate Kling AI through an OOMOL-connected account using the oo CLI for video-generation submission and retrieval.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect Kling connector schemas, submit asynchronous Kling AI V3 video-generation tasks, and retrieve task status and generated videos through their connected OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup instructs users to pipe remote installer scripts directly into a shell.

Mitigation: Prefer a verified package or download-and-check workflow before running installers.

Risk: Submitting a video-generation request changes Kling AI state and may consume account credits.

Mitigation: Confirm the exact action payload and effect with the user before running write actions.

Risk: The skill operates through OOMOL as an intermediary for Kling AI actions.

Mitigation: Install only when the user is comfortable with OOMOL-connected account execution for Kling AI.

## Reference(s):

- [Kling AI homepage](https://klingai.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Kling AI Skill on ClawHub](https://clawhub.ai/oomol/skills/oo-kling)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; write actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
