## Description:

Converts documents such as Word, Markdown, PDF, PPT, and Excel files into explainer, report, courseware, or training videos through the dLazy hosted file-to-video agent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and content teams use this skill to turn source documents into structured video projects with outline, storyboard, voiceover, build, and validation steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The third-party dLazy CLI and hosted service receive the documents, prompts, and project context supplied during use.

Mitigation: Use the pinned npx invocation or an isolated environment, review the linked CLI source or package before use, and avoid submitting documents that should not be shared with dLazy.

Risk: Files attached with the CLI are uploaded to dLazy media storage before being referenced by the hosted agent.

Mitigation: Review and minimize uploaded files, remove sensitive content when possible, and only attach materials appropriate for the dLazy service.

Risk: Authentication uses a dLazy API key that may be stored in local CLI configuration or supplied through an environment variable.

Mitigation: Keep the key revocable, protect local config and environment access, and rotate or revoke the key from the dLazy dashboard when access should change.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-doc-to-video)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown text with CLI commands and streamed assistant responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference uploaded files and project IDs; responses depend on dLazy service availability, account authentication, and credits.]

## Skill Version(s):

1.0.14 (source: server release metadata; artifact frontmatter reports 1.0.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
