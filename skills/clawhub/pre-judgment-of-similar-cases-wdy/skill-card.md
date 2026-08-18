## Description:

This skill retrieves relevant legal provisions and similar cases from Wendaoyun for user-described disputes, then formats legal consequences and suggested next steps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rose-develop](https://clawhub.ai/user/rose-develop)

### License/Terms of Use:

MIT-0

## Use Case:

External users and legal support agents use this skill to retrieve relevant legal provisions and similar case examples from Wendaoyun based on a user's dispute summary. It can format retrieved laws, cases, and optional next-step guidance in Markdown.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Legal dispute summaries are sent to a third-party API and may contain personal or sensitive facts.

Mitigation: Avoid including names, ID numbers, addresses, account details, or other unnecessary sensitive facts unless disclosure to Wendaoyun is appropriate.

Risk: The skill formats legal provisions, similar cases, and suggested next steps that users may treat as decision-ready legal guidance.

Mitigation: Review retrieved results and recommendations before relying on them, especially for high-impact legal decisions.

## Reference(s):

- [Wendaoyun Open Platform](https://open.wendaoyun.com/home)
- [Wendaoyun get-laws API endpoint](https://h5.wintaocloud.com/prod-api/api/invoke/get-laws)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, API Calls, Configuration instructions]

**Output Format:** [Markdown legal lookup results with law excerpts, similar case summaries, optional guidance, and setup instructions when configuration is missing]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses WENDAOYUN_API_KEY and sends user-provided dispute summaries to Wendaoyun API endpoints; top_k defaults to 3 and is capped at 5.]

## Skill Version(s):

1.0.7 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
