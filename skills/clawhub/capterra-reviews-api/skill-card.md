## Description:

Search Capterra for B2B software, read a full product profile with the complete pricing table and 25 reviews included, and page deeper reviews with per-criterion scores.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and research agents use this skill to search Capterra, compare B2B software products, inspect pricing and profile details, and mine review data for buyer research, competitive intelligence, and voice-of-customer analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses an external paid API service and each documented endpoint call consumes credits.

Mitigation: Confirm Scavio usage is acceptable before installation, monitor credit consumption, and avoid redundant review-page calls described in the guardrails.

Risk: The skill requires SCAVIO_API_KEY for authenticated API calls.

Mitigation: Store SCAVIO_API_KEY in an environment variable or secret store and keep it out of source code.

Risk: Incorrect review pagination or hand-written slugs can return duplicate page-one data while still being billed.

Mitigation: Use the returned reviews_url or exact slug, keep review pages within the documented 1-100 range, and check for duplicate rows.

Risk: Capterra product, pricing, rating, and review details can be misleading if guessed or fabricated.

Mitigation: Return only data from Scavio API responses and report unavailable fields rather than inferring missing values.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/capterra-reviews-api)
- [Scavio Capterra Search Documentation](https://scavio.dev/docs/capterra-search)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON API response descriptions and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces agent guidance for authenticated Scavio API calls; API responses use structured JSON envelopes.]

## Skill Version(s):

1.0.2 (source: server release evidence; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
