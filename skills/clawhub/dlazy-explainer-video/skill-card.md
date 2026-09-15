## Description:

Turns a document, topic, or brief into a narrated explainer video by helping outline, storyboard, generate voiceover, build, and validate the result.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to ask a dLazy-hosted agent to convert documents, topics, or briefs into narrated explainer, courseware, report, or training videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires dLazy authentication and stores or uses an API key for CLI access.

Mitigation: Use the documented login or API-key setup flow, protect the local CLI config and DLAZY_API_KEY environment variable, and rotate or revoke the key if access is no longer needed or exposure is suspected.

Risk: Attached local files may be uploaded to dLazy media storage for video generation.

Mitigation: Attach only files intended for upload to dLazy and avoid sending sensitive or regulated data unless the deployment has approved that use.

Risk: The skill installs or runs a third-party CLI package to contact hosted dLazy APIs.

Mitigation: Review the linked source or npm package before installation in high-trust environments and prefer npx or sandboxed execution when possible.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-explainer-video)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and plain text guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill delegates video-generation work to the dLazy CLI and may reference hosted project state or uploaded files.]

## Skill Version(s):

1.0.13 (source: server release metadata; artifact frontmatter reports 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
