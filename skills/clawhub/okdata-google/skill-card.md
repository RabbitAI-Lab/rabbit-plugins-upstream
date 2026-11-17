## Description:

Queries public Google Ads Transparency Center advertiser and ad data through okdata.

This skill is ready for commercial/non-commercial use.

## Publisher:

[conn-ho](https://clawhub.ai/user/conn-ho)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use this skill to find advertisers in the Google Ads Transparency Center and retrieve their ads by advertiser ID or website domain through okdata.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release security review was partial, and the external service URL was flagged for review.

Mitigation: Confirm that api.okdata.online is trusted for your use case; the benign verdict does not establish that all related material was reviewed.

Risk: Paid endpoint calls can incur charges, including calls that reach the data source but fail or return no results.

Mitigation: State the endpoint and maximum cost before the first paid call, cap calls with max_price, and request additional pages only when needed.

Risk: An exposed API key could be misused.

Mitigation: Keep the key in OKDATA_API_KEY or the client's configuration; never print it or place it in a URL.

## Reference(s):

- [Google Ads Transparency API documentation](https://okdata.online/apis/google/?src=skill-okdata-google)
- [okdata agent setup guide](https://okdata.online/agents.md)

## Skill Output:

**Output Type(s):** [API Calls, Text]

**Output Format:** [Text containing Google Ads Transparency advertiser and ad results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One page per call; additional pages require separate paid calls.]

## Skill Version(s):

0.2.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
