## Description:

Converts documents such as Word, Markdown, PDF, Excel, and PPT files into explainer, report, courseware, or training videos by using the dLazy CLI and hosted sandbox agent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, employees, and external users use this skill to start or continue dLazy document-to-video projects from an agent workflow. It is suited for turning uploaded documents into explainers, report broadcasts, courseware, and training videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached documents may be sent to dLazy API and media storage endpoints.

Mitigation: Attach only documents approved for upload to dLazy and review organization data-handling requirements before use.

Risk: The skill depends on installing or running the external dLazy CLI through npm or npx.

Mitigation: Review the referenced CLI source or npm package before installation and avoid running npm commands with elevated privileges.

Risk: An API key may be saved in the user's local dLazy configuration.

Mitigation: Use normal user-level file permissions, rotate or revoke keys when needed, and prefer per-invocation environment variables where local persistence is not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-doc-to-video)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Files]

**Output Format:** [Markdown or plain text with inline CLI commands and service-generated project outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May stream hosted agent responses and produce video-related files or links through the dLazy service.]

## Skill Version(s):

1.0.11 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
