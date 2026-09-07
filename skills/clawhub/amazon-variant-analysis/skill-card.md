## Description:

Helps Amazon sellers compare review performance across color, size, and other child-ASIN variants to identify weak variants, strong sellers, and inventory or listing actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and operators use this skill to run ARI-powered review collection and analysis, including variant, VOC, competitor, alert, benchmark, and export workflows. Paid collection or AI analysis workflows require an explicit quote and user confirmation before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles a live ARI API key.

Mitigation: Treat ARI_API_KEY and the local ARI configuration as sensitive credentials; do not paste keys into reports, examples, screenshots, or public files.

Risk: ARI_BASE_URL and ARI_WEB_URL can direct requests and web links to an environment-controlled host.

Mitigation: Leave these variables unset for normal use, or set them only when the destination is fully trusted.

Risk: Some collection, analysis, leaderboard, and advice commands can consume paid ARI credits.

Mitigation: Run quote or preview commands first and add --confirm only after the user has checked the cost and explicitly approved it.

Risk: A network or stream interruption after confirmation may still correspond to a completed, charged report.

Mitigation: Check the latest saved report before retrying a confirmed paid command.

Risk: The skill exposes broader ARI review-management workflows than the variant-analysis name alone implies.

Mitigation: Install it only when broad Amazon review analytics, alerts, workbench, benchmark, and export capabilities are intended.

## Reference(s):

- [ARI CLI and API Reference](references/reference.md)
- [User Guide](使用说明.md)
- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/amazon-variant-analysis)
- [Server-Resolved GitHub Source](https://github.com/funewa/Amazon-variant-analysis)
- [ARI Service](https://ari.funewa.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, CSV, HTML]

**Output Format:** [Natural-language guidance plus CLI JSON responses, Markdown or HTML reports, and CSV review exports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key; reports may include report IDs, report URLs, credits used, sample sizes, and analysis windows.]

## Skill Version(s):

0.1.2 (source: ClawHub release metadata; artifact frontmatter and _meta.json report 1.3.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
