## Description:

Converts blog posts or document-style inputs into narrated videos by routing prompts and optional files through the dLazy file-to-video CLI workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, content teams, and developers use this skill to turn blog posts, articles, or document-style source material into narrated video drafts with storyboard, voiceover, and build steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release is advertised as blog-to-video while the artifact routes users to a broader file/document-to-video workflow.

Mitigation: Confirm the intended workflow with the user and review prompts or attached files before invoking the dLazy file-to-video CLI template.

Risk: Using the skill can require a locally stored dLazy API key and can upload attached files to dLazy storage.

Mitigation: Use approved dLazy credentials, rotate or revoke keys when needed, and avoid uploading sensitive files unless that data flow is approved.

Risk: The skill depends on the pinned @dlazy/cli package and external dLazy API and file-storage endpoints.

Mitigation: Review the pinned CLI package source before installation and run it only in environments where access to api.dlazy.com and files.dlazy.com is acceptable.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-blog-to-video)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and streamed CLI text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include dLazy project identifiers and operational guidance; attached local files can be uploaded by the dLazy CLI.]

## Skill Version(s):

1.0.17 (source: server release metadata; artifact frontmatter reports 1.0.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
