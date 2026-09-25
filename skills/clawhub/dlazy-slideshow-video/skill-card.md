## Description:

Turns slides or documents into narrated slideshow-style videos with voiceover and transitions through the dLazy hosted CLI workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and content teams use this skill to ask an agent to convert presentations, PDFs, documents, images, or slide material into explainer, report, courseware, or training videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached files are sent to the external dLazy service, and selected local files may be uploaded.

Mitigation: Confirm the user is comfortable sharing the relevant content with dLazy before using the skill, and avoid uploading sensitive files unless approved.

Risk: The dLazy CLI can store an organization API key in the local user configuration.

Mitigation: Prefer npx for non-persistent use when appropriate, protect the local config file, and rotate or revoke the API key from the dLazy dashboard if exposure is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-slideshow-video)
- [Publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands and streamed CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference dLazy project ids, uploaded file URLs, authentication status, or service errors returned by the CLI.]

## Skill Version(s):

1.0.17 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
