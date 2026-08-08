## Description:

Queries the Zhihuiya patent database for simple bibliographic patent metadata from patent IDs or publication numbers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to retrieve front-page patent bibliography for specific patent IDs or publication numbers. It helps present patent titles, abstracts, applicants, inventors, classification codes, filing dates, priority claims, and citation references without performing broader patent search or legal analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Patent queries and LinkFox credentials are sent to LinkFox services.

Mitigation: Install only when the LinkFox services are trusted, keep API keys in environment variables, and verify gateway-related environment variables point to expected LinkFox domains.

Risk: The skill includes agent-assisted account, SMS-code, API-key, and payment flows for authentication or credit issues.

Mitigation: Prefer the official LinkFox web flow for registration, API-key setup, and payments when users do not want to provide phone numbers, SMS codes, or payment choices through the agent.

Risk: Full patent lookup responses are retained in local linkfox data files.

Mitigation: Review and delete saved response files when they are no longer needed, especially after queries involving sensitive patent portfolios.

Risk: Queries consume LinkFox credits and batch calls can multiply the cost.

Mitigation: Warn users before paid lookups, reuse cached results where appropriate, and avoid automatic repeated queries with changed parameters.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-zhihuiya-simple-bibliography)
- [Publisher profile](https://clawhub.ai/user/linkfox-ai)
- [Zhihuiya simple bibliography API reference](references/api.md)
- [Authentication and credits onboarding](references/onboarding.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance, shell commands, and JSON API responses saved to local files or printed to stdout]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The lookup script saves full responses under a linkfox session data directory, uses a 24-hour local cache by default, and summarizes large responses unless inline output is requested.]

## Skill Version(s):

1.0.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
