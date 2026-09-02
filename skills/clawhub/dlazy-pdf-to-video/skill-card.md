## Description:

PDF 转视频 PDF to Video helps agents turn PDFs and other documents into explainer, report, courseware, or training video workflows by parsing the document, outlining, storyboarding, generating voiceover, building, and validating the result.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, educators, and business users can use this skill to run a dLazy-hosted file-to-video workflow for PDFs and other documents. It is suited for creating explainer videos, report broadcasts, courseware, and training videos from user-provided source files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and user-selected documents may be sent to the third-party dLazy SaaS.

Mitigation: Confirm that the intended documents are appropriate to upload to dLazy before use.

Risk: A saved dLazy API key may persist in local CLI configuration.

Mitigation: Use the pinned npx invocation when a global install is not desired, and rotate or revoke the API key from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-pdf-to-video)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and CLI configuration details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill invokes a pinned third-party CLI package and may stream responses from the dLazy SaaS.]

## Skill Version(s):

1.0.9 (source: server release; artifact frontmatter says 1.0.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
