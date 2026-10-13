## Description:

Queries the details of a WeChat Channels live room by its live ID using Qinghu data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and analysts use this skill to retrieve details about a specific WeChat Channels live room and summarize the results for a user.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup or upgrades may change Node, npm packages, PATH, or shell profiles without clear prior approval.

Mitigation: Require explicit user approval before installing or upgrading tools or changing PATH or shell profiles.

Risk: Live-room lookups consume paid Qinghu credits, and failed calls may still incur charges.

Mitigation: Confirm the estimated credits and obtain consent before paid calls; avoid repeated trial-and-error calls.

Risk: Using the tool requires a locally configured Qinghu token.

Mitigation: Ask the user to configure their token locally and do not disclose it in responses.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-shipinhao-live-detail)
- [Qinghu qhkit package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise Markdown summary; table file for larger results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports credits charged for paid calls and distinguishes previews from full results.]

## Skill Version(s):

0.1.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
