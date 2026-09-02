## Description:

Search Google Hotels for a destination and dates, then fetch per-property vendor pricing and full details as structured JSON, with price, rating, class, and amenity filters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to search Google Hotels through Scavio for destinations and stay dates, compare lodging by price, rating, class, and amenities, and retrieve property details with vendor pricing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Hotel searches, dates, and selected property detail requests are sent to Scavio.

Mitigation: Avoid sending sensitive travel details unless the user accepts that the request will be processed by Scavio.

Risk: Each endpoint call consumes Scavio credits and exhausted balances return billing-related errors.

Mitigation: Confirm search scope before making repeated calls, handle 402 responses, and surface credit or billing errors to the user.

Risk: The skill requires SCAVIO_API_KEY for authenticated API access.

Mitigation: Keep SCAVIO_API_KEY in an environment variable or secret store and do not commit it to source code.

## Reference(s):

- [Scavio Google Hotels API documentation](https://scavio.dev/docs/google-hotels)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/google-hotels-api)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Code, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON API responses and bash or Python examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; API calls use Scavio credits and may return lodging results, pricing, ratings, amenities, and booking-source details.]

## Skill Version(s):

1.0.1 (source: server release evidence; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
