## Description:

Turns articles or documents into narrated explainer videos by guiding outline, storyboard, voiceover, build, and validation through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to route article or document-to-video requests to dLazy's hosted file-to-video workflow, including project continuation and optional file attachments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is labeled as article-to-video but invokes a broader file/document-to-video workflow.

Mitigation: Review the requested task scope before use and install only when the broader dLazy document/file-to-video service is intended.

Risk: Attached local files may be uploaded to dLazy media storage, and the CLI stores or uses a dLazy API key.

Mitigation: Avoid confidential files unless upload is acceptable, use least-necessary inputs, and rotate or revoke API keys from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-article-to-video)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May upload attached local files to dLazy media storage and relies on a locally configured dLazy API key.]

## Skill Version(s):

1.0.13 (source: server release metadata; artifact frontmatter reports 1.0.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
