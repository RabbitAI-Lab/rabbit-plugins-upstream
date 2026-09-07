## Description:

Amazon ASIN 运营体检 combines product-detail and review evidence for a single ASIN to produce issues, supporting evidence, and operational priorities.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon operators and ecommerce teams use this skill to audit a single ASIN, inspect product-detail and review evidence, and prioritize listing, review, and product-improvement actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid analysis, collection, leaderboard, or advice flows can consume ARI credits, and account auto-confirm settings can reduce per-action prompts.

Mitigation: Use explicit quote-only requests for price checks, keep auto-confirm off when cost control matters, and require clear user confirmation before paid or persistent account changes.

Risk: A network interruption after a paid operation may occur after the service has already charged credits or generated a report.

Mitigation: Check the existing report or operation status by ASIN, report ID, or request ID before retrying any confirmed paid command.

Risk: Exports can write local CSV, Markdown, or HTML files, including to a user-specified output path.

Mitigation: Use expected local export paths, avoid arbitrary --out values, and verify the destination before running export commands.

Risk: Operational recommendations can be misleading if based on small samples, limited collection windows, or incomplete Amazon variant coverage.

Mitigation: Report sample size, date range, collection window, and known scope limits, and separate direct data readings from inferred strategy recommendations.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/asin-audit)
- [README](artifact/README.md)
- [Usage Guide](artifact/使用说明.md)
- [Operation Workflow](artifact/references/operation-workflow.md)
- [ARI CLI and API Reference](artifact/references/reference.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports and concise text summaries, with JSON, CSV, Markdown, or HTML files for advanced commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key; paid analysis and collection flows may consume ARI credits.]

## Skill Version(s):

1.4.7 (source: frontmatter, release evidence, _meta.json, CHANGELOG, script constant)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
