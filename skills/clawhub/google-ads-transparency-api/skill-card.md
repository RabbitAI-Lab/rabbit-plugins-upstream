## Description:

Resolve a brand or domain to a Google advertiser id, then pull every ad it runs across Search, YouTube, Shopping, Maps and Play, and open one creative with its full region and impression history. 3 endpoints, 1 credit each.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and marketing researchers use this skill to resolve Google advertiser identities and retrieve public ad creatives, run dates, regions, surfaces, and impression ranges through the Scavio API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries send ad research targets, domains, advertiser IDs, regions, and filters to Scavio under the user's API key.

Mitigation: Use the skill only for approved research targets and avoid confidential investigations or regulated data unless third-party processing by Scavio is approved.

Risk: Paginated searches consume credits for each request page.

Mitigation: Budget result walks before starting, cap pagination, and keep search limits within documented endpoint ceilings.

Risk: Google reports impression and ad counts as ranges or unavailable values, which can be misread as precise totals.

Mitigation: Report ranges as ranges and explain that unavailable impression data is not zero, especially outside EEA regions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/google-ads-transparency-api)
- [Scavio Google Ads Advertisers documentation](https://scavio.dev/docs/google-ads-advertisers)
- [Scavio rate limits documentation](https://scavio.dev/docs/rate-limits)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON request and response guidance, Python and JavaScript code examples, and shell setup commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; API responses are structured JSON from Scavio and consume credits per request page.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
