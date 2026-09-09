## Description:

Turns a video idea into a reviewable production plan, then expands it into canvas shapes for story, character, scene, shot, keyframe, video generation, and final concatenation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative operators use this skill to turn a high-level video idea into a structured idea-to-video workflow, including story planning, character portraits, scene and shot breakdowns, keyframes, generated shot videos, and a merged final video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs and drives an external dLazy CLI and may store a dLazy API key locally.

Mitigation: Use a per-run npx invocation or isolated environment when possible, verify the package and version before use, and rotate or revoke the API key if exposure is suspected.

Risk: Prompts and selected media may be uploaded to dLazy services for generation.

Mitigation: Limit file access to media intended for upload and avoid submitting confidential or sensitive content unless the dLazy service terms and data handling are acceptable.

Risk: The artifact contains conflicting execution instructions and can propose terminal commands.

Mitigation: Review each generated command before execution and avoid granting broad filesystem or shell access beyond the immediate task.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-idea2video)
- [dLazy CLI source declared by skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package declared by skill metadata](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage declared by skill metadata](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline JSON-like templates and bash commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires dLazy CLI access and a dLazy API key; prompts and selected media may be sent to dLazy services and generated media URLs may be returned.]

## Skill Version(s):

1.3.18 (source: server release evidence; artifact frontmatter reports 1.3.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
