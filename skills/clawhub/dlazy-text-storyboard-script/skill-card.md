## Description:

Generates detailed short-video storyboard scripts from user-provided themes, structured copy, or outlines while preserving the spoken script text word for word.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and creators use this skill to turn structured copy, themes, or outlines into shot-by-shot short-video storyboard scripts with scene, camera, notes, technical shooting details, and spoken script allocation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install and run a cloud generation CLI even though it presents as a text-only storyboard helper.

Mitigation: Install only when dLazy cloud generation is intended, and verify the exact npm package and version before allowing global installation or command execution.

Risk: Prompts and referenced media files may be sent to dLazy services, and login may store an API key locally.

Mitigation: Avoid sending sensitive prompts or media, use appropriate API-key handling, and rotate or revoke keys from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-text-storyboard-script)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration]

**Output Format:** [Markdown storyboard script with video parameters, numbered shots, scene descriptions, camera details, notes, and spoken script text.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The storyboard defaults to a 9:16 aspect ratio and 720p resolution when the user does not specify video parameters.]

## Skill Version(s):

1.2.12 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
