## Description:

Qinghu AI Creator Data Engine takes Douyin, Xiaohongshu, and Bilibili creator profile links, retrieves account profile and playback metrics, and exports a standardized Excel file for creator monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and creator-operations teams use this skill to batch-check creator account metrics, monitor competitor or partner accounts, and export the results for reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may request Qinghu API keys through chat.

Mitigation: Use a platform secret store, environment variable, or preconfigured credential file instead of pasting API keys into chat.

Risk: The skill may install or upgrade qhkit globally on the host.

Mitigation: Install only in environments where persistent global Node package changes are acceptable, or use an isolated runtime.

Risk: Qinghu creator-data workflow submissions can consume paid credits.

Mitigation: Run an estimate first and require explicit user confirmation before any generate action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-creator-data-engine)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys page](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, text, markdown]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides an agent to submit qhkit workflow requests and return generated Excel file links when the workflow completes.]

## Skill Version(s):

0.1.2 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
