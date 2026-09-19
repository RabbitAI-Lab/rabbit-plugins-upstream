## Description:

PDF 转视频 PDF to Video helps an agent use dLazy's hosted file-to-video workflow to turn PDFs or other documents into explainer, report, courseware, or training videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when they want an agent to run dLazy's PDF or document-to-video workflow for explainers, report broadcasts, courseware, or training videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached documents may be sent to dLazy's API and media storage.

Mitigation: Use the skill only with files approved for dLazy hosted processing, and avoid attaching confidential documents unless that upload is acceptable.

Risk: Authentication requires a dLazy API key that may be stored in local CLI configuration.

Mitigation: Use a revocable API key, protect the local configuration file, and rotate the key if exposure is suspected.

Risk: A global CLI install persists the pinned dLazy CLI on the user's system.

Mitigation: Prefer the pinned npx invocation when a temporary install is more appropriate, and review the pinned package or source before installation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-pdf-to-video)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides an agent to authenticate with dLazy, start or continue dLazy projects, attach files, and handle CLI/API error states.]

## Skill Version(s):

1.0.15 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
