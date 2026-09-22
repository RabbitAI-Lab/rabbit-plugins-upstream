## Description:

JSON修复工具 helps agents repair loose JSON files by normalizing trailing commas, single quotes, unquoted keys, comments, and hexadecimal or octal numbers into valid JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to repair malformed JSON files or directories before downstream parsing, configuration, or automation workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad command and file authority for JSON repair tasks.

Mitigation: Install only after review, limit use to explicitly selected files or directories, and require confirmation before overwriting or recursively modifying content.

Risk: JavaScript VM evaluation is presented as part of the parsing approach and should not be treated as a safe parser for untrusted malicious input.

Mitigation: Avoid untrusted inputs where possible and prefer non-evaluating JSON repair tools for higher-risk files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/json-repair-kit)
- [Artifact homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON examples and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose file reads, writes, backups, validation, and Node.js command execution for selected JSON files or directories.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
