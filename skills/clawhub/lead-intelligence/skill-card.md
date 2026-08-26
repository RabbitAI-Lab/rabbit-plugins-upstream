## Description:

Helps users search companies or contacts with compliant filters, score leads from user-submitted observable signals, and generate local lead reports with a Lead Intelligence API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

Sales, growth, and operations users can ask an agent to prepare compliant company or contact searches, score submitted leads deterministically, and summarize lead batches into local reports. Developers and operators can use the skill's request contracts to call the Lead Intelligence service without exposing API keys or unsupported provider payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The API key could be exposed if pasted into chat, logs, request bodies, or generated reports.

Mitigation: Keep LEAD_INTELLIGENCE_API_KEY in the environment, do not echo the full value, and send it only in the Authorization header.

Risk: Setting AI_SKILLS_API_URL to an untrusted endpoint would send the authorization header to that endpoint.

Mitigation: Only override AI_SKILLS_API_URL with a trusted Lead Intelligence service root.

Risk: Contact search results may be misused to infer, purchase, or enrich personal contact details.

Mitigation: Report only returned availability booleans, do not infer email addresses or phone numbers, and obtain separate confirmation before external outreach or CRM writes.

Risk: Lead scores can be mistaken for identity verification, purchase intent, or conversion probability.

Mitigation: Present scores as deterministic summaries of user-submitted observable signals and explain the factors that contributed to each score.

## Reference(s):

- [API Key Configuration](references/API-KEY.md)
- [Operations Contract](references/OPERATIONS.md)
- [HTTP Requests and Task Query](references/HTTP-REQUESTS.md)
- [Privacy, Scoring, and Error Rules](references/BEHAVIOR-RULES.md)
- [AI Skills Platform](https://ai-skills.open-idea.net)
- [Lead Intelligence ClawHub Listing](https://clawhub.ai/youteacher/skills/lead-intelligence)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON and bash examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include bounded task polling guidance, privacy-preserving lead summaries, deterministic scores, local reports, and billing-header summaries.]

## Skill Version(s):

1.0.0 (source: release evidence and package metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
