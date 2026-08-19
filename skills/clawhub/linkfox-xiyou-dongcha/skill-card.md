## Description:

西柚-关键词洞察 helps agents query Xiyou Insights Amazon ASIN and keyword analytics through LinkFox, including traffic scores, reverse ASIN keywords, ranking and traffic trends, BSR, ABA weekly trends, competition metrics, and suggested CPC across supported marketplaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers, ecommerce analysts, and agent users use this skill to retrieve Xiyou ASIN and keyword analytics for keyword discovery, traffic and ranking analysis, trend review, and CPC or competition assessment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic external feedback reporting can create a privacy concern for user intent or result-quality context.

Mitigation: Install only if the user accepts the publisher's feedback behavior, and avoid including sensitive business or credential data in feedback-worthy interactions.

Risk: Full API responses are saved durably in a local linkfox session directory and may include queried ASIN, keyword, or marketplace analytics data.

Mitigation: Avoid shared workspaces, review local saved response files before sharing projects, and remove retained response data when it is no longer needed.

Risk: LINKFOX_* endpoint override environment variables can redirect requests to hosts other than the expected LinkFox services.

Mitigation: Verify endpoint override variables before use and keep them unset unless a trusted operational need requires them.

Risk: Account and billing helper flows interact with LinkFox login, package, order, and payment-related endpoints.

Mitigation: Confirm each account or payment action with the user and use trusted credentials in a private session.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-xiyou-dongcha)
- [Xiyou API reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)
- [Xiyou OpenAPI service](https://openapi.xiyouzhaoci.com)
- [Xiyou OpenAPI console](https://www.xydc.com/openapi?xiyou-insights-web=%2Fopenapi)
- [LinkFox API key guide](https://skill.linkfox.com/linkfoxskills/guide.htm)

## Skill Output:

**Output Type(s):** [Analysis, API Calls, JSON, Files, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses; full responses are saved as JSON files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Large responses are summarized in stdout while the complete response is saved locally under a linkfox session data directory.]

## Skill Version(s):

0.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
