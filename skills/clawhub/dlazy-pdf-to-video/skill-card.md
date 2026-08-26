## Description:

PDF to Video turns PDFs and other documents into explainer, report, courseware, or training videos by using dLazy to parse, outline, storyboard, voice over, build, and validate video content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, educators, and business users use this skill when they have a PDF or other document and want a generated explainer, report broadcast, courseware, or training video. The skill guides an agent to authenticate with dLazy, start or continue a project, attach local files when needed, and run the hosted file-to-video workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached documents may be sent to dLazy hosted services and uploaded to dLazy media storage.

Mitigation: Use the skill only when that upload is acceptable, and avoid attaching confidential or sensitive documents unless the user has approved that handling.

Risk: The dLazy CLI stores an API key in a local user configuration file or accepts it through DLAZY_API_KEY.

Mitigation: Protect the local config file, prefer scoped organization keys, and rotate or revoke keys from the dLazy dashboard when access should change.

Risk: The workflow depends on the third-party dLazy CLI package and hosted API availability.

Mitigation: Review the disclosed CLI source and pinned npm package before installation, and surface authentication, balance, or service errors to the user with the documented remediation steps.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and CLI guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill directs the agent to use the pinned dLazy CLI workflow and may stream hosted service responses back through the terminal.]

## Skill Version(s):

1.0.7 (source: server release metadata; artifact frontmatter reports 1.0.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
