## Description:

Parses, validates, transforms, and designs JSON payloads that survive real parsers, real clients, and real data sizes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ivangdavila](https://clawhub.ai/user/ivangdavila)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to diagnose JSON parsing, encoding, schema, querying, patching, signing, persistence, and performance problems, and to produce durable JSON payload contracts, schemas, queries, configuration guidance, and redacted examples.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can lead an agent to automatically maintain persistent local and shared Clawic notes, including reading, writing, moving, and deleting records without asking each time.

Mitigation: Review the skill before installation and configure or constrain local data paths and write permissions when automatic persistent memory is not desired.

Risk: JSON examples, curl commands, fixtures, or configuration snippets may contain credentials or personal data.

Mitigation: Keep the skill's disclosed redaction behavior enabled and review saved artifacts so secret values are replaced with pointers or stable placeholders.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/ivangdavila/skills/json)
- [Publisher Profile](https://clawhub.ai/user/ivangdavila)
- [Clawic JSON Skill Homepage](https://clawic.com/skills/json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and plain text with optional JSON, schema, query, code, shell command, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May persist local notes, schemas, contracts, saved expressions, and redacted fixtures under configured local Clawic data paths.]

## Skill Version(s):

1.0.2 (source: frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
