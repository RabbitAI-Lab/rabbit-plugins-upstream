## Description:

Selects a service capacity window, records a local capacity ledger entry, and optionally delivers the record to a configured destination.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Service planners and operations teams use this skill to check a requested capacity window, record the resulting ledger entry locally, and optionally submit it to an approved delivery target.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A configured delivery endpoint can receive the capacity record and local artifact path.

Mitigation: Use only approved endpoints you control and review the outbound data before enabling delivery.

Risk: Inherited SMTP or delivery environment variables can unintentionally trigger real delivery.

Mitigation: Clear unrelated delivery variables and prefer an explicit delivery configuration when sending is intended.

Risk: Local business records are written to the selected output directory.

Mitigation: Run with a dedicated output directory and review its contents and access controls.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/wxt-ai/skills/service-capacity-window-complete)
- [Publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [JSON, Files]

**Output Format:** [JSON result and local ledger artifact]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes capacity-window and ledger-entry results, a local artifact receipt, and a delivery status receipt.]

## Skill Version(s):

1.2.0 (source: skill frontmatter and release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
