## Description:

Helps agents search the web, images, news, and videos with Brave Search through a user-authorized Maton connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users use this skill to find web pages, images, news, and videos with Brave Search. A Maton account and an approved Brave Search connection are required.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search requests access Brave Search through a Maton connection authorized by the user.

Mitigation: Confirm authorization before creating a connection; begin with ordinary search calls and keep credentials private.

Risk: Optional automation can send data to a third-party trigger destination.

Mitigation: Approve automation explicitly and use only destinations whose host the user named and trusts.

Risk: Location headers can disclose location information during a search.

Mitigation: Send location headers only when needed and approved by the user.

## Reference(s):

- [Brave Search skill release](https://clawhub.ai/byungkyu/skills/brave-search-api)
- [Maton](https://maton.ai)
- [Brave Search API documentation](https://api-dashboard.search.brave.com/documentation)
- [Maton documentation](https://docs.maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Text or Markdown with search results and optional command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Searches require network access and a user-authorized Maton connection.]

## Skill Version(s):

1.2.7 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
