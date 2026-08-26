## Description:

Turn a novel chapter, web-novel excerpt, or story script into narrated vertical short video scenes with illustrated shots that keep every character looking the same from beat to beat.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, authors, marketers, and agent users use this skill to turn story text into ordered narrated vertical promo scenes for story channels, book trailers, web-novel promotion, chapter recaps, and faceless storytelling accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores shared local Beatra authorization state for paid media tools.

Mitigation: Install only if that authorization is acceptable, keep the Device Token private, and revoke the Beatra agent connection or uninstall the package when it is no longer needed.

Risk: The bundled client silently auto-updates installed package code by default.

Mitigation: Run `python3 scripts/mcp_client.py update --auto off` after installation if manual update review is preferred, and use `python3 scripts/mcp_client.py update --check` to inspect available updates.

Risk: Paid image, speech, and video requests can consume Beatra credits.

Mitigation: Review live price cards, require explicit approval before paid calls, keep stable request IDs, and retry uncertain submissions only with the same frozen request payload.

## Reference(s):

- [Novel Promo Workflow](references/workflow.md)
- [Installation and Authentication](references/installation-and-auth.md)
- [Installation Registration](references/installation-registration.md)
- [Tasks and Results](references/tasks-and-results.md)
- [Billing, Errors, and Recovery](references/billing-errors-and-recovery.md)
- [MCP Connection](references/mcp-connection.md)
- [Automatic Updates and Safety](references/automatic-updates-and-safety.md)
- [Uninstall and Disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON payload examples and shell command snippets; completed remote tasks return media artifact details.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Plans four to six narrated vertical scenes by default and reports task status, resolved model, dimensions, duration, usage, and billing fields returned by Beatra.]

## Skill Version(s):

0.1.4 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
