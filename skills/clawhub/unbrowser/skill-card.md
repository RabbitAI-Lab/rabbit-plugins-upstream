## Description:

Cheap first-pass web discovery without launching Chrome - fetch SSR pages, run bounded JS, find routes/forms/API endpoints, extract structured data, and detect bot-wall or browser-only escalation points.

This skill is ready for commercial/non-commercial use.

## Publisher:

[protostatis](https://clawhub.ai/user/protostatis)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill for low-cost first-pass browsing of public web pages, SSR/static sites, search results, route/form/API discovery, structured extraction, and deciding when a full managed browser is required.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cookies supplied to the skill can act as account credentials.

Mitigation: Treat cookies as sensitive credentials, scope them to the authorized host, clear them after authenticated use, and close the session before unrelated work.

Risk: Authenticated actions could change user account state.

Mitigation: Require explicit user approval before posts, purchases, deletes, transfers, settings changes, or other state-changing actions.

Risk: Challenge-cookie solving can expose browser cookies if bound or routed too broadly.

Mitigation: Keep cookie solving local and host-scoped, use explicit allowlists for private or internal targets, and do not expose unauthenticated solver endpoints publicly.

Risk: Page JavaScript and DOM content are untrusted.

Mitigation: Use eval only for diagnostic or extraction code written by the agent, and never execute strings extracted from a page.

## Reference(s):

- [unbrowser upstream repository](https://github.com/protostatis/unbrowser)
- [unbrowser ClawHub release](https://clawhub.ai/protostatis/skills/unbrowser)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell, JSON-RPC, and Python examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes host-scoped cookie handling, session isolation, and managed-browser escalation guidance.]

## Skill Version(s):

0.0.21 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
