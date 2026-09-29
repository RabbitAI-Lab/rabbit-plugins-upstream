## Description:

Detects the presence of delivery packages within the target surveillance area; suitable for inventory checks and unattended alerts at community stations, residential entrances, and office building lobbies. | 包裹检测技能，检测目标监控区域内是否出现快递包裹，适用于社区驿站、小区门口、写字楼前台快递盘点和无人值守提醒

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to analyze surveillance images, videos, or media URLs for delivery-package presence, counts, positions, retention status, and related report links. It also supports querying prior package-detection reports from the connected cloud service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Package-surveillance media or URLs may be sent to lifeemergence.com cloud services.

Mitigation: Use the skill only with media approved for that service and avoid submitting sensitive surveillance content unless data-handling requirements are satisfied.

Risk: The skill may silently create or reuse local account state and store authentication tokens locally.

Mitigation: Run the skill in an isolated workspace or account context, review local state before reuse, and remove stored credentials when the deployment ends.

Risk: Shared workspaces may expose report history through reused identity state.

Mitigation: Avoid shared workspaces until identity isolation is verified, and use dedicated identities for separate users or tenants.

Risk: The hidden open-id option could affect identity association if exposed or relied on directly.

Mitigation: Do not expose the hidden identity option to end users; restrict operator access and validate identity behavior before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-package-detection-analysis)
- [Skill usage demo](https://lifeemergence.com/sample.html)
- [API interface documentation](artifact/references/api_doc.md)
- [Analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown reports, Markdown tables, JSON analysis output, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include package detection findings, counts, locations, reminders, status messages, and report links.]

## Skill Version(s):

1.0.14 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
