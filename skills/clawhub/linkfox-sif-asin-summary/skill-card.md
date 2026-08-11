## Description:

Analyzes Amazon ASIN traffic-source composition and exposure distribution using SIF data, including current, previous, newly entered, and exited period comparisons.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers, marketplace analysts, and e-commerce operators use this skill to inspect ASIN-level exposure sources, compare organic and paid traffic, and analyze period-over-period keyword movement across supported Amazon marketplaces.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ASIN query data, request metadata, and response data are sent to and returned from LinkFox's hosted service.

Mitigation: Use only with data appropriate for the LinkFox service, confirm the user's intent before queries, and avoid submitting unrelated confidential business data.

Risk: The skill handles API keys, phone/SMS login flows, account setup, billing recovery, payment QR codes, and order status checks.

Mitigation: Prefer self-service account setup, treat phone numbers, SMS codes, API keys, QR codes, and order identifiers as sensitive, and avoid storing keys in shared shell profiles.

Risk: Queries consume paid credits, and repeated retries or broad requests can increase cost.

Mitigation: Warn users before high-frequency or repeated calls, reuse the local cache where appropriate, and do not automatically retry with changed parameters after failures or empty results.

Risk: Full API responses are persisted locally under the working directory and may include product, marketplace, and analysis details.

Mitigation: Run in an appropriate workspace, review saved JSON before sharing it, and clean local output or cache files when they are no longer needed.

Risk: Automatic feedback reporting can send conversation or result context to LinkFox when triggered.

Mitigation: Review feedback content before submission and avoid sending private conversation details unless the user approves.

## Reference(s):

- [SIF-ASIN Traffic Source API Reference](references/api.md)
- [Authentication and Credit Onboarding](references/onboarding.md)
- [ClawHub Skill Release Page](https://clawhub.ai/linkfox-ai/skills/linkfox-sif-asin-summary)
- [LinkFox Skills](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, JSON files, guidance]

**Output Format:** [Markdown analysis with tables, inline shell commands, configuration snippets, and saved JSON response files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes full API responses under the working directory's linkfox data folder, summarizes large responses on stdout, and uses a 24-hour local cache for repeated parameter combinations.]

## Skill Version(s):

1.0.6 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
