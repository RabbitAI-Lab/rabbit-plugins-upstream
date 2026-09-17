## Description:

Kling AI lets agents inspect Kling connector schemas, submit asynchronous Kling AI V3 video-generation tasks, and retrieve generation status through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Kling AI through an OOMOL-connected account, including checking task schemas, submitting video-generation jobs, and retrieving completed videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path includes internet installer commands that run downloaded scripts in a shell.

Mitigation: Install only if OOMOL's distribution path is trusted; prefer inspecting a pinned or signed oo CLI installer before running it.

Risk: Submitting a video generation task is a write action that changes Kling AI state and may consume account credit.

Mitigation: Confirm the exact payload and intended effect before running submit_video_generation, and review billing or connection errors before retrying.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-kling)
- [Kling AI homepage](https://klingai.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an installed oo CLI, an authenticated OOMOL account, and a connected Kling AI provider; write actions require confirmation of the exact payload and effect.]

## Skill Version(s):

1.0.2 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
