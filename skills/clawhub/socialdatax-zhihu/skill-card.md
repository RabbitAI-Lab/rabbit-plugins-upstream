## Description:

Provides read-only Zhihu research for hot lists, content search and details, comment analysis, creator profiles, and article lists through SocialDataX.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

People researching Zhihu trends, questions, answers, articles, videos, discussions, or creators can use this skill to retrieve read-only information for analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Lookup inputs and the API key are sent to SocialDataX, and requests—especially across many pages—may incur service charges.

Mitigation: Avoid sending private information, limit page requests, and review applicable service charges before use.

Risk: The external executable was not run or fully audited.

Mitigation: Review the package and use a vetted, fixed CLI version rather than an unpinned latest release.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-zhihu)
- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [JSON, Research guidance]

**Output Format:** [Pretty-printed JSON research results from the CLI or structured results from equivalent MCP tools]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Zhihu data covering hot lists, content, comments and replies, creator profiles, and creator article lists.]

## Skill Version(s):

0.1.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
