## Description:

Explainer Video turns a document, topic, or brief into a narrated explainer or training video workflow covering outline, storyboard, voiceover, build, and validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to start or continue dLazy hosted projects that convert documents, topics, or briefs into narrated explainer, courseware, or training videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, options, and user-selected files are sent to dLazy's hosted service.

Mitigation: Avoid attaching sensitive documents unless dLazy's terms and the user's organizational policy allow that data transfer.

Risk: A dLazy API key may be saved locally for reuse by the CLI.

Mitigation: Use the documented key rotation and revocation workflow, and prefer the npx invocation when avoiding a persistent global CLI installation.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-explainer-video)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include commands for dLazy CLI authentication, project discovery, project continuation, file attachment, and session control.]

## Skill Version(s):

1.0.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
