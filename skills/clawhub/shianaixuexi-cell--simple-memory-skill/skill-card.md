## Description:

Zero-dependency AI memory system. No API keys needed. Pure local storage with smart search. Works everywhere.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shianaixuexi-cell](https://clawhub.ai/user/shianaixuexi-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this skill to set up project-local memory for preferences, decisions, facts, lessons, and active session state. It provides CLI-backed workflows for storing, searching, listing, importing, and exporting local memory files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill encourages plaintext storage of conversation-derived information in project-local files, which can capture sensitive or regulated data without clear consent or retention controls.

Mitigation: Do not store secrets or regulated personal data; add SESSION-STATE.json, MEMORY.md, and memories/*.json to .gitignore; review and delete memory files periodically.

Risk: The security guidance flags memory-list --date as unsafe with untrusted input until date validation is fixed.

Mitigation: Use only trusted, validated date values and avoid passing untrusted user input to memory-list --date.

Risk: The documentation mentions maintenance commands that are not present in the packaged CLI files.

Mitigation: Verify command availability before relying on maintenance workflows, and use export, manual review, or implemented commands for memory maintenance.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/shianaixuexi-cell/skills/simple-memory-skill)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands, JSON examples, and file-oriented configuration steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update project-local memory files such as SESSION-STATE.json, MEMORY.md, and memories/*.json when the described commands are run.]

## Skill Version(s):

1.0.0 (source: frontmatter, package.json, ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
