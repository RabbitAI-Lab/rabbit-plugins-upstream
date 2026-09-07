## Description:

Analyzes Amazon competitor reviews across ASINs to compare praised strengths, repeated complaints, trends, and differentiation opportunities, then produces competitor comparison reports and operating recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and ecommerce operators use this skill to compare their products with competitor ASINs, identify recurring buyer pain points, and turn review evidence into positioning, listing, monitoring, and product-improvement actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spend account credits through collection and AI analysis workflows, and some flows may execute under account auto-confirm rules.

Mitigation: Use “only quote, do not execute” for pricing-only sessions, turn autoconfirm off when strict approval is required, and review credit estimates before allowing paid actions.

Risk: The skill uses an ARI API key and network access to the ARI service.

Mitigation: Install only when ARI is trusted, keep the API key out of chat and reports, and avoid custom ARI_BASE_URL settings unless operating a trusted self-hosted environment.

Risk: Monitoring, schedule, watch, and competitor-binding actions can change persistent account state or trigger future collection costs.

Mitigation: Confirm the exact ASIN, site, schedule, watch identifier, and expected ongoing cost before approving persistent changes.

Risk: Exports can write files locally and may expose review or report data through chosen output paths.

Mitigation: Use export paths only in trusted local directories and avoid arbitrary paths in shared or untrusted environments.

Risk: Review analysis is limited by the comments ARI has collected and may not cover every Amazon review or product variant.

Mitigation: State sample size, collection window, site, and comparability limits in summaries, and avoid treating small samples or partial data as definitive market evidence.

## Reference(s):

- [ARI CLI and API Reference](references/reference.md)
- [ARI Amazon Review Assistant Usage Guide](使用说明.md)
- [ARI Account and API Keys](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI Billing](https://ari.funewa.com/zh/billing)
- [ARI Reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown reports, concise text summaries, JSON CLI responses, shell commands, and optional exported CSV/Markdown/HTML files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should state data range, sample limitations, credits used when applicable, and links to generated ARI reports when returned.]

## Skill Version(s):

1.4.7 (source: server release, frontmatter, changelog, _meta.json, script VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
