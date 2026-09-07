## Description:

Converts PPT, PowerPoint, Keynote, and other documents into explainer, pitch, courseware, report, or training videos through the dLazy hosted file-to-video agent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, employees, and external users can use this skill when they want an agent to turn presentations or documents into narrated videos using dLazy's project-based file-to-video workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive, regulated, or business-sensitive documents may be uploaded to dLazy's hosted API and file storage when attached with the skill.

Mitigation: Invoke the skill only when dLazy processing is intended, confirm attached files before use, and avoid private or regulated documents unless approved.

Risk: The skill's document scope is broader than the PPT-focused name, which may lead users to send non-presentation files to the third-party service.

Mitigation: Confirm the requested conversion target and file set before running the dLazy CLI, especially for Word, Excel, PDF, and other document inputs.

Risk: Global installation and saved API credentials can persist beyond a single run.

Mitigation: Prefer per-run npx or a contained environment when appropriate, and use revocable or narrowly scoped dLazy API credentials.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-ppt-to-video)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash code blocks and CLI guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference dLazy project ids, uploaded file URLs, API authentication state, and hosted file-to-video generation results.]

## Skill Version(s):

1.0.10 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
