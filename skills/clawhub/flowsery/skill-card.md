## Description:

Openclaw Flowsery lets agents query Flowsery web analytics for site traffic, trends, visitor behavior, revenue, conversions, and AI-detected session issues, with documented safeguards for personal data and destructive operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tarasshyn](https://clawhub.ai/user/tarasshyn)

### License/Terms of Use:

MIT-0

## Use Case:

External site owners, marketers, and developers use this skill to answer Flowsery analytics questions, inspect traffic and conversion trends, review AI-detected UX issues, and manage goal or payment records when the user explicitly authorizes write or delete actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A Flowsery API token can provide workspace-level analytics access and expose sensitive site metrics if mishandled.

Mitigation: Use the narrowest token Flowsery allows, keep it out of logs and client code, and send it only to analytics.flowsery.com.

Risk: Visitor profiles and payment records can contain personal data such as email, name, location, activity history, and revenue.

Mitigation: Retrieve individual profiles only for explicit authorized requests and summarize the minimum detail needed to answer the user.

Risk: Goal and payment writes or deletes can alter or permanently erase historical business data.

Mitigation: Require explicit confirmation before recording or deleting goals or payments, restating the website, operation, filters, and date range.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/tarasshyn/skills/flowsery)
- [Flowsery Product Site](https://flowsery.com)
- [Flowsery Analytics API Reference](references/api-reference.md)
- [Breakdown Dimensions Reference](references/breakdown-dimensions.md)
- [OpenClaw Plugin README](openclaw-plugin/README.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Flowsery API query parameters, filters, date ranges, and concise analytics summaries.]

## Skill Version(s):

1.0.6 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
