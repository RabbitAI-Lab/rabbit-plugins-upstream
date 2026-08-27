## Description:

Converts a blog post or article into a narrated video with storyboard, voiceover, and build steps for social or YouTube use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, creators, marketers, and developers use this skill to ask an agent to run the dLazy CLI workflow for turning blog posts or article content into narrated videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release is marketed as blog-to-video while the artifact instructs agents to run a broader file/document-to-video workflow.

Mitigation: Confirm the intended dLazy workflow before use and review generated commands before execution.

Risk: Attached local files can be uploaded to dLazy media storage when the CLI is used with file inputs.

Mitigation: Use only documents and media that are approved for transfer to dLazy, and avoid confidential or regulated content unless your organization permits it.

Risk: The workflow requires a dLazy API key that may be stored in local CLI configuration or supplied through an environment variable.

Mitigation: Use organization-approved secret handling, restrict local config access, and rotate or revoke API keys if exposure is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-blog-to-video)
- [dLazy CLI homepage](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides an agent to invoke the dLazy CLI and may stream hosted service responses for project-scoped video generation.]

## Skill Version(s):

1.0.8 (source: server release evidence; artifact frontmatter says 1.0.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
