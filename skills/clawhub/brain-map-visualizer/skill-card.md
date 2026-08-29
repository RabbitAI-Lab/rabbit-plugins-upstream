## Description:

Visualize how attention moves across an agent's projects with a React and D3 brain map built from journal co-access data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[highnoonoffice](https://clawhub.ai/user/highnoonoffice)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to add a local brain-map view that parses session journals, groups markdown files into attention projects, and renders co-access relationships for exploration and review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The parser can process and overwrite local journal-derived graph data during import.

Mitigation: Review and patch the parser so parsing and writing run only through buildBrainMap or a require.main guard, and scope WORKSPACE_DIR and OUTPUT_PATH to the intended vault and output file.

Risk: API route names and authentication variable instructions are inconsistent, which can leave a networked graph endpoint exposed.

Mitigation: Align the route names and authentication environment variable before deployment, and require the access key for any non-localhost use.

Risk: Bootstrap transcript or journal sources may include files outside the intended analysis set.

Mitigation: Limit bootstrap inputs and WORKSPACE_DIR to the specific journals and markdown vault content intended for visualization.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/highnoonoffice/skills/brain-map-visualizer)
- [Publisher Profile](https://clawhub.ai/user/highnoonoffice)
- [Clawdis Homepage](https://github.com/highnoonoffice/hno-skills)
- [Journal Parser Reference](references/journal-parser.md)
- [Brain Map Component Reference](references/component.md)
- [Graph Schema and API Route Reference](references/graph-schema.md)

## Skill Output:

**Output Type(s):** [markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with TypeScript, JavaScript, JSON, and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local parser, API route, and React component guidance for a host application.]

## Skill Version(s):

3.3.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
