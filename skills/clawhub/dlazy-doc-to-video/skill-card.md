## Description:

This skill helps turn Doc, Word, and Markdown files into explainer, report, or training videos by parsing the document, outlining it, creating a storyboard and voiceover, and building and validating the result.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

People who need to explain documents, reports, or training material use this skill to create an explainer, report, or training video from a Doc, Word, or Markdown file.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Messages and organization project activity are sent to the hosted service, and attached files are uploaded to its media storage.

Mitigation: Avoid sending sensitive information or attaching files that are not approved for the service; review the service terms and the CLI's data handling before use.

Risk: The CLI uses an organization API key saved in its local configuration or supplied through an environment variable.

Mitigation: Use the intended organization account, protect the local configuration and environment, and rotate or revoke the key if it may have been exposed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-doc-to-video)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Video, Text]

**Output Format:** [Generated video and streamed text responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Document files can be attached as inputs and uploaded to the service.]

## Skill Version(s):

1.0.37 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
