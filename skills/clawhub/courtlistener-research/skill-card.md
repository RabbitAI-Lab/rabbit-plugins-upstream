## Description:

Researches public US legal opinions, courts, and judicial people through CourtListener via the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and legal researchers use this skill to search public CourtListener opinions, browse courts, and look up public judicial-person records as initial research leads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: CourtListener search terms and the Crawlora API key are sent to Crawlora.

Mitigation: Install and use only when that disclosure is acceptable, and keep the API key in the CRAWLORA_API_KEY environment variable.

Risk: Returned legal data may be incomplete or unsuitable as a final legal conclusion.

Mitigation: Treat results as research leads and verify important conclusions against the underlying opinions and applicable jurisdictional law.

## Reference(s):

- [courtlistener-research endpoint reference](reference/endpoints.md)
- [ClawHub courtlistener-research skill page](https://clawhub.ai/crawlora-org/skills/courtlistener-research)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands that return JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and uses documented GET-only CourtListener routes.]

## Skill Version(s):

1.0.10 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
