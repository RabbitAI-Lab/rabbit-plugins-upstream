## Description:

Reviews talking-head scripts before publication with sentence-level information-density scoring, structure checks, red-line compliance review, and concise guidance; diagnose-only by default.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

Single-operator knowledge creators use this skill to decide whether a talking-head script is ready to publish, identify weak information density or structure, and catch red-line issues before release.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks the agent to read local ZMM/vault reference files, so reviews may depend on private local files that are missing, stale, or unintended for this workflow.

Mitigation: Confirm the referenced vault files exist and are intended for use before enabling the skill; stop or narrow the review when required references are unavailable.

Risk: The skill directs automatic feedback writeback into memory without clear opt-in.

Mitigation: Make memory updates explicit or opt-in, review the proposed memory note before writing, and keep backups of the memory directory.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-review)
- [评分锚点](artifact/references/评分锚点.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown review report with scoring tables, verdicts, and concise guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May ask one clarifying question when the target audience is unclear; diagnose-only by default unless the user asks for edits.]

## Skill Version(s):

0.2.4 (source: release metadata; artifact frontmatter lists 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
