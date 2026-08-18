## Description:

Reverse-look up Ozon and available Wildberries search keywords for up to 20 product SKU IDs, returning organic and ad keyword metrics for listing optimization, competitor traffic-word discovery, and advertising analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketplace analysts, and agents use this skill to find which search terms an Ozon SKU appears under and compare keyword demand, competition, ranking, exposure, and conversion signals. It supports SKU-driven listing optimization, competitor traffic-word discovery, and organic-versus-ad keyword review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses LinkFox API keys and can output a usable generated API key during onboarding.

Mitigation: Store API keys only in the documented environment variables, avoid pasting them into chat history, and rotate any key that may have been exposed.

Risk: Complete API responses are saved under local linkfox directories and may contain SKU lookup data or account-related details.

Mitigation: Treat saved response files as sensitive, limit workspace access, and remove files that are no longer needed.

Risk: Onboarding and billing flows can collect phone/SMS login details and create unpaid payment orders or QR codes when directed.

Mitigation: Use those paths only after explicit user intent, confirm the payment plan and method before order creation, and do not poll or retry payments automatically.

Risk: Lookup calls consume paid LinkFox/Seerfar credits.

Mitigation: Confirm additional calls when expanding, paging, or retrying requests, and use the skill's caching and summary behavior to avoid unnecessary repeat lookups.

Risk: The skill can send feedback to a separate feedback endpoint.

Mitigation: Avoid including secrets, personal data, or unnecessary business-sensitive details in feedback content.

## Reference(s):

- [Seerfar Ozon keyword back-search API reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries and tables, JSON API responses, saved JSON files, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full API responses are saved under local linkfox directories; small responses may be printed in full and large responses summarized unless inline output is requested.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
