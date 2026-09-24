## Description:

Repair malformed JSON files by normalizing them through Node.js evaluation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wanng-ide](https://clawhub.ai/user/wanng-ide)

### License/Terms of Use:

ISC

## Use Case:

Developers and agents use this skill to repair malformed JSON configuration or data files by converting loose JSON-like syntax into valid formatted JSON.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Malformed JSON is evaluated as JavaScript, which can be risky for untrusted input.

Mitigation: Only use the skill on JSON files and directories that are fully trusted; prefer a non-executing JSON5 or JSONC parser for untrusted content.

Risk: Recursive directory repair can automatically rewrite many JSON files.

Mitigation: Avoid recursive repair on shared, downloaded, repository, or attacker-writable directories; use a separate output file or review backups before keeping changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wanng-ide/skills/json-repair-kit)
- [ClawHub publisher profile](https://clawhub.ai/user/wanng-ide)

## Skill Output:

**Output Type(s):** [text, code, shell commands, configuration, guidance]

**Output Format:** [JSON files and Markdown guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can write repaired JSON in place with backup files or to a separate output file.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata and artifact/package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
