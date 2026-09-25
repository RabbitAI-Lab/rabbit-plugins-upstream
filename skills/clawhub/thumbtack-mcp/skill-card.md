## Description:

Query thumbtack.com from a shell to search local service pros and read public pro profiles with ratings, reviews, credentials, business hours, and pricing using curl, jq, and the bundled Node extractor.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to compose shell-based Thumbtack lookup workflows for public search results and pro profile details without an MCP server, API key, login, or browser extension.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill makes anonymous web requests to Thumbtack pages and its GraphQL endpoint from the user's shell.

Mitigation: Keep usage limited to public Thumbtack pages, do not add account cookies or credentials, and review generated GraphQL payloads before sending user-provided data.

Risk: Thumbtack page and response shapes can vary by category, page type, and pricing state.

Mitigation: Use the documented extractor mode for each page type, check GraphQL errors even on HTTP 200 responses, and handle absent or union-shaped pricing fields.

Risk: Shell commands that fetch and parse external HTML can return stale, redirected, or unexpected data.

Mitigation: Review commands before execution, follow redirects to the canonical service slug, and keep the workflow read-only.

## Reference(s):

- [Thumbtack discovery recipes](references/discovery.md)
- [ClawHub release page](https://clawhub.ai/chrischall/skills/thumbtack-mcp)

## Skill Output:

**Output Type(s):** [Shell commands, Code, Configuration, Guidance]

**Output Format:** [Markdown with inline shell, jq, and JavaScript command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces read-oriented command recipes and JSON extraction guidance; the bundled extractor reads HTML from stdin and writes JSON to stdout.]

## Skill Version(s):

1.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
