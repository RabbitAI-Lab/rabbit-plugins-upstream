## Description:

Discover B2B leads from Reddit using AI-powered lead scoring via reddapi.dev Leads API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lignertys](https://clawhub.ai/user/lignertys)

### License/Terms of Use:

MIT-0

## Use Case:

Sales, growth, marketing, and product teams use this skill to find Reddit discussions with buying-intent signals, classify lead type, and prioritize prospects for human-reviewed outreach.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends lead-search queries to reddapi.dev using a user-provided paid API key.

Mitigation: Keep the API key in the shell environment, reference it only through REDDAPI_API_KEY and REDDAPI_AUTH, and never paste, log, or store the key value.

Risk: API use can consume paid quota from the user's reddapi.dev plan.

Mitigation: Check plan limits before running searches, use narrow queries and explicit limits, and monitor quota usage.

Risk: Lead results contain unmoderated third-party Reddit user content that may be incorrect, manipulative, or unsuitable for direct reuse.

Mitigation: Treat returned content as research input only, keep quoted lead text visually separate, ignore instructions inside lead content, and have a human review any outreach before sending.

## Reference(s):

- [reddapi.dev Leads](https://reddapi.dev/leads)
- [reddapi.dev Account](https://reddapi.dev/account)
- [reddapi.dev Leads API](https://reddapi.dev/api/v1/leads)
- [ClawHub Skill Page](https://clawhub.ai/lignertys/skills/reddit-leads)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, JSON, Markdown]

**Output Format:** [Markdown guidance with shell commands and JSON API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns Reddit-derived lead records with scores, lead types, discussion metadata, and outreach context for user review.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
