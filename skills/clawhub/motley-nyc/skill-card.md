## Description:

Answer NYC family questions from Motley's live dataset — which neighborhood fits, which school is right, how school admissions actually works.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bitbrujo](https://clawhub.ai/user/bitbrujo)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to answer family-focused New York City neighborhood, school, admissions, safety, health, and family-resource questions through Motley's hosted MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: NYC school, neighborhood, address, or family-preference queries are sent to Motley's hosted MCP service.

Mitigation: Use the skill only when users are comfortable sharing those queries with Motley, and avoid sending unnecessary personal details.

Risk: Neighborhood scores and admissions details may be time-sensitive.

Mitigation: Use response metadata such as scores_as_of when available and state dates when the timing affects the answer.

Risk: Invented neighborhood or school identifiers could produce misleading answers.

Mitigation: Look up nta_code and DBN identifiers with the provided tools before using identifier-specific calls.

## Reference(s):

- [Motley MCP homepage](https://motley.nyc/mcp)
- [Motley MCP server endpoint](https://mcp.motley.nyc/mcp)
- [Motley website](https://motley.nyc)
- [ClawHub skill page](https://clawhub.ai/bitbrujo/skills/motley-nyc)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands, configuration examples, and natural-language guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses Motley's hosted MCP tools, which return typed structuredContent alongside text.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
