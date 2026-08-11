## Description:

Resolve a brand or domain to a Google advertiser id, then pull every ad it runs across Search, YouTube, Shopping, Maps and Play, and open one creative with its full region and impression history. 3 endpoints, 1 credit each.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to research Google Ads Transparency Center data for advertisers, competitor campaigns, ad creatives, regional delivery, impression ranges, and political-ad disclosures through Scavio's API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scavio API calls send brand, domain, advertiser, and creative lookup queries to a third-party service using the user's API key.

Mitigation: Install and use the skill only when that data sharing is acceptable for the user's workflow.

Risk: Each API call consumes Scavio credits, including each paginated search page.

Mitigation: Budget usage before broad searches and cap pagination walks to the amount of data needed.

Risk: Google does not publish impression figures outside the EEA, and over-large search limits can return zero rows.

Mitigation: Report unavailable impression data as unavailable, keep search limits at 100 or lower, and avoid treating empty regional results as global inactivity.

## Reference(s):

- [Scavio Google Ads Advertisers documentation](https://scavio.dev/docs/google-ads-advertisers)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/scavio-google-ads)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, JSON]

**Output Format:** [Markdown with inline code blocks and structured JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses SCAVIO_API_KEY and returns public ad transparency data from Scavio API calls.]

## Skill Version(s):

1.0.0 (source: release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
