## Description:

here.now lets agents publish websites and files to live URLs in seconds.

This skill is ready for commercial/non-commercial use.

## Publisher:

[adamludwin](https://clawhub.ai/user/adamludwin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, agents, and teams use here.now to publish websites and static files, manage site access, work with custom domains or workspace URLs, and store or share private Drive files through documented shell and API workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can direct agents to persist a here.now API key under ~/.herenow/credentials.

Mitigation: Confirm the user's intent before login persistence and avoid exposing API keys in command arguments, logs, or generated content.

Risk: The skill supports private Drive sharing, mutation, deletes, overwrites, and scoped token creation.

Mitigation: Require explicit user approval for Drive sharing, destructive changes, overwrites, and broad token scopes; prefer narrow prefixes and short token lifetimes.

Risk: The skill can publish selected local files to public or controlled-access URLs.

Mitigation: Review the target path and access mode before publishing, and use restricted or password access when content should not be public.

Risk: The skill can initiate domain purchases, which evidence and artifact behavior describe as final.

Mitigation: Show the quoted purchase and renewal prices and obtain explicit user confirmation before any purchase action.

## Reference(s):

- [here.now documentation](https://here.now/docs)
- [here.now OpenAPI specification](https://here.now/openapi.json)
- [ClawHub skill release](https://clawhub.ai/adamludwin/skills/here-now)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, URLs, and API request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce live site URLs, private Drive guidance, access-control instructions, and configuration steps for here.now credentials or domains.]

## Skill Version(s):

1.32.0 (source: server release evidence and SKILL.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
