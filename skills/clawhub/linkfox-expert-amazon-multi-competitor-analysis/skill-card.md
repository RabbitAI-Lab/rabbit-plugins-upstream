## Description:

This skill turns an Amazon ASIN and marketplace into an end-to-end competitor analysis by selecting relevant competitors, collecting Keepa, SellerSprite, ABA, review, and AIGC signals, comparing products across eight dimensions, and generating an 11-section HTML report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers, marketplace analysts, and ecommerce operators use this skill to investigate 5-10 relevant competitors for a target ASIN, compare traffic, sales, pricing, review, A+ content, and image signals, and produce a data-grounded HTML competitor report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a LinkFox API key and calls external LinkFox services.

Mitigation: Review the configured LINKFOX_TOOL_GATEWAY and only provide credentials in environments where those external calls are approved.

Risk: The workflow may save full product, review, keyword, and analysis responses locally.

Mitigation: Run it in an approved workspace and review generated files before sharing or retaining them.

Risk: Some paths can upload local images or files to public URLs.

Mitigation: Avoid sensitive local images or files and require explicit approval before upload-oriented steps.

Risk: The evidence flags automatic feedback reporting and remote onboarding downloads for review.

Mitigation: Do not allow onboarding downloads or feedback submissions unless the user explicitly approves them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-expert-amazon-multi-competitor-analysis)
- [Competitor research pipeline I/O](skills/competitor-research-pipeline/references/io.md)
- [Competitor research pipeline data tools reference](skills/competitor-research-pipeline/references/data-tools-reference.md)
- [Competitor selector scoring model](skills/competitor-selector/references/scoring-model.md)
- [Report layout reference](skills/linkfox-report-generator/references/analysis-layouts.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with structured JSON intermediates and a generated HTML report file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The workflow returns a report path and summary after competitor selection is confirmed; intermediate product, review, keyword, and analysis data may be saved locally.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
