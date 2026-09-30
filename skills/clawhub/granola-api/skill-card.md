## Description:

Helps agents search Granola meetings, summarize notes, identify action items, and retrieve transcripts through a user-authorized Maton connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

People using Granola meeting notes can ask an agent to find meetings, summarize discussions, identify action items, and retrieve available transcripts. Access requires a Maton account and an authorized Granola connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Meeting notes and transcripts may contain private personal or business information.

Mitigation: Prefer OAuth, retrieve only the meetings needed, and avoid forwarding or exposing raw meeting content.

Risk: Hosted functions, triggers, or destinations could send meeting data beyond the intended task.

Mitigation: Require user approval after reviewing the exact automation scope and destination before creating or using them.

## Reference(s):

- [ClawHub Granola skill](https://clawhub.ai/byungkyu/skills/granola-api)
- [Granola MCP documentation](https://docs.granola.ai/help-center/sharing/integrations/mcp)
- [Maton homepage](https://maton.ai)
- [Maton documentation](https://docs.maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Natural-language answers and Markdown, with commands when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may contain private meeting notes or transcripts; transcript access depends on the user's Granola plan.]

## Skill Version(s):

1.2.5 (source: ClawHub release; artifact metadata: 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
