## Description:

Use when someone wants a polished short clip from text, images, or imported audio - 1080p B-roll, start/end frame animation, or a motion shot with a mixed track. Not for cinematic generated-audio clips or talking-head-only hosts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to guide an agent through one Pruna p-video-2 prediction for text-to-video, image-to-video, frame-pair animation, or audio-conditioned short clips. It helps collect required inputs, draft faithful motion prompts, choose supported generation settings, and prepare Pruna API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, images, and audio used for generation are sent to Pruna.

Mitigation: Avoid confidential or regulated media unless the user's policy allows Pruna to receive it.

Risk: The skill asks agents to install prerequisite skills, including an optional full-suite install, which can change agent behavior beyond the reviewed artifact.

Mitigation: Review or pin referenced prerequisite skills before allowing an agent to run the npx install commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/p-video-2)
- [Pruna file upload API endpoint](https://api.pruna.ai/v1/files)
- [Pruna predictions API endpoint](https://api.pruna.ai/v1/predictions)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown with inline bash and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides one p-video-2 prediction per invocation; the generated media is produced by the external Pruna service.]

## Skill Version(s):

1.0.13 (source: evidence.release.version and SKILL.md frontmatter metadata.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
