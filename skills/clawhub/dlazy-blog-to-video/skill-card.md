## Description:

Converts a blog post or article into a narrated video with storyboard, voiceover, and build support for social or YouTube.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask the dLazy hosted workflow to turn blog posts or linked articles into narrated video assets. It is suited to social and YouTube video drafts where the user accepts sending prompts and attachments to dLazy services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The advertised blog-to-video identity conflicts with instructions that run a broader file/document-to-video remote workflow.

Mitigation: Confirm that the broader file-to-video workflow is intended before installation or invocation, especially when processing documents beyond blog posts.

Risk: Prompts and attached local files may be sent to dLazy API and media storage services.

Mitigation: Only provide content authorized for third-party processing, and avoid sensitive files unless the user's organization has approved dLazy for that data.

Risk: The skill relies on a pinned external npm CLI and API-key based authentication.

Mitigation: Prefer on-demand npx execution where possible, review the pinned @dlazy/cli@1.2.3 package and source before use, and rotate or revoke API keys from the dLazy dashboard when needed.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct the agent to invoke the pinned @dlazy/cli workflow and upload user-provided files to dLazy services.]

## Skill Version(s):

1.0.12 (source: server release evidence; artifact frontmatter reports 1.0.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
