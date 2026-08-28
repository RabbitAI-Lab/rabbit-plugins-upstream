## Description:

Helps agents search public ad creatives, analyze advertisers by name, and create domain-based ad trend reports through the AI Skills Ad Intelligence API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to retrieve public ad-intelligence evidence for competitor advertising review, creative research, advertiser analysis, and domain-based trend reporting. It requires a configured AD_INTELLIGENCE_API_KEY.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Ad-search queries and the AD_INTELLIGENCE_API_KEY are sent to the documented AI Skills service.

Mitigation: Install only if this data sharing is acceptable, configure the key through the environment, and do not paste or log the full key.

Risk: Public ad-intelligence observations can be mistaken for proof of current campaigns, legal identity, performance, or permission to reuse creative assets.

Mitigation: Keep source URLs, regions, and first/last seen dates with results; treat results as observed public evidence and obtain separate permission before reusing creative assets.

Risk: API results may be partial, failed, cancelled, delayed, or billed according to response headers.

Mitigation: Use idempotency keys, bounded task polling, and report only actual API status, returned results, and billing headers without assuming completeness or double-counting charges.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/youteacher/skills/ad-intelligence)
- [AI Skills homepage](https://ai-skills.open-idea.net)
- [API Key configuration](https://ai-skills.open-idea.net/skill-docs/ad-intelligence/API-KEY.md)
- [Operations contract](https://ai-skills.open-idea.net/skill-docs/ad-intelligence/OPERATIONS.md)
- [HTTP requests and task polling](https://ai-skills.open-idea.net/skill-docs/ad-intelligence/HTTP-REQUESTS.md)
- [Behavior, evidence, and error rules](https://ai-skills.open-idea.net/skill-docs/ad-intelligence/BEHAVIOR-RULES.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, API calls, Guidance]

**Output Format:** [Markdown with inline shell commands, API request examples, and structured result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include task IDs, API status, billing headers, source URLs, regions, and first/last seen timestamps from API responses.]

## Skill Version(s):

1.2.1 (source: server release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
