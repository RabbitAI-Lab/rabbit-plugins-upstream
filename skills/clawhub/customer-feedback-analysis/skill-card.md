## Description:

Analyze public customer reviews and discussions through Crawlora to identify complaint themes, feature requests, praise, and competitive gaps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Product, support, research, and go-to-market teams use this skill to collect bounded samples of public customer feedback and turn them into traceable theme tables, cited examples, gaps, and follow-up hypotheses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product and review queries, filters, and request bodies are sent to Crawlora.

Mitigation: Use only public or approved feedback collection prompts and avoid confidential customer data in query text or POST bodies.

Risk: The skill requires a Crawlora API key.

Mitigation: Keep CRAWLORA_API_KEY in the environment, do not paste it into prompts or command history, and rotate it if exposure is suspected.

Risk: Sampled, filtered, or helpfulness-ranked reviews can overstate or understate customer sentiment.

Mitigation: Report source filters, collection dates, denominator counts, deduplication rules, and gaps alongside every theme table.

## Reference(s):

- [customer-feedback-analysis endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/customer-feedback-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown analysis with cited examples, source counts, filters, gaps, and optional shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call Crawlora endpoints through the bundled shell helper and print JSON for downstream analysis.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
