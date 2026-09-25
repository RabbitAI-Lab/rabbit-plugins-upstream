## Description:

Figma API integration with managed OAuth for reading design files, nodes, version history, comments, reactions, rendered node images, and published design-system assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[maton](https://clawhub.ai/user/maton)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, designers, and agents use this skill to inspect Figma designs, export node images, manage comments, and audit design-system components through an authenticated Maton connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authorizing the Maton connection grants the skill access to Figma files available to the connected account.

Mitigation: Use OAuth, select the least privilege scope available, and connect only an account whose Figma access matches the task.

Risk: Write operations, new connections, hosted functions, triggers, destinations, and --exec watches can change resources or act unattended.

Mitigation: Keep routine work read-only and require explicit user approval for the exact write, connection, automation, or watch execution before running it.

Risk: Stored OAuth connections and optional automation can forward or expose business data if configured too broadly.

Mitigation: Limit outputs to fields needed for the task and treat hosted functions, triggers, and destinations as persistent automation requiring separate review.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/maton/skills/figma)
- [Maton Publisher Profile](https://clawhub.ai/user/maton)
- [Maton Homepage](https://maton.ai)
- [Figma REST API Introduction](https://developers.figma.com/docs/rest-api/)
- [Figma File Endpoints](https://developers.figma.com/docs/rest-api/file-endpoints/)
- [Figma Comment Endpoints](https://developers.figma.com/docs/rest-api/comments-endpoints/)
- [Figma Component and Style Endpoints](https://developers.figma.com/docs/rest-api/component-endpoints/)
- [Figma Rate Limits](https://developers.figma.com/docs/rest-api/rate-limits/)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, code snippets, API paths, and concise guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include authenticated Figma API call guidance and must keep write operations, new connections, hosted functions, triggers, and watch execution behind explicit user approval.]

## Skill Version(s):

1.2.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
