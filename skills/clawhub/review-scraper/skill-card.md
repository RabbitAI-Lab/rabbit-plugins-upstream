## Description:

Review Scraper helps agents collect, analyze, filter, monitor, and export Amazon review data for ASINs across eight Amazon marketplaces through the ARI service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operators use this skill to ask an agent for Amazon review collection, VOC analysis, negative-review triage, trend checks, monitoring setup, and report or CSV exports for specific ASINs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spend account credits or change ongoing account behavior without a fresh per-request confirmation in some flows.

Mitigation: Review quoted costs before paid actions and set auto-confirm off if every paid action should require explicit approval.

Risk: Use requires connecting an ARI account, storing an ARI API key locally, and sending ASIN or review workflow data to ari.funewa.com.

Mitigation: Install only when this data sharing and local credential storage match the user's account and data-handling expectations.

Risk: Outputs depend on ARI-collected samples and may not cover all Amazon reviews, variants, or time windows.

Mitigation: State the sample range and data limits in analysis, and avoid treating incomplete samples as complete market evidence.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/review-scraper)
- [README](artifact/README.md)
- [Usage Guide](artifact/使用说明.md)
- [ARI CLI and API Reference](artifact/references/reference.md)
- [ARI Service](https://ari.funewa.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and text responses with optional command examples, CSV exports, HTML report exports, and online report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are based on ARI-collected Amazon review data and should state sample range, review evidence, costs, and data limitations when relevant.]

## Skill Version(s):

1.4.11 (source: server evidence, artifact/_meta.json, SKILL.md frontmatter, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
