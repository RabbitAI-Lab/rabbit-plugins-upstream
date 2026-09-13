## Description:

Reddit Search helps agents search Reddit posts, comments, users, and subreddits through Xpoz MCP without requiring Reddit API credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[atyachin](https://clawhub.ai/user/atyachin)

### License/Terms of Use:


## Use Case:

Developers, researchers, and external users use this skill to find Reddit discussions, discover communities, look up users, and collect search results or exportable datasets through Xpoz MCP.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Searches and exports are sent through Xpoz MCP as a third-party Reddit search provider.

Mitigation: Install and use the skill only when the user accepts Xpoz handling the submitted queries and returned export workflow.

Risk: The skill depends on the mcporter npm package without a pinned version in the provided metadata.

Mitigation: Prefer a reviewed or pinned mcporter version where possible and run it with normal least-privilege safeguards.

## Reference(s):

- [Reddit Search on ClawHub](https://clawhub.ai/atyachin/skills/reddit-api)
- [Xpoz](https://xpoz.ai)
- [xpoz-setup Skill](https://clawhub.ai/skills/xpoz-setup)
- [xpoz-social-search Skill](https://clawhub.ai/skills/xpoz-social-search)
- [expert-finder Skill](https://clawhub.ai/skills/expert-finder)
- [social-sentiment Skill](https://clawhub.ai/skills/social-sentiment)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May initiate Xpoz MCP searches that return Reddit search results, operation status, and CSV export URLs.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
