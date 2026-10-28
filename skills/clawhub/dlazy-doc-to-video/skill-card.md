## Description:

doc to video, word to video, markdown to video, document to video — parse the document, outline, storyboard, voiceover, build, validate. Use when the user gives a Doc / Word / Markdown file and wants an explainer, report broadcast, or training video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users can provide a document and use this skill to create an explainer, report broadcast, courseware, or training video through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Attached documents and prompts are sent to dLazy services, and files are uploaded to its media storage.

Mitigation: Attach only documents you are authorized to upload, and check dLazy's storage terms before sharing sensitive material.

Risk: The CLI stores an organization API key in the user's local configuration.

Mitigation: Protect the local config and rotate or revoke the key if it may have been exposed.

Risk: The workflow installs or invokes a pinned third-party CLI package.

Mitigation: Review the pinned CLI package and project before installing.

## Reference(s):

- [dLazy website](https://dlazy.com)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [CLI project page listed in skill metadata](https://github.com/dlazy-ai/cli)
- [ClawHub release page](https://clawhub.ai/dlazyai/skills/dlazy-doc-to-video)

## Skill Output:

**Output Type(s):** [Video files, Text, Markdown]

**Output Format:** [Generated video files with accompanying project text; exact formats depend on the service response.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The workflow may upload attached documents to dLazy media storage.]

## Skill Version(s):

1.0.32 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
