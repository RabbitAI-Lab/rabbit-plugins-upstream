## Description:

Search Capterra for B2B software, read a full product profile with the complete pricing table and 25 reviews included, and page deeper reviews with per-criterion scores.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search Capterra products, retrieve product profiles, compare pricing and alternatives, and analyze reviews for software selection, competitive intelligence, and voice-of-customer research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the skill sends Capterra search terms, product IDs, review URLs, and the Scavio API key to Scavio's API.

Mitigation: Install and run it only where sharing those inputs with Scavio is acceptable, and provide the API key through a secret or environment variable.

Risk: Each endpoint call is billed in credits, and duplicate review calls or invalid pagination can waste credits.

Mitigation: Use the documented workflow: avoid page 1 review calls, keep review pages within the page 100 cap, and pass the returned reviews_url or exact slug.

## Reference(s):

- [Scavio Capterra Search API Documentation](https://scavio.dev/docs/capterra-search?utm_source=agent-skills&utm_medium=skill&utm_campaign=capterra-reviews-api)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=capterra-reviews-api)
- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/capterra-reviews-api)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, API Calls, Configuration]

**Output Format:** [Markdown with JSON request shapes and Python, JavaScript, and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; Scavio API responses are structured JSON envelopes with data, response_time, credits_used, and credits_remaining.]

## Skill Version(s):

1.0.3 (source: server release metadata; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
