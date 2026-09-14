## Description:

Converts PPT, PowerPoint, Keynote, and related document inputs into explainer, pitch, courseware, or training videos through the dLazy file-to-video workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and content teams use this skill to have an agent run the dLazy file-to-video workflow for PPT, PowerPoint, Keynote, and related document-to-video tasks such as explainers, pitches, courseware, and training videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached files are sent to dLazy services for processing.

Mitigation: Upload only documents intended for dLazy processing and avoid sensitive or restricted files unless the user has approval to share them with dLazy.

Risk: The dLazy CLI stores an API key locally for normal operation.

Mitigation: Use OS user-restricted configuration or the DLAZY_API_KEY environment variable when appropriate, and rotate or revoke the key if exposure is suspected.

Risk: The skill depends on an external npm CLI package.

Mitigation: Use the pinned npx or global install command in a restricted environment, review the upstream package before use, and avoid running npm with elevated privileges.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-ppt-to-video)
- [dLazy publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI project](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides an agent to invoke the pinned dLazy CLI workflow; resulting CLI sessions may stream text status and reference generated video project outputs.]

## Skill Version(s):

1.0.13 (source: server release evidence; artifact frontmatter reports 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
