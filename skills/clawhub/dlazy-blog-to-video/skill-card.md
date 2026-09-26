## Description:

Converts blog posts and other documents into narrated videos with storyboard, voiceover, and build steps through the dLazy file-to-video workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators, marketers, educators, and developers use this skill to turn blog posts or documents into social, YouTube, explainer, courseware, report, or training videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly attached files can be sent to dLazy API and media storage.

Mitigation: Use only data approved for sharing with dLazy, and avoid confidential documents unless that sharing is allowed.

Risk: The skill advertises blog-to-video but routes work through a broader file/document-to-video template.

Mitigation: Confirm the user's intended input type and disclosure expectations before processing non-blog files.

Risk: Use requires a dLazy API key stored in local CLI configuration or passed through the environment.

Mitigation: Protect the key, prefer the documented login flow, and rotate or revoke the key if exposure is suspected.

Risk: The workflow depends on installing or running the pinned @dlazy/cli package.

Mitigation: Review the pinned package and repository before use, and keep installation scoped to approved environments.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-blog-to-video)
- [dLazy Homepage](https://dlazy.com)
- [dLazy CLI Repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May invoke the pinned dLazy CLI package and may reference generated video project state managed by the dLazy service.]

## Skill Version(s):

1.0.19 (source: server release metadata; artifact frontmatter says 1.0.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
