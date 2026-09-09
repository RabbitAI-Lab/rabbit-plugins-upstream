## Description:

Converts a blog post or article into a narrated video workflow with storyboard, voiceover, and build support through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn blog posts, articles, or related document content into narrated video projects for social, YouTube, explainer, courseware, or training workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The blog-to-video label routes users into a broader file/document-to-video workflow that can upload local files to dLazy.

Mitigation: Treat the skill as a general file/document-to-video workflow and attach only files intentionally meant for upload.

Risk: Using the third-party dLazy CLI sends prompts, project context, and attached files to dLazy services.

Mitigation: Install only when third-party processing is acceptable, prefer the npx/on-demand path where appropriate, and rotate or revoke the dLazy API key when no longer needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-blog-to-video)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; attached local files are uploaded through the dLazy CLI when used with --files.]

## Skill Version(s):

1.0.13 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
