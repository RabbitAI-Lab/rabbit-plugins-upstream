## Description:

AstrMap VOC helps global e-commerce sellers collect Amazon reviews, analyze negative feedback, quantify frequent issues, surface hidden negative signals in high-star reviews, generate improvement suggestions, track review trends, and run incremental updates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sparkbayes](https://clawhub.ai/user/sparkbayes)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce sellers and agents use this skill to manage AstrMap review-analysis workflows for Amazon products, including task creation, status polling, result retrieval, trend review, and positive or negative review analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credit-consuming API actions can be started, and the security evidence notes that the code does not enforce the documented confirmation step.

Mitigation: Require explicit user confirmation before create_task, create_incremental, or trigger_analysis, and check account points before any credit-consuming action.

Risk: The skill sends the AstrMap API key, product identifiers or URLs, task IDs, and review-analysis data to api.astrmap.com.

Mitigation: Use the skill only when that transfer is acceptable, provide the API key through CUSTOMER_INSIGHTS_API_KEY or a direct parameter, avoid exposing it in chat or logs, and rotate or disable it when no longer needed.

Risk: Review collection may require a Chrome extension with an Amazon buyer account session.

Mitigation: Use a dedicated Amazon buyer account rather than a business seller account, verify the extension source before installation, and review requested browser permissions.

## Reference(s):

- [AstrMap API Reference](references/api_reference.md)
- [AstrMap Security Guide](references/security.md)
- [AstrMap App](https://app.astrmap.com/)
- [AstrMap Extension Download](https://www.astrmap.com/#download)
- [AstrMap API Endpoint](https://api.astrmap.com)
- [ClawHub Skill Page](https://clawhub.ai/sparkbayes/skills/astrmap-voc)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and API result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require CUSTOMER_INSIGHTS_API_KEY and may call AstrMap APIs when the user authorizes actions.]

## Skill Version(s):

1.0.6 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
