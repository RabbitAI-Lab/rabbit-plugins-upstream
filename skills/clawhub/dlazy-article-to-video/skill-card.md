## Description:

Turns a written article, text, or news item into a narrated explainer video workflow covering outline, storyboard, voiceover, build, and validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke the dLazy CLI and hosted agent to turn articles or documents into narrated explainer, report, courseware, or training videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and options are sent to api.dlazy.com, and attached files are uploaded to files.dlazy.com.

Mitigation: Confirm organizational approval for dLazy's hosted service and avoid uploading confidential documents unless dLazy's terms and policy requirements allow it.

Risk: The skill uses a dLazy API key from local configuration or an environment variable.

Mitigation: Use scoped credentials, keep local configuration access restricted, and rotate or revoke keys when needed.

Risk: The release wraps an external CLI install path, optionally installed globally with npm.

Mitigation: Prefer npx/on-demand execution when a persistent global CLI is not desired, and review the pinned @dlazy/cli package before global installation.

Risk: The evidence notes a naming and scope mismatch between article-to-video wording and document/file-to-video behavior.

Mitigation: Confirm the intended dLazy template and input type before invoking generation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-article-to-video)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and CLI output guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May invoke a hosted dLazy service that returns streamed terminal text and project-scoped video generation results.]

## Skill Version(s):

1.0.17 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
