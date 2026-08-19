## Description:

Queries the Zhihuiya patent database for forward citation details, including cited patents and non-patent literature for supplied patent IDs or publication numbers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Patent analysts, researchers, and developers use this skill to retrieve and summarize the patent and non-patent references cited by specific patents. It is intended for citation lookup and citation-detail presentation, not legal-status, patent-family, or landscape analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Patent queries, API keys, and saved response or cache files may contain sensitive information.

Mitigation: Use trusted workspaces, protect LinkFox environment variables, and restrict access to generated LinkFox output and cache files.

Risk: The onboarding flow can request a phone number and SMS code, then print an API key.

Mitigation: Prefer obtaining API keys directly from the official LinkFox site, and only use SMS onboarding intentionally while keeping codes and keys private.

Risk: Citation queries consume credits and billing commands can create payment orders.

Mitigation: Review query cost, plan details, and payment method before running additional queries or order commands.

Risk: Feedback reporting may include user intent or result details when feedback is sent.

Mitigation: Review feedback content before sending it if the interaction may include sensitive patent, business, or user information.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-zhihuiya-patent-forward-citation)
- [智慧芽专利引用查询 API 参考](references/api.md)
- [解决认证和积分问题](references/onboarding.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with JSON response summaries and saved JSON response files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires patentId or patentNumber input; full API responses are saved under a LinkFox session directory, with summaries printed for larger responses.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
