## Description:

Analyzes Weibo comments and replies to surface audience feedback, sentiment themes, objections, pain points, and discussion summaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Social media analysts and teams use this skill to review Weibo post comments and replies, group observed themes, and summarize audience feedback, objections, and pain points.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The integration uses an API key, and unbounded comment retrieval may incur usage-based costs.

Mitigation: Keep SOCIALDATAX_API_KEY in the environment, set --pages or --max-items to bound retrieval, and consult the provider's service documentation.

Risk: The documented @latest CLI reference can change between runs.

Mitigation: Use a reviewed, fixed CLI version for repeatable runs.

## Reference(s):

- [SocialDataX service documentation](https://socialdatax.com/docs)

## Skill Output:

**Output Type(s):** [JSON, Text summaries, Analysis]

**Output Format:** [JSON comment and reply data with concise text summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Summaries group comments by observed themes and indicate whether retrieval covered one page or multiple pages.]

## Skill Version(s):

0.1.21 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
