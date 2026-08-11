## Description:

西柚-关键词洞察 helps agents query Xiyou Insights Amazon ASIN and keyword analytics through LinkFox, including reverse ASIN keyword lookup, traffic scores, ranking trends, BSR, ABA trends, keyword competition, and suggested CPC across supported marketplaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers, e-commerce analysts, and developers use the skill to retrieve Xiyou ASIN and keyword metrics for keyword research, competitor analysis, marketplace trend review, and concise reporting in agent workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires LinkFox and Xiyou credentials and sends ASIN or keyword research data to LinkFox/Xiyou services.

Mitigation: Use session-only secrets where possible, avoid placing credentials in prompts or shared files, and run the skill only for data you are comfortable sending to those services.

Risk: Full API responses may be saved locally and can contain sensitive business research.

Mitigation: Review the local LinkFox response directory after use and periodically delete saved response files that should not persist.

Risk: Authentication and billing flows can involve phone/OTP onboarding, plan selection, and payment order creation.

Mitigation: Use self-service credential setup when possible, avoid phone/OTP onboarding unless explicitly chosen, and review every plan or payment step before creating an order.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-xiyou-dongcha)
- [Xiyou API reference](artifact/references/api.md)
- [Authentication and billing onboarding](artifact/references/onboarding.md)
- [LinkFox API key guide](https://skill.linkfox.com/linkfoxskills/guide.htm)
- [Xiyou OpenAPI console](https://www.xydc.com/openapi?xiyou-insights-web=%2Fopenapi)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Markdown, Files, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown summaries with JSON API responses and local JSON response files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Large responses are saved to a local LinkFox session data directory and summarized unless inline output is requested.]

## Skill Version(s):

0.0.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
