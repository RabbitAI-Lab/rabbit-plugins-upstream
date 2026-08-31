## Description:

Turn product photos into verified Bring! list items via MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[schnueck](https://clawhub.ai/user/schnueck)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to identify products from photos, classify them against the Bring! catalog, and add verified items to configured shopping lists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MCP server requires Bring account credentials and can modify configured shopping lists.

Mitigation: Store the password in a secret store and keep BRING_ALLOWED_LISTS limited to the lists the agent should write.

Risk: Ambiguous photos or weak catalog matches could lead to adding the wrong item.

Mitigation: Treat unclear classification as a no-write result and ask for clarification or present candidates before writing.

Risk: Supplied local image paths may be read and uploaded to Bring for the requested item.

Mitigation: Attach photos only from permitted local paths and avoid exposing image paths or photo bytes in conversation output.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/schnueck/skills/bring-photo-mcp)
- [Publisher profile](https://clawhub.ai/user/schnueck)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, API calls]

**Output Format:** [Markdown guidance with MCP tool calls and concise write-status summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports non-sensitive verification evidence and avoids exposing credentials, list IDs, image paths, or photo bytes.]

## Skill Version(s):

1.0.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
