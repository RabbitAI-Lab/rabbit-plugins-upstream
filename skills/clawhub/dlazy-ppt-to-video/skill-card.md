## Description:

Converts PPT, PowerPoint, Keynote, and other document inputs into dLazy hosted file-to-video projects for parsing, outlining, storyboarding, voiceover, building, and validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and users with dLazy credentials use this skill to start or continue hosted file-to-video projects that turn presentations and documents into explainer, pitch, courseware, or training videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached files may be sent to dLazy's hosted service.

Mitigation: Use the skill only with content approved for dLazy processing and avoid attaching sensitive files unless the user's policy allows it.

Risk: The dLazy CLI may store an API key in the user's local configuration.

Mitigation: Prefer per-invocation credentials or npx when persistence is not desired, and rotate or revoke the key from the dLazy dashboard when access should end.

Risk: A persistent global CLI install can remain available after the task is complete.

Mitigation: Use the pinned npx invocation when a temporary execution path is preferred.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-ppt-to-video)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and streamed CLI text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference hosted dLazy project ids and local file attachments uploaded through the dLazy CLI.]

## Skill Version(s):

1.0.14 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
