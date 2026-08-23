## Description:

Search Airbnb stays with the full discount ledger, pull one listing with its complete amenity list and rating breakdown, and page through real review bodies.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search Airbnb listings, compare stay pricing, inspect listing details, and review guest feedback through Scavio's structured API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Airbnb search, listing, and review requests to Scavio using SCAVIO_API_KEY.

Mitigation: Store SCAVIO_API_KEY in an environment variable or secret store and avoid putting it in source code, logs, or shared transcripts.

Risk: Each endpoint call consumes one Scavio credit, including paginated search or review requests.

Mitigation: Confirm the intended search scope before making calls and bound pagination with explicit page, cursor, limit, and offset choices.

Risk: Responses may include personal data such as reviewer names, reviewer photos, reviewer locations, and host profile details.

Mitigation: Summarize review and host information for the user's task and avoid profiling individual people.

Risk: Dateless searches can return Airbnb-selected date windows and A/B-tested prices that may not match the user's intended stay.

Mitigation: Send check_in, check_out, and currency explicitly for dated price comparisons and do not quote prices when dates_are_defaulted is true.

## Reference(s):

- [Scavio Airbnb Search Documentation](https://scavio.dev/docs/airbnb-search)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits)
- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/scavio-airbnb)

## Skill Output:

**Output Type(s):** [guidance, code, shell commands, configuration, JSON]

**Output Format:** [Markdown guidance with inline code examples and JSON response descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY and uses Scavio API calls that consume one credit per endpoint request.]

## Skill Version(s):

1.0.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
