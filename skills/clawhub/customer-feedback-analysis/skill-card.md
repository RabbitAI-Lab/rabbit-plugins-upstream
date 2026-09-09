## Description:

Analyze public customer reviews and discussions through Crawlora to identify complaint themes, feature requests, praise, and competitive gaps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Product, customer experience, and research teams use this skill to collect bounded public feedback samples and turn them into traceable voice-of-customer theme tables with counts, cited examples, caveats, and follow-up hypotheses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled helper can send the Crawlora API key to an arbitrary API base when CRAWLORA_API_BASE is set.

Mitigation: Run the skill only where CRAWLORA_API_BASE is unset or controlled, and review the destination before executing helper commands.

Risk: Public feedback samples can be biased by source, filters, sort order, missing dates, or pagination limits.

Mitigation: Report sample bounds, filters, denominators, exclusions, and collection gaps; avoid presenting sample counts as population prevalence.

Risk: Collected reviews or discussions may contain personal data or private customer material if the brief is scoped poorly.

Mitigation: Use public feedback only, avoid private customer data and internal prompts, keep excerpts brief, and do not export reviewer contact details.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown theme table and brief with cited examples, counts, caveats, and optional inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses bounded public feedback samples; reports filters, denominators, deduplication rules, gaps, and untested hypotheses.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
