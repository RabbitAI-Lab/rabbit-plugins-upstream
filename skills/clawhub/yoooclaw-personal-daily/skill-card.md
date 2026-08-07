## Description:

Generates a personalized daily news digest from the user's configured topics, using current web search results and source-quality filtering.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vivalavida-say-hi](https://clawhub.ai/user/vivalavida-say-hi)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to turn their configured interests into a concise daily news digest. It is suited for tracking current events across topics such as AI, electric vehicles, startups, robotics, companies, or products.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Configured interests may be sent as web-search queries.

Mitigation: Installers should only configure topics they are comfortable using for web search.

Risk: A vague prompt could activate the personalized digest unexpectedly.

Mitigation: Ask the agent to confirm before running the digest when activation intent is unclear.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/vivalavida-say-hi/skills/yoooclaw-personal-daily)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Structured chat text in Chinese with grouped news summaries and source URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Does not generate files; full digest is limited to about 1500 Chinese characters when enough current news is available.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
