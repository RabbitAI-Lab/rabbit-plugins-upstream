## Description:

Converts blog posts, articles, and broader document inputs into narrated video projects with storyboard, voiceover, and build support through the dLazy file-to-video service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and content teams use this skill to ask an agent to turn a blog post, article, PDF, presentation, or other document into a narrated explainer, social, YouTube, courseware, or training video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached files may be sent to the external dLazy API and file storage service.

Mitigation: Use only with data approved for third-party SaaS processing, and avoid attaching confidential or regulated files unless dLazy's terms and controls meet the deployment requirements.

Risk: The skill stores or uses a dLazy API key through local CLI configuration.

Mitigation: Protect the local config file, prefer per-environment secrets handling where available, and rotate or revoke the organization API key when access changes.

Risk: The package name focuses on blog-to-video while the artifact and security evidence indicate broader document-to-video behavior.

Mitigation: Review tasks and attached files with the broader document-processing behavior in mind before invoking the skill.

Risk: Execution depends on a third-party npm CLI package.

Mitigation: Use the pinned @dlazy/cli 1.2.3 version from the evidence and review the package/source before installation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-blog-to-video)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the pinned @dlazy/cli 1.2.3 package and may send prompts and attached files to dLazy API and file storage endpoints.]

## Skill Version(s):

1.0.16 (source: server release metadata; artifact frontmatter reports 1.0.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
