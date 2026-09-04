## Description:

Converts blog posts, articles, and documents into narrated videos with storyboard, voiceover, build, and validation steps through the dLazy file-to-video workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to convert a blog post, article, or attached document into an explainer, social, YouTube, courseware, or training video. It guides an agent to authenticate with dLazy, start or continue a file-to-video project, and attach local files when needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release name focuses on blog-to-video, while the artifact describes a broader document-to-video workflow that may process PPT, Word, Excel, PDF, and other attached files.

Mitigation: Confirm the intended input type with the user before attaching files, and disclose that the workflow may process broader document content than the title suggests.

Risk: Prompts and explicitly attached files are sent to dLazy services, and the dLazy API key may be stored in a local CLI configuration file.

Mitigation: Use only approved data, avoid sensitive files unless permitted, and rotate or revoke the dLazy API key from the dLazy dashboard if access changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-blog-to-video)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May instruct use of a pinned dLazy CLI package, project ids, prompts, and explicitly attached files.]

## Skill Version(s):

1.0.11 (source: server release metadata; artifact frontmatter reports 1.0.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
