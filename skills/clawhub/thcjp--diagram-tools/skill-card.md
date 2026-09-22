## Description:

Generates Mermaid, Graphviz, flowchart, mind map, UML, timeline, and data visualization diagrams for agent users.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, technical teams, and automation users use this skill to create structured diagrams such as flowcharts, mind maps, UML diagrams, architecture diagrams, timelines, and basic data visualizations from agent-provided content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence rates the skill as suspicious because it requests broad read, write, shell execution, API, and credential-related authority that is not tightly scoped to diagram generation.

Mitigation: Use the skill only in a controlled workspace, avoid exposing unrelated files or secrets, and approve shell commands only when they are clearly expected diagram-rendering commands.

Risk: The skill references API key configuration and external services without detailed scoping.

Mitigation: Use narrowly scoped environment variables, keep credentials out of version control and logs, and rotate any credential that may have been exposed during use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/diagram-tools)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, JSON-style result envelopes, diagram source snippets, and shell commands when diagram rendering requires execution.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Mermaid or DOT diagram text, rendered diagram file guidance, and API key setup guidance.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
