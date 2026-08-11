## Description:

Helps agents retrieve and analyze Weibo hot searches, post search results, post details, comments, replies, engagement lists, creator profiles, and creator post lists through SocialDataX.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent for read-only Weibo research, including trend review, post discovery, comment analysis, engagement review, and creator profile or post-list lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow sends requests to SocialDataX using SOCIALDATAX_API_KEY and makes network calls to a third-party service.

Mitigation: Install and use the skill only after reviewing the SocialDataX package, service terms, and whether the API key and social-data workflow fit the deployment's data-handling requirements.

Risk: Incorrect credentials, malformed Weibo IDs or URLs, or account balance issues can prevent successful data retrieval.

Mitigation: Check SOCIALDATAX_API_KEY, parameters, and returned error messages; do not repeatedly retry insufficient-balance errors before the user resolves the balance condition.

## Reference(s):

- [SocialDataX API access and documentation](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-weibo)
- [Publisher profile](https://clawhub.ai/user/devinchen2014)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and guidance for read-only SocialDataX Weibo data calls]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SOCIALDATAX_API_KEY plus node and npm; API responses may include Weibo data returned by SocialDataX.]

## Skill Version(s):

0.1.17 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
