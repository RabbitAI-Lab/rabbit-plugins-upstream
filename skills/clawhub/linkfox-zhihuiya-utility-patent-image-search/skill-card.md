## Description:

Image-based utility model patent similarity search using Zhihuiya, with support for public image URLs, country/date/legal-status filters, and ranked patent-result summaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search for visually similar utility model patents from a product image URL, supporting patent-risk screening and prior-art research. Results are similarity-ranked and should not be treated as legal determinations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images and patent-search parameters are sent through LinkFox/Zhihuiya workflows, and local images may be uploaded to a public URL valid for 24 hours.

Mitigation: Use only images and search parameters that are appropriate for third-party processing, and avoid confidential unreleased images unless temporary public access is acceptable.

Risk: The onboarding flow can handle SMS login, API keys, account credentials, and billing orders.

Mitigation: Keep SMS codes and API keys out of shared logs, prefer temporary or managed secret storage, and confirm any payment or credit-consuming action before execution.

Risk: The search script persists full API responses and cache files in LinkFox session directories.

Mitigation: Review saved JSON files for sensitive product, patent, or account information before sharing the workspace or logs.

Risk: Patent similarity scores can support screening but do not establish infringement or freedom-to-operate conclusions.

Mitigation: Present results as similarity-ranked research output and recommend professional patent counsel for legal decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-zhihuiya-utility-patent-image-search)
- [Zhihuiya patent image search API reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, files, guidance]

**Output Format:** [Markdown guidance with JSON parameters, shell commands, and saved JSON API responses.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full API responses are saved to LinkFox session data; large responses are summarized unless inline output is requested.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
