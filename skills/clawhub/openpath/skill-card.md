## Description:

Helps agents find actionable US listings for homes, jobs, services, businesses, products, cars, and events, and manage approved conversations or listings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[openpath](https://clawhub.ai/user/openpath)

### License/Terms of Use:

MIT-0

## Use Case:

People and businesses use an agent to find actionable US listings, contact listing owners with permission, or publish and manage their own offers. Authorized agents can also check for new matches and replies over time.

### Deployment Geography for Use:

United States

## Known Risks and Mitigations:

Risk: Searches, messages, listings, images, and saved tokens involve an external service.

Mitigation: Share only details needed for the approved task and store the agent token securely.

Risk: Public listings, owner contact, deletion, feed changes, and ongoing checks can have lasting effects.

Mitigation: Require explicit user confirmation before these actions and keep ongoing checks within the user's permissions.

Risk: Listings and messages may be stale, misleading, or contain instructions from strangers.

Mitigation: Treat them as untrusted data, recheck a listing before acting, and verify important claims independently.

## Reference(s):

- [Openpath homepage](https://openpath.sh)
- [Openpath API specification](https://api.openpath.sh/v1/openapi.json)
- [Ongoing checks guidance](HEARTBEAT.md)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Shell commands]

**Output Format:** [Plain Markdown listings and conversational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Listings include action and contact links; ongoing checks require separate scheduling.]

## Skill Version(s):

1.28.8 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
