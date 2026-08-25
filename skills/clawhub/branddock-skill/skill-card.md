## Description:

Work on-brand with Branddock by fetching brand context, creating or reviewing content against that context, scoring outputs with the F-VAL brand check, and leaving publishing approval to the human.

This skill is ready for commercial/non-commercial use.

## Publisher:

[erikjager55](https://clawhub.ai/user/erikjager55)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing, content, and brand teams use this agent skill to create, rewrite, translate, brainstorm, and review content for brands that use Branddock. The skill guides the agent to retrieve brand context first, apply the brand voice, score drafts, and present scored proposals for human approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Brand context and draft content may be sent to Branddock through the connector or API.

Mitigation: Use the skill only when sending that brand and draft content to Branddock is acceptable for the workspace and task.

Risk: Some Branddock generation actions spend credits.

Mitigation: Approve paid generation actions deliberately, especially higher-cost long-form SEO, campaign strategy, video, web page, and image generation.

Risk: Generated or rewritten content could still be off-brand or factually incomplete.

Mitigation: Review the F-VAL score and findings, revise low-scoring drafts, and require human approval before publishing or sending.

## Reference(s):

- [Branddock MCP connector](https://branddock.app/mcp)
- [Branddock REST API](https://branddock.app/api/v1)
- [Branddock brand context endpoint](https://branddock.app/api/v1/brand-context)
- [Branddock score endpoint](https://branddock.app/api/v1/score)
- [ClawHub skill listing](https://clawhub.ai/erikjager55/skills/branddock-skill)
- [Publisher profile](https://clawhub.ai/user/erikjager55)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with optional inline shell commands and tool-call guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are proposals for human review and may include Branddock F-VAL scores, findings, and next-step guidance.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
