## Description:

Converts PPT, Word, Excel, PDF, and other documents into narrated explainer, report, courseware, or training videos through dLazy's hosted file-to-video agent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when they have a document and need an agent-guided workflow to create an explainer, report broadcast, courseware video, or training video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached documents are sent to dLazy APIs and media storage for hosted processing.

Mitigation: Only upload documents the user is authorized to share, and avoid sensitive files unless the deployment has approved dLazy processing.

Risk: The dLazy API key can be stored in local CLI configuration.

Mitigation: Use per-invocation environment variables when persistent storage is not desired, and rotate or revoke the key from the dLazy dashboard when needed.

Risk: A global npm install leaves a persistent CLI binary on the system.

Mitigation: Use the pinned npx invocation when a temporary, on-demand CLI run is preferred.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-file-to-video)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and streamed CLI text with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference dLazy project IDs, uploaded file URLs, status messages, and generated video workflow results returned by the hosted service.]

## Skill Version(s):

1.3.10 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
