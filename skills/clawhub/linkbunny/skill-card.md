## Description:

Builds backlinks by linking backlinks to other sites. Use when user says "build backlinks" or "linkbunny"

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkbunny](https://clawhub.ai/user/linkbunny)

### License/Terms of Use:

MIT-0

## Use Case:

Site owners and their authorized agents use LinkBunny to manage backlink-exchange profiles, review matched link requests, and report or reject placements. The agent must get owner approval for account, site, publication, reporting, and rejection actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The check-in curl example can expose the account token through command arguments.

Mitigation: Review the credential example and pass the token through standard input with curl --config -; rotate the token if it may have been captured in accessible logs.

Risk: Using the paid service shares registered site and placement details, and backlink publication can affect the owner's site.

Mitigation: Retain the documented approval gates, register only authorized sites, and obtain approval before publication, reporting, or rejection.

## Reference(s):

- [LinkBunny agent documentation](https://getlinkbunny.com/docs/agents?ref=clawhub)
- [LinkBunny skill source](https://getlinkbunny.com/skill.md)
- [curl configuration options](https://curl.se/docs/manpage.html#-K)
- [LinkBunny ClawHub release](https://clawhub.ai/linkbunny/skills/linkbunny)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands and API request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes owner-approval gates and token-handling guidance; does not independently verify reported placements.]

## Skill Version(s):

1.2.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
