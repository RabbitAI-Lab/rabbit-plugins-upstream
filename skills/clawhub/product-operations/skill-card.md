## Description:

Helps users turn product or campaign goals into actionable operations plans, calculate funnel and ROI metrics from real summary data, run launch checks, and export plans or retrospectives.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

External users and product operations teams use this skill to plan campaigns, review operational metrics, create launch checklists, and prepare exportable plan or retrospective artifacts. It is intended for workflows where the user provides goals, dates, channel choices, budgets, team size, or summarized metrics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Operation requests and summarized metrics may be sent to the ai-skills.open-idea.net service API.

Mitigation: Use the skill only when that service is trusted and the submitted operational data is appropriate for the workflow.

Risk: The skill requires storing PRODUCT_OPERATIONS_API_KEY in OpenClaw configuration.

Mitigation: Protect the API key, avoid printing it in replies or logs, and rotate it if exposure is suspected.

Risk: Spreadsheet workflows can include sensitive raw data if the agent extracts broader data than intended.

Mitigation: Confirm the local extraction maps only the intended summary fields before submitting metrics.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/youteacher/skills/product-operations)
- [AI Skills platform](https://ai-skills.open-idea.net)
- [API key configuration](https://ai-skills.open-idea.net/skill-docs/product-operations/API-KEY.md)
- [HTTP requests and task polling](https://ai-skills.open-idea.net/skill-docs/product-operations/HTTP-REQUESTS.md)
- [Operations and fields](https://ai-skills.open-idea.net/skill-docs/product-operations/OPERATIONS.md)
- [Metrics and behavior rules](https://ai-skills.open-idea.net/skill-docs/product-operations/BEHAVIOR-RULES.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with inline shell commands and exported CSV, XLSX, Markdown, or ICS files when requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses user-provided operational inputs or summary metrics; local spreadsheet handling should submit only intended summary fields.]

## Skill Version(s):

1.1.2 (source: server release metadata and skill metadata packageVersion)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
