## Description:

Searches LinkFox's historical Amazon opportunity metrics pool to reverse-filter US Amazon niches and keywords by market size, growth, competition, price tier, demographics, product features, and review themes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and e-commerce analysts use this skill to turn business criteria such as low competition, fast growth, price-tier gaps, demographics, or review pain points into candidate US Amazon niches and keywords. Agents can map natural-language selection criteria to the smallest viable filter set, run the LinkFox search, and present returned niche snapshots for comparison.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a LinkFox API key and may involve account, billing, phone-number login, or payment recovery flows.

Mitigation: Install only in environments where those credentials and flows are acceptable, scope API keys carefully, and confirm gateway-related environment variables point to legitimate LinkFox domains.

Risk: Search responses and potentially sensitive query data are persisted locally by the skill.

Mitigation: Keep generated LinkFox data out of shared repositories and review saved files before sharing workspaces or logs.

Risk: Automatic feedback reporting can send external telemetry.

Mitigation: Treat feedback reporting as external telemetry and disable or control it through the host environment when needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-amazon-opportunity-search-by-metrics)
- [API Reference](references/api.md)
- [Authentication and Billing Onboarding](references/onboarding.md)
- [LinkFox Skills](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown comparison tables and JSON API responses saved to local files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search calls require at least one keyword, niche name, or metric filter; the skill currently covers the US Amazon marketplace and successful calls consume LinkFox credits.]

## Skill Version(s):

1.0.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
