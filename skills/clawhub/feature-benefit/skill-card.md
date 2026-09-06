## Description:

Connects Amazon product features to user benefits validated by review evidence and proposes Listing expression improvements; it requires an ARI API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and operators use this skill to analyze product detail and review evidence, then turn product features into supportable benefit-focused Listing recommendations. It is scoped to the fixed listing/benefits workflow and excludes advertising bidding, unsupported claims, and automatic Amazon page publishing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires an ARI account API key.

Mitigation: Use the documented setup/configure flow or ARI_API_KEY environment variable, keep the key out of reports and screenshots, and revoke or rotate it from the ARI account page if needed.

Risk: Paid review collection, AI analysis, leaderboard, and advice flows can spend ARI credits.

Mitigation: Run quote or preview steps first, require explicit confirmation unless a user-configured autoconfirm policy applies, and turn autoconfirm off when strict per-run approval is needed.

Risk: Monitoring, watch, and competitor settings can change recurring review-analysis behavior.

Mitigation: Review schedule, watch, and competitor settings after runs, explain expected costs before enabling recurring collection, and only perform management actions on explicit user request.

Risk: Export commands can write reports or review CSV data to local paths.

Mitigation: Choose export destinations deliberately, avoid public or shared folders for sensitive review data, and verify generated file paths before sharing.

Risk: The feature-benefit label is narrower than the broader ARI CLI capabilities bundled with the skill.

Mitigation: For this release, keep normal use to the fixed listing/benefits workflow and do not use unrelated broader commands unless the user explicitly requests those ARI workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/feature-benefit)
- [ARI CLI and API reference](references/reference.md)
- [Feature-benefit operation workflow](references/operation-workflow.md)
- [ARI product management](https://ari.funewa.com/zh/products)
- [ARI reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and structured JSON from CLI/API workflows, with shell commands and local file outputs for exports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report links, report IDs, credit usage, sample-window notes, and locally written CSV, Markdown, or HTML exports.]

## Skill Version(s):

1.4.5 (source: frontmatter, _meta.json, skill-defaults.json, CLI VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
