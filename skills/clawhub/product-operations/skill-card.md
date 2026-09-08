## Description:

Helps product operations teams turn product or campaign goals into executable operations plans, calculate funnel and ROI metrics from user-provided summary data, run launch checklists, and export plans or retrospectives.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

External users and product operations teams use this skill to plan campaigns, review summarized funnel and ROI data, generate launch checklists, and export operational plans or retrospectives.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill calls an external service or a configured self-hosted endpoint.

Mitigation: Install only when use of the AI Skills hosted service is intended, and use only a trusted AI_SKILLS_API_URL for self-hosted deployments.

Risk: PRODUCT_OPERATIONS_API_KEY is a secret used for Bearer-token API calls.

Mitigation: Store it only in the configured environment variable and do not expose the full key in responses, logs, exports, or repositories.

Risk: Operational review data could include unnecessary business data if raw files or unrelated fields are submitted.

Mitigation: Submit only summarized metrics extracted from user-selected files, and confirm that raw files or unrelated business data are not sent.

Risk: Metric reviews can mislead users if missing data, zero denominators, or correlations are presented as firm conclusions.

Mitigation: Report calculation limits, show 'unable to calculate' when denominators are zero, and separate raw data, calculated metrics, and action recommendations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/youteacher/skills/product-operations)
- [AI Skills platform homepage](https://ai-skills.open-idea.net)
- [API key configuration](https://ai-skills.open-idea.net/skill-docs/product-operations/API-KEY.md)
- [HTTP requests and task polling](https://ai-skills.open-idea.net/skill-docs/product-operations/HTTP-REQUESTS.md)
- [Operations and fields](https://ai-skills.open-idea.net/skill-docs/product-operations/OPERATIONS.md)
- [Metrics and behavior rules](https://ai-skills.open-idea.net/skill-docs/product-operations/BEHAVIOR-RULES.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with API request examples and generated exports in CSV, XLSX, Markdown, and ICS formats.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses PRODUCT_OPERATIONS_API_KEY and may use AI_SKILLS_API_URL for a trusted self-hosted endpoint; file reviews should submit only summary metrics from user-selected files.]

## Skill Version(s):

1.1.0 (source: server release and package metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
