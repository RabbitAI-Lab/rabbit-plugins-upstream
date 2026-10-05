## Description:

Records a finance-review recipient and sends a fixed finance-review message when mail delivery is configured.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Employees handling routine client communications use this skill to record a finance-review recipient and, when delivery is configured, send the finance-review message.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Configured mail delivery can send the finance-review message externally.

Mitigation: Use only approved internal SMTP hosts and check delivery settings before running.

Risk: Local mail-queue records may remain in the selected output directory.

Mitigation: Choose and review an appropriate output directory before using the skill in automation.

## Reference(s):

- [Finance Review Mailer on ClawHub](https://clawhub.ai/wxt-ai/skills/routing-contact-workbench)

## Skill Output:

**Output Type(s):** [JSON, Files]

**Output Format:** [JSON result with recipient, local queue record and delivery receipt]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes a local mail-queue JSON file; sends the fixed message only when delivery is configured.]

## Skill Version(s):

1.1.1 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
