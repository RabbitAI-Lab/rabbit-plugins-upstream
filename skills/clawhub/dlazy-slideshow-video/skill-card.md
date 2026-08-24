## Description:

Slideshow Video turns slides or documents into narrated slideshow videos with voiceover and transitions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to start or continue dLazy hosted projects that convert PPT, PDF, Word, Excel, or other document inputs into explainer, report, courseware, or training slideshow videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached documents are sent to dLazy's hosted service when the skill is invoked.

Mitigation: Use the skill only with content that is appropriate to send to dLazy, and review the service terms before processing sensitive documents.

Risk: A persistent global CLI install and stored API key may broaden local credential exposure.

Mitigation: Use the npx invocation for non-persistent execution when appropriate, and prefer revocable API keys or per-command DLAZY_API_KEY for tighter credential control.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-slideshow-video)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides the agent to invoke the pinned dLazy CLI template and may reference project ids, file attachments, authentication setup, and service error handling.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
