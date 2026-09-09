## Description:

Search Zillow listings for sale, for rent or sold, pull one property in full with Zestimate and tax history, and read a real-estate agent's profile and reviews.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and real-estate analysts use this skill to search Zillow sale, rental, and sold listings, retrieve full property records, and read agent profiles for comparables, rent-vs-buy analysis, or market monitoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Zillow search locations, property URLs or IDs, agent screen names, and the Scavio API key are sent to Scavio during use.

Mitigation: Use the skill for user-directed property lookups, keep the API key in an environment variable or secret store, and avoid entering unrelated sensitive personal information into search parameters.

Risk: Each API call consumes Scavio credits, including calls that return empty results or parameter errors.

Mitigation: Confirm parameters before calling, use city names when filters or sorts are applied, and relax overly narrow searches instead of retrying identical requests.

Risk: Real-estate data can be misread if estimates, listings, and reviews are presented without context.

Mitigation: Label Zestimate values as Zillow estimates rather than appraisals or sale prices, and keep agent reviews separate from property information.

## Reference(s):

- [Scavio Zillow Search Documentation](https://scavio.dev/docs/zillow-search?utm_source=agent-skills&utm_medium=skill&utm_campaign=zillow-property-data)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=zillow-property-data)
- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/zillow-property-data)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with JSON API responses and inline shell or code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; each Zillow endpoint call consumes one Scavio credit.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
