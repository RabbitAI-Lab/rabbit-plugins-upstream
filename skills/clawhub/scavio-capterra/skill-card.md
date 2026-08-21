## Description:

Search Capterra for B2B software, read a full product profile with the complete pricing table and 25 reviews included, and page deeper reviews with per-criterion scores. 3 endpoints, 2 credits each.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, agents, and software research teams use this skill to search Capterra, inspect product profiles, compare alternatives, and analyze review data for B2B software selection and competitive research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses Scavio as an external API provider for Capterra research.

Mitigation: Install only when external Scavio API use is acceptable for the intended research workflow.

Risk: The skill requires SCAVIO_API_KEY and each API request consumes credits.

Mitigation: Keep the API key out of source control and monitor credit usage before making additional product or review requests.

Risk: Incorrect review pagination or hand-written review slugs can return duplicate page-one data while still consuming credits.

Mitigation: Use the returned reviews_url or exact slug, avoid requesting reviews page 1, and keep review pagination within the documented page cap.

## Reference(s):

- [Scavio Capterra Search Documentation](https://scavio.dev/docs/capterra-search)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits)
- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/scavio-capterra)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with shell commands, code examples, and structured JSON API response descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY. Scavio API requests consume credits, with each Capterra endpoint documented as 2 credits.]

## Skill Version(s):

1.0.3 (source: server release evidence and target metadata; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
