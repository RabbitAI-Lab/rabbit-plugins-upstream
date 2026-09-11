## Description:

Search Capterra for B2B software, read a full product profile with the complete pricing table and 25 reviews included, and page deeper reviews with per-criterion scores.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search Capterra software listings, inspect product pricing and review data, compare alternatives, and support B2B software selection or competitive research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API requests are sent to Scavio and consume credits.

Mitigation: Confirm the user's intent before making calls, avoid duplicate review-page requests, and track credit use in returned responses.

Risk: SCAVIO_API_KEY is required for use.

Mitigation: Keep the key in an environment variable or secret store and do not place real keys in source code or shared prompts.

Risk: Optional SDK installation adds package supply-chain exposure.

Mitigation: Use direct HTTPS requests when possible, or install SDKs in a clean virtual environment after reviewing package provenance.

Risk: Incorrect Capterra review slugs or page numbers can return duplicate page-one data while still being billed.

Mitigation: Use the API-returned reviews_url or exact slug, skip page 1 because product profiles already include the latest 25 reviews, and never request pages above 100.

## Reference(s):

- [Scavio Capterra API documentation](https://scavio.dev/docs/capterra-search?utm_source=agent-skills&utm_medium=skill&utm_campaign=capterra-reviews-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=capterra-reviews-api)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/capterra-reviews-api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON API examples and shell setup commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides agents to call Scavio HTTPS endpoints that return structured JSON and consume API credits.]

## Skill Version(s):

1.0.4 (source: server release metadata; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
