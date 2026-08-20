## Description:

Looks up SIF traffic keywords for a single Amazon ASIN, including organic and ad ranks, search volume, traffic share, conversion markers, and weekly or monthly time windows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and e-commerce analysts use this skill to retrieve and present keyword performance data for a specific Amazon ASIN. It supports reverse ASIN keyword lookup, rank checks, ad keyword analysis, traffic-share review, conversion-marker review, and period-based keyword filtering.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ASIN queries and related account data are sent to LinkFox.

Mitigation: Install and use the skill only when sharing those queries and account details with LinkFox is acceptable.

Risk: Full API responses are written locally and cached, which may preserve competitive keyword data or account-linked results.

Mitigation: Treat generated response files and cache files as sensitive, keep them in trusted workspaces, and remove them when no longer needed.

Risk: The onboarding flow can guide phone-number login, API-key setup, and paid credit purchase steps.

Mitigation: Protect generated API keys, review any payment order before scanning or paying a QR code, and confirm that the user intends to spend credits before additional calls.

Risk: Environment-variable gateway overrides can redirect API traffic.

Mitigation: Avoid using gateway override environment variables unless the destination is explicitly trusted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-sif-asin-keywords)
- [SIF-ASIN keyword API reference](references/api.md)
- [Authentication and credits onboarding](references/onboarding.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance, shell commands, and JSON API responses saved to local files or summarized to stdout]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes full API responses under a local linkfox session directory, summarizes large responses unless inline output is requested, and uses a 24-hour local cache for repeated parameter combinations.]

## Skill Version(s):

1.0.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
