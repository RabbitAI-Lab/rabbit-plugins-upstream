## Description:

Deploy privacy-first analytics with correct API patterns, rate limits, and GDPR compliance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ivangdavila](https://clawhub.ai/user/ivangdavila)

### License/Terms of Use:


## Use Case:

Developers and engineers use this skill to implement Umami, Plausible, or PostHog analytics integrations with privacy, consent, rate-limit, and credential-handling safeguards.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Analytics integrations can expose provider API keys if credentials are hardcoded or committed.

Mitigation: Store provider keys in environment variables and keep separate development projects for testing.

Risk: Tracking events can collect personal information or identifiers without appropriate consent.

Mitigation: Obtain required consent, avoid sending personal information in events, and configure retention limits.

Risk: Analytics requests may exceed provider rate limits and fail or drop data.

Mitigation: Implement exponential backoff on 429 responses and follow provider-specific batching or request patterns.

## Reference(s):


## Skill Output:

**Output Type(s):** [Guidance, Code, Configuration]

**Output Format:** [Markdown guidance with inline code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No executable artifacts; guidance focuses on analytics API usage, consent, retention, rate limits, and credential handling.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
