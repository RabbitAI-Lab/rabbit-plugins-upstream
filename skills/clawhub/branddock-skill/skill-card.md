## Description:

Work on-brand with Branddock, the brand memory and brand check for AI; use this skill whenever creating, rewriting, or reviewing content for a Branddock brand, so the agent fetches real brand context first, writes with it, scores every output with the F-VAL brand check, and leaves publishing to the human.

This skill is ready for commercial/non-commercial use.

## Publisher:

[erikjager55](https://clawhub.ai/user/erikjager55)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing, brand, and content teams using Branddock use this skill to help agents retrieve brand context, draft or rewrite brand-aligned content, score outputs against F-VAL, and keep final publishing approval with a human.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Branddock access can expose brand context, drafts, or workspace data through the configured connector or API.

Mitigation: Install this skill only for Branddock workflows, review connector permissions, and avoid placing API keys directly in chats unless the client handles secrets safely.

Risk: Branddock generation tools can consume credits and may produce drafts that still need brand or business review.

Mitigation: Review credit-consuming actions before approving them, and treat all generated content as proposals requiring human approval.

Risk: If Branddock access is unavailable, an agent could otherwise produce unsupported brand claims.

Mitigation: Reconnect the connector or use a valid workspace-locked API key; do not improvise brand facts without fetched Branddock context.

## Reference(s):

- [Branddock MCP connector](https://branddock.app/mcp)
- [Branddock REST API](https://branddock.app/api/v1)
- [Brand context endpoint](https://branddock.app/api/v1/brand-context)
- [Brand scoring endpoint](https://branddock.app/api/v1/score)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and plain text with optional inline shell commands or API-call examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should include the Branddock score when content is scored and should leave publishing, scheduling, or sending to the human.]

## Skill Version(s):

1.1.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
