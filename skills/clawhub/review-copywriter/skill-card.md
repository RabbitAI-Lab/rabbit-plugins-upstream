## Description:

Organizes Amazon review purchase drivers, customer questions, and experience language into evidence-backed Listing optimization direction and supporting evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and operators use this skill to convert existing Amazon review and product data into Listing optimization plans, evidence lists, pain-point summaries, purchase motivations, trend notes, and action priorities. It is not intended for data-free copywriting, ad buying, keyword bidding, or automatic publication to Amazon pages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can trigger paid ARI analysis or collection workflows that spend credits.

Mitigation: Use quote-only paths when requested, report the estimated credit cost and balance before confirmed paid runs, and avoid relaxed auto-confirm thresholds unless the user explicitly asks for them.

Risk: The skill uses an ARI API key and may access Amazon review, product, account, and report data.

Mitigation: Install only if the publisher and ARI service are trusted, keep the API key out of reports and examples, and prefer the official ARI endpoint unless a custom endpoint is intentionally configured.

Risk: Monitoring, competitor setup, account confirmation settings, and exports can alter account state or write report data locally.

Mitigation: Confirm monitoring or competitor changes explicitly, keep exports to safe file paths, and avoid exporting data unless the user asks for it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/review-copywriter)
- [ARI CLI and API reference](references/reference.md)
- [Dedicated listing workflow](references/operation-workflow.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or concise text, with shell commands shown only for setup, advanced use, or troubleshooting.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include ASIN and site, review sample scope, trend caveats, report IDs, credit usage, remaining balance, and ARI report links when returned by the API.]

## Skill Version(s):

1.4.7 (source: server release evidence, SKILL.md frontmatter, CHANGELOG, _meta.json, scripts/ari.py)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
