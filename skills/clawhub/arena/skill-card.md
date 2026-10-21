## Description:

Give independent Codex agents the same substantial task, compare their solutions against a clear rubric, and deliver one verified result. Use when the user asks to "arena" a task or compare competing approaches. Checks for updates when invoked.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yagel-yosef](https://clawhub.ai/user/yagel-yosef)

### License/Terms of Use:

MIT-0

## Use Case:

External developers can use Arena in Codex for substantial tasks with multiple plausible solutions, comparing independent attempts against a rubric before delivering one reviewed, verified result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: On invocation, the skill can automatically adopt upstream changes to its instructions and updater code without reviewing those changes first.

Mitigation: Review upstream changes before adopting them; use a reviewed Git checkout pinned to a commit when you need to prevent automatic advancement, and avoid relying on automatic ClawHub replacement when local edits must be preserved.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/yagel-yosef/skills/arena)
- [Declared project homepage](https://github.com/yagel-yosef/arena-skill)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Files]

**Output Format:** [Task-dependent deliverables with a concise rationale and verification summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Combines independent attempts into one reviewed result; output depends on the user's task.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
