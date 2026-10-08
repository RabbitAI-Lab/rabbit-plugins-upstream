## Description:

Looks up public Instagram profiles, posts, and Reels through the Crawlora API and returns structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and marketers use this skill to research public Instagram profiles, individual posts, and Reels for social audits or influencer vetting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Public lookup identifiers and request data are sent to the third-party Crawlora service.

Mitigation: Use only for public lookups and avoid sensitive or private identifiers in routes and queries.

Risk: The Crawlora API key is a credential needed for requests.

Mitigation: Keep CRAWLORA_API_KEY private; do not hardcode, expose, or commit it.

Risk: Use of Instagram public data may be subject to service terms.

Mitigation: Review Crawlora's and Instagram's terms before use.

## Reference(s):

- [Instagram endpoint reference](artifact/reference/endpoints.md)
- [Instagram Research release](https://clawhub.ai/crawlora-org/skills/instagram-research)

## Skill Output:

**Output Type(s):** [JSON, Text, Shell commands]

**Output Format:** [JSON or text with shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Public profile, post, and Reels data; Reels pagination uses a cursor.]

## Skill Version(s):

1.0.18 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
