## Description:

Amazon product review intelligence analysis tool for global e-commerce sellers that fetches Amazon reviews, analyzes negative feedback, surfaces issues in high-rated reviews, tracks trends, and suggests product improvements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sparkbayes](https://clawhub.ai/user/sparkbayes)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce sellers and their agents use this skill to collect Amazon product review data through AstrMap, monitor task status, and retrieve review intelligence such as AI insights, negative review lists, tag distributions, statistics, and trends.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The AstrMap API key and review/task data are sent to AstrMap services for authentication and analysis.

Mitigation: Install only if AstrMap is trusted for this data, pass the key through CUSTOMER_INSIGHTS_API_KEY when possible, and rotate or disable the key when no longer needed.

Risk: Creating collection tasks requires a Chrome browser extension that can access data from sites the browser is signed in to.

Mitigation: Review the extension permissions before loading it and use a dedicated Amazon buyer account instead of a seller, primary, or business account.

Risk: Auto-analysis and incremental fetch operations can deduct AstrMap account points.

Mitigation: Check the points balance, explain the expected point use, and wait for explicit user confirmation before creating those tasks.

## Reference(s):

- [AstrMap API Reference](references/api_reference.md)
- [AstrMap Browser Extension Security Guide](references/security.md)
- [ClawHub Skill Page](https://clawhub.ai/sparkbayes/skills/amazon-review-insights)
- [AstrMap Extension Download Page](https://www.astrmap.com/en/#download)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and API response summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call AstrMap APIs and summarize task status, review statistics, AI insights, category-tag distributions, trends, and review lists.]

## Skill Version(s):

1.2.5 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
