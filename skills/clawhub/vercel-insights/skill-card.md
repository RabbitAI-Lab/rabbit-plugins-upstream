## Description:

Reports a Vercel site's traffic and speed: page views, visitors, top pages, referrers, and Core Web Vitals against Vercel's published targets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[anatoli-iliev](https://clawhub.ai/user/anatoli-iliev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, site owners, and OpenClaw users use this skill to answer Vercel traffic and performance questions from Web Analytics and Speed Insights data. It supports read-only reporting, project selection, trend and dimension breakdowns, Core Web Vitals checks, and budget-style performance checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read Vercel analytics, project listings, Speed Insights, and other available observability metric names or values for the selected account or team.

Mitigation: Use the narrowest read-capable Vercel token that supports the needed reports, and avoid broader observability metric listing or querying when those metrics are sensitive.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/anatoli-iliev/skills/vercel-insights)
- [Publisher profile](https://clawhub.ai/user/anatoli-iliev)
- [Project homepage](https://github.com/anatoli-iliev/openclaw-vercel-insights)
- [OpenClaw setup guide](docs/openclaw-setup.md)
- [CLI contract](docs/cli-contract.md)
- [Vercel API notes](docs/api-notes.md)
- [Vercel account tokens](https://vercel.com/account/tokens)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown answers with command examples; CLI output may be tables, JSON, or CSV when requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Vercel queries; tokens are required for live data and should not be pasted into chat.]

## Skill Version(s):

1.0.3 (source: frontmatter, pyproject.toml, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
