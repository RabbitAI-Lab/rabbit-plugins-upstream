## Description:

Guides agents through using curl and parser recipes to access Artsonia student portfolios, comments, fans, feedback, profile data, downloads, and selected account actions without running the Artsonia MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, parents, and authorized account operators use this skill to retrieve Artsonia portfolio data and run reviewed curl workflows for session-based reads, downloads, and selected account updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles Artsonia credentials and persistent session cookies.

Mitigation: Read passwords from stdin or a secret manager, protect the cookie jar, and rotate credentials if exposed.

Risk: The workflows can access student portfolio data, parent contact data, and unauthenticated private-image download URLs.

Mitigation: Use only with accounts and artwork you are authorized to access; avoid bulk downloads and the no-auth image path unless explicitly approved.

Risk: Some recipes perform real POST actions such as comments, fan invitations, feedback marking, and profile notification changes.

Mitigation: Require explicit confirmation before every POST, re-read the affected page afterward, and treat redirects as insufficient proof of success.

## Reference(s):

- [Endpoint recipes](references/endpoints.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes credential handling guidance, session-cookie handling, endpoint recipes, parser invocation examples, and post-write verification steps.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
