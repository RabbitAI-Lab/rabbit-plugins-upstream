## Description:

A structured workflow skill dedicated to social-media carousel design. The core method is 'decide intent first, then execute,' using a 'single-confirmation + cover-first' two-phase flow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Social media creators and agents use this skill to plan cohesive carousel slide sets and guide their cover-first generation. It structures the direction, slide plan, confirmation, and follow-up generation steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media are sent to dLazy, and local media may be uploaded for processing.

Mitigation: Send only prompts and media approved for dLazy cloud processing.

Risk: The dLazy API key is saved in the local CLI configuration.

Mitigation: Protect the local configuration and rotate or revoke the key if it may have been exposed.

Risk: The skill text contains a stale CLI version note alongside the 1.2.3 install commands.

Mitigation: Review the external CLI and confirm version 1.2.3 before installation.

## Reference(s):

- [dLazy CLI project page](https://github.com/dlazy-ai/cli)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Structured guidance, Shell commands]

**Output Format:** [Markdown with slide-planning tables, confirmation prompts, and CLI command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Provides a structured carousel plan and generation workflow; image rendering is performed through the dLazy CLI.]

## Skill Version(s):

1.3.37 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
