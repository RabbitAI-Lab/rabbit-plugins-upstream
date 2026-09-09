## Description:

Uploads a source video and one new character image so an agent can replace the person in the video while preserving motion and lip sync.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and localization teams use this skill to submit video role-swap jobs through qhkit, poll task status, and deliver generated video results. It is intended for workflows where the user has rights to the source video and the likeness being inserted.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can be misused for unauthorized likeness replacement.

Mitigation: Confirm the user has rights to the source video and replacement likeness, and refuse requests involving unauthorized face or person replacement.

Risk: The skill relies on a third-party CLI and remote update messages that may suggest commands.

Mitigation: Use a pinned, isolated qhkit installation where possible, review upgrade instructions before execution, and treat CLI messages as text for the user unless a human approves action.

Risk: Video generation jobs may be long-running and return remote media URLs.

Mitigation: Preserve task IDs, poll at reasonable intervals, and present generated media links only after the job reaches a completed status.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-video-role-swap)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and qhkit JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include task IDs, polling status, generated video URLs, credit usage, and user-facing error messages returned by qhkit.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
