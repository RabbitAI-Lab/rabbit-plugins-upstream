## Description:

Turn product photos into verified Bring! list items via MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[schnueck](https://clawhub.ai/user/schnueck)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn product photos into verified Bring! shopping-list entries through the Bring Photo MCP server, including catalog classification, duplicate handling, and photo/list operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MCP server uses Bring account credentials and can write to configured shopping lists.

Mitigation: Trust the bring-photo-mcp package before installation, store BRING_PASSWORD only in a secret store, and set BRING_ALLOWED_LISTS narrowly.

Risk: Photo recognition or catalog classification can be ambiguous and may otherwise add the wrong item.

Mitigation: Ask for clarification or avoid writing when the photo is unreadable, classification confidence is insufficient, or duplicate policy would overwrite an ambiguous item.

Risk: Shopping-list operations can expose sensitive account, list, item, or image details in conversation output.

Mitigation: Report only requested operation status and non-sensitive verification evidence; do not reveal credentials, list IDs, item-detail UUIDs, image paths, or photo bytes.

## Reference(s):

- [Bring Photo MCP on ClawHub](https://clawhub.ai/schnueck/skills/bring-photo-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Concise text or Markdown responses with per-list write status and non-sensitive verification evidence.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses configured Bring credentials and allowed-list scope; omits credentials, list IDs, UUIDs, image paths, and photo bytes.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
