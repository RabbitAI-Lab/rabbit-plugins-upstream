## Description:

Parses, validates, flattens, and converts JSON data from construction APIs, IoT sensors, and BIM metadata into tabular outputs for analysis and reporting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and automation teams use this skill to parse and validate JSON from construction systems, then flatten or convert it for reporting, statistics, and downstream workflow use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release security summary says the skill asks for command execution and broad file/API capabilities that are not clearly scoped to its JSON parsing purpose.

Mitigation: Install only when those capabilities are intentionally needed, review the skill before use, and run it with least-privilege file, API, and command permissions.

Risk: The security guidance warns that this may be unsuitable if a user only needs a parser that reads input and writes explicitly requested outputs.

Mitigation: Prefer a narrower JSON parser for simple parsing tasks, or constrain this skill to explicit input files and requested output locations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/json-parser)
- [Publisher profile](https://clawhub.ai/user/thcjp)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, JSON examples, Python snippets, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May describe parsed data, validation results, table conversion steps, configuration, and error-handling guidance.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
