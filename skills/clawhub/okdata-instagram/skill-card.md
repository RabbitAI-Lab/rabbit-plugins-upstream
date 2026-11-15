## Description:

Provides agents with access to public Instagram account, post, comment, hashtag, and Reel transcript data through the okdata API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[conn-ho](https://clawhub.ai/user/conn-ho)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents can use this skill to look up public Instagram accounts, posts, comments, hashtags, and Reel transcripts. The API requires an OKDATA_API_KEY and charges per successful request.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Instagram lookup requests to an external, paid API, and the scan had incomplete reference checks.

Mitigation: Use the service only if you trust and need it, review expected per-call costs and set a max_price before requests, and keep OKDATA_API_KEY in an environment variable rather than sharing it in chat.

## Reference(s):

- [okdata Instagram API documentation](https://okdata.online/zh/apis/instagram/)

## Skill Output:

**Output Type(s):** [Text, Structured data, Analysis]

**Output Format:** [Text responses and structured Instagram data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results cover available public Instagram data; API requests are billed per call.]

## Skill Version(s):

0.1.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
