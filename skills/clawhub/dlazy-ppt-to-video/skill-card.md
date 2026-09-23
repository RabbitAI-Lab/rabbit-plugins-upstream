## Description:

Converts PPT, PowerPoint, Keynote, and other document inputs into explainer, pitch, courseware, or training video workflows through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and content creators use this skill to start or continue dLazy projects that turn slide decks and documents into structured videos with outlines, storyboards, voiceover, build steps, and validation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached documents may be sent to dLazy API and file-hosting endpoints.

Mitigation: Use the skill only when the dLazy account, service terms, and data-handling posture are acceptable for the files being uploaded.

Risk: Authentication can store a dLazy API key in local CLI configuration.

Mitigation: Prefer per-invocation credentials or the documented npx flow when avoiding persistent global install or stored local credentials is important.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-ppt-to-video)
- [dLazy CLI metadata homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown and terminal-oriented text with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May stream responses from dLazy hosted endpoints and may reference uploaded file URLs when local files are attached.]

## Skill Version(s):

1.0.16 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
