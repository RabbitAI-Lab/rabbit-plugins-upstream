## Description:

Turns slides or documents into narrated slideshow videos with voiceover and transitions when a user wants a slideshow-style video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, developers, and content teams use this skill to ask a dLazy-hosted agent to turn PPT, PDF, Word, Excel, image, or document inputs into slideshow-style explainer, report, courseware, or training videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached files are sent to dLazy cloud services for processing.

Mitigation: Install only when cloud processing is acceptable for the intended data, and avoid sending sensitive files unless the user's organization permits use of dLazy for that content.

Risk: The dLazy API key may be stored locally in the CLI configuration.

Mitigation: Use the documented configuration location and prefer the DLAZY_API_KEY environment variable or key rotation when local persistence is not desired.

Risk: A global npm install keeps the dLazy CLI on the system after use.

Mitigation: Use the documented npx @dlazy/cli@1.2.3 alternative for one-off runs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-slideshow-video)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash code blocks and CLI guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference project ids, prompts, local file attachments, dLazy API endpoints, and authentication setup.]

## Skill Version(s):

1.0.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
