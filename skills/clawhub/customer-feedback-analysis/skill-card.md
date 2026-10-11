## Description:

Analyze public customer reviews and discussions through Crawlora to identify complaint themes, feature requests, praise, and competitive gaps for traceable voice-of-customer briefs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Product teams and analysts use this skill to compare bounded samples of public customer feedback, identify themes and competitive gaps, and prepare briefs with cited examples and explicit sample counts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Review-search queries and the Crawlora API key are sent to Crawlora.

Mitigation: Use the skill only if this disclosure is acceptable; keep the API key in the environment and out of commits and logs.

Risk: Overbroad collection may include irrelevant or sensitive feedback.

Mitigation: Bound collection to public feedback relevant to the task and avoid exporting reviewer contact details.

## Reference(s):

- [Customer Feedback Analysis on ClawHub](https://clawhub.ai/crawlora-org/skills/customer-feedback-analysis)
- [Crawlora endpoint reference](artifact/reference/endpoints.md)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [Markdown, Analysis, Guidance]

**Output Format:** [Markdown theme table and brief with cited examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports unique-review counts and denominators, collection dates and filters, exclusions, gaps, and proposed follow-ups.]

## Skill Version(s):

1.0.10 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
