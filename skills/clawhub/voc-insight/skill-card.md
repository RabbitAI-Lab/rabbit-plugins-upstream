## Description:

VOC洞察 helps agents collect and analyze Amazon reviews to surface customer personas, purchase motivations, usage scenarios, sentiment, unmet needs, Listing copy ideas, and product improvement recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and ecommerce operators use this skill to ask an agent for VOC reports, review collection, negative-review triage, competitor comparison, category benchmarking, and Listing optimization guidance for specified ASINs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses an ARI API key and sends Amazon review, product, report, monitoring, and account requests to ari.funewa.com.

Mitigation: Install only when this data sharing is acceptable; keep the API key in ARI_API_KEY or the local user config and do not include it in prompts, reports, or command examples.

Risk: Some commands consume credits or make persistent account changes, including confirmed analysis, collection, schedules, competitor bindings, watch management, mark-read actions, exports, and workbench status changes.

Mitigation: Review quotes and target identifiers before execution, and run confirmed or account-changing commands only after the user explicitly asks for that action.

Risk: A network interruption during a paid command may occur after the service has already charged credits or created a report.

Mitigation: Check the existing report or operation status before retrying paid commands so the same work is not accidentally charged twice.

Risk: Review-derived insights can be misleading when the review sample is small, stale, or limited to a specific collection window.

Mitigation: Report sample size, site, time window, report ID, credits used, and whether findings are direct data, inference, or recommendations.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/funewa/skills/voc-insight)
- [ARI CLI and API reference](references/reference.md)
- [ARI product management](https://ari.funewa.com/zh/products)
- [ARI reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports and guidance with inline shell commands; exported reports may be Markdown, HTML, or CSV depending on the command.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses an ARI API key and may call ari.funewa.com for review, product, report, monitoring, and account-related operations.]

## Skill Version(s):

1.4.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
