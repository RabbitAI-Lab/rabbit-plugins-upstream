## Description:

Generate deterministic seeded K-12 arithmetic drill sets, query Zaner-Bloser and DNealian primary handwriting ruling specifications, configure custom name-tracing sheets, and look up cursive stroke-group progressions via PaperLesson MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[paperlesson](https://clawhub.ai/user/paperlesson)

### License/Terms of Use:

MIT-0

## Use Case:

External educators and caregivers can use an MCP-compatible agent to prepare arithmetic practice, consult handwriting guidance, and configure tracing worksheets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill makes requests to the external PaperLesson service, and the scan does not establish what information every request may contain.

Mitigation: Before use, consider whether you trust and need the service and review what information the request sends.

Risk: The security scan was partial and two local references were unresolved, so not every referenced item was checked.

Mitigation: Review the referenced items before relying on them.

## Reference(s):

- [PaperLesson worksheet studio](https://paperlesson.com/)
- [Custom name tracing generator](https://paperlesson.com/name-tracing-generator)
- [Primary handwriting worksheets](https://paperlesson.com/handwriting-worksheets)
- [Cursive handwriting worksheets](https://paperlesson.com/cursive-handwriting-worksheets)
- [PaperLesson MCP endpoint](https://paperlesson.com/api/mcp)

## Skill Output:

**Output Type(s):** [Text, Configuration]

**Output Format:** [Educational practice content, reference information, and worksheet configuration in text or structured responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Seeded arithmetic drills are deterministic when the same inputs and seed are used.]

## Skill Version(s):

1.0.1 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
