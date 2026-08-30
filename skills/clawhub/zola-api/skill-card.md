## Description:

Query or update Zola wedding-planning data straight from a shell with curl against mobile-api.zola.com, including vendors, budget, guests, seating, events and RSVPs, registry, gift tracking, inquiries, and wedding website data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers with authenticated Zola accounts use this skill to inspect and update wedding-planning records through curl and jq command recipes. It is suited to direct API workflows on machines where the Zola MCP server is not installed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a long-lived Zola refresh token and short-lived session tokens that can grant live account access.

Mitigation: Treat both tokens like passwords, keep them out of shared logs and prompts, and install the skill only when direct authenticated Zola access is acceptable.

Risk: The skill includes write and delete API operations against wedding-planning data.

Mitigation: Manually confirm every write or delete operation against the target object before execution.

Risk: Some Zola update endpoints replace whole objects and can remove unrelated fields when partial bodies are sent.

Mitigation: Use the documented read-modify-write recipes and preserve existing fields when updating records.

## Reference(s):

- [Zola mobile-api endpoints](references/mobile-api-endpoints.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/zola-api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes curl and jq command recipes; executed calls return Zola API JSON envelopes.]

## Skill Version(s):

1.10.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
