## Description:

Helps agents query Flowsery website analytics, examine visitor behavior and detected issues, and manage goal and payment records when explicitly requested.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tarasshyn](https://clawhub.ai/user/tarasshyn)

### License/Terms of Use:

MIT-0

## Use Case:

Website operators and developers use this skill to review traffic, trends, conversions, revenue, and detected site issues across Flowsery-tracked websites. With explicit authorization, they can inspect visitor profiles or manage goal and payment records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Visitor profiles and payment data can reveal personal details and sensitive revenue information.

Mitigation: Confirm authorization before viewing a specific visitor and show only the details needed to answer the request.

Risk: Direct API guidance allows irreversible deletion of goal events and payment records.

Mitigation: Require human review and explicit confirmation of the website, filters, date range, and record count before deletion.

Risk: A workspace token can grant access to sensitive analytics across multiple websites.

Mitigation: Keep the token private, use only the intended Flowsery endpoint, and prefer the read-only OpenClaw plugin for routine queries.

## Reference(s):

- [Flowsery Analytics](https://flowsery.com)
- [Flowsery API reference](artifact/references/api-reference.md)
- [Breakdown dimensions](artifact/references/breakdown-dimensions.md)
- [OpenClaw plugin setup](artifact/openclaw-plugin/README.md)
- [ClawHub skill listing](https://clawhub.ai/tarasshyn/skills/flowsery)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown analytics summaries and optional API command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include sensitive visitor or revenue information; disclose only what the request requires.]

## Skill Version(s):

1.1.0 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
