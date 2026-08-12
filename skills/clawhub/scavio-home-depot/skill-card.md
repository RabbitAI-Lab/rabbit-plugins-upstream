## Description:

Search Home Depot, pull full item detail and page through review bodies as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to search Home Depot listings, retrieve item details, monitor pricing and promotions, enrich product catalogs, and page through product reviews using Scavio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires access to a Scavio API key.

Mitigation: Provide SCAVIO_API_KEY only in environments where the agent is authorized to use Scavio, and rotate the key if it is exposed.

Risk: Home Depot searches, product lookups, and review pages consume paid Scavio credits.

Mitigation: Set explicit paging and spending limits before broad searches or review mining.

Risk: Requests beyond valid result pages can still consume credits.

Mitigation: Stop review pagination at total_pages and cap search pagination before looping.

## Reference(s):

- [Scavio Home Depot Search Documentation](https://scavio.dev/docs/home-depot-search)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits)
- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/scavio-home-depot)

## Skill Output:

**Output Type(s):** [guidance, code, shell commands, configuration, JSON]

**Output Format:** [Markdown guidance with JSON API responses and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; Home Depot endpoints cost 2 Scavio credits per request.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
