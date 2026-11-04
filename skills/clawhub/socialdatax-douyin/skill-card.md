## Description:

This skill retrieves and helps analyze Douyin trends, posts, comments, creator profiles, and series through SocialDataX.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, analysts, and agents use this skill to retrieve Douyin trends, search posts and creators, inspect content and comments, and summarize creator activity through SocialDataX.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on third-party CLI software and a hosted data service.

Mitigation: Use a reviewed fixed CLI version where possible and provide only the needed API key.

Risk: Lookup inputs are sent to SocialDataX, and data calls may consume service credits.

Mitigation: Remove unrelated private text from lookup inputs and check service credit costs.

Risk: Local credential settings could expose the API key if committed to a repository.

Mitigation: Keep local credential settings out of version control.

## Reference(s):


## Skill Output:

**Output Type(s):** [API Calls, JSON data, Analysis]

**Output Format:** [Structured JSON data with concise natural-language summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only research across Douyin trends, posts, comments, creator profiles, and series.]

## Skill Version(s):

0.1.23 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
