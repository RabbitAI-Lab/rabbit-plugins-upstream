## Description:

Expands a single seed keyword into related Amazon marketplace keywords with search volume, trend, PPC bid, ranking difficulty, and competition metrics from Jungle Scout data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce operators, marketplace analysts, and agents use this skill to expand Amazon seed keywords into related keyword tables with demand, trend, competition, and PPC bid metrics. It supports keyword discovery, long-tail filtering, low-competition analysis, and advertising research across supported Amazon marketplaces.

### Deployment Geography for Use:

Global; keyword data queries are limited to the supported Amazon marketplaces: US, UK, DE, IN, CA, FR, IT, ES, MX, and JP.

## Known Risks and Mitigations:

Risk: The skill sends keyword queries and authorization credentials to LinkFox-controlled services.

Mitigation: Install only when LinkFox is trusted for the queried business data and keep API keys scoped, rotated, and out of shared logs.

Risk: Onboarding and billing flows can collect phone/SMS data and create payment orders.

Mitigation: Prefer account creation and plan purchases through the official LinkFox website, and require explicit user confirmation before paid actions.

Risk: Environment variable overrides can redirect API, login, or agent-user requests.

Mitigation: Review LINKFOX_* endpoint overrides before use and remove unexpected values from the runtime environment.

Risk: Full API responses are stored persistently as local JSON files.

Mitigation: Treat generated linkfox data directories as potentially sensitive and exclude them from commits, archives, and shared workspaces unless reviewed.

Risk: Automatic feedback reporting could include user intent or sensitive content.

Mitigation: Avoid sending sensitive user content through feedback and review feedback text before submission when possible.

## Reference(s):

- [Skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-junglescout-keyword-by-keyword)
- [API reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)
- [LinkFox Skills](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown tables and summaries, JSON API responses, and shell/configuration snippets when onboarding is needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes full API responses to local JSON files and prints either full JSON or a compact summary depending on response size.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
