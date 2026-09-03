## Description:

文档转视频 Doc to Video helps agents use dLazy to turn documents into explainer, report, courseware, or training videos by parsing source material and coordinating outline, storyboard, voiceover, build, and validation steps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and content teams use this skill when they have a document such as Word, Markdown, PDF, PPT, or Excel and want dLazy to generate an explainer, report broadcast, courseware, or training video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached documents are sent to dLazy hosted services for video generation.

Mitigation: Use the skill only with documents your organization permits sending to dLazy, and review dLazy terms, retention, and account controls before using confidential content.

Risk: Global installation of the dLazy CLI persists a local binary and saved configuration on the user's machine.

Mitigation: Use the pinned npx invocation for one-off use when a persistent global CLI install is not desired.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-doc-to-video)
- [dLazy CLI Repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline bash commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides an agent to invoke the pinned dLazy file-to-video template and continue project-scoped sessions.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter reports 1.0.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
