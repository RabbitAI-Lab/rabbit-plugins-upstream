## Description:

Turns slides or documents into narrated slideshow-style videos with voiceover and transitions through the dLazy hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and content teams use this skill to create explainer, report, courseware, or training videos from slides, PDFs, documents, and related source material.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached files may be sent to the dLazy SaaS service.

Mitigation: Use the skill only for content appropriate to share with dLazy, and avoid uploading sensitive files unless the service terms and account controls are acceptable.

Risk: The dLazy API key may be saved in a local CLI configuration file.

Mitigation: Use `DLAZY_API_KEY` per invocation or `npx @dlazy/cli@1.2.3` when persistent local configuration or a global install is not desired; rotate or revoke keys from the dLazy dashboard when needed.

Risk: Generated slideshow content can misstate source material or produce unsuitable narration, storyboards, or transitions.

Mitigation: Review generated video output, narration, and source-document interpretation before publication or business use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-slideshow-video)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and CLI guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference generated slideshow-video work managed by dLazy projects.]

## Skill Version(s):

1.0.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
