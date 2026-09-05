## Description:

Read MaxPreps.com high school sports data, including school search results, team schedules, scores, records, rosters, stat leaders, rankings, and athlete careers for US high schools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill for low-volume, user-directed lookups of public MaxPreps high-school sports information and for producing commands or guidance that retrieve and decode that data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can fetch public student athlete roster and career information from MaxPreps.

Mitigation: Use it for low-volume, user-directed lookups and avoid republishing sensitive student-related data without appropriate care.

Risk: MaxPreps page shapes and positional data maps can change, which may cause decoded fields to be wrong while still looking plausible.

Mitigation: Cross-check decoded schedules, rosters, and standings against the public site or the verification recipes before relying on results.

## Reference(s):

- [MaxPreps recipes](references/recipes.md)
- [MaxPreps](https://www.maxpreps.com)
- [maxpreps-mcp typed MCP tools](https://github.com/chrischall/maxpreps-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, code, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON-producing CLI usage.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only MaxPreps lookups; CLI output is JSON when commands are executed.]

## Skill Version(s):

0.3.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
