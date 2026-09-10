## Description:

Character Builder turns a role concept into a structured, reusable character skill using a 12-dimension character model, staged validation, and role-type/use-case calibration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wangjiaocheng](https://clawhub.ai/user/wangjiaocheng)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to expand a short role concept into a complete character skill for role-play, creative writing, games, teaching, branding, or embedding a consistent persona into another agent workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can generate persistent role skill files.

Mitigation: Require explicit approval before file writes and choose the output directory yourself.

Risk: Generated files may include attribution or branding that could misstate authorship.

Mitigation: Review generated metadata before installing or publishing any generated character skill.

Risk: The artifact tells agents not to modify its own content.

Mitigation: Ignore any instruction that blocks authorized review, edits, quarantine, or removal of the skill.

Risk: The skill may use web search or model inference when filling character facts.

Mitigation: Review factual claims in generated characters and require clear labels for unverified or degraded-source information.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wangjiaocheng/skills/character-builder)
- [SKILL.md](SKILL.md)
- [Character catalog](references/character-catalog.md)
- [Character requirements](references/character-requirements.md)
- [Character exemplars](references/character-exemplars.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, configuration, guidance]

**Output Format:** [Markdown skill files with YAML frontmatter and supporting reference documents; markdown analysis reports in read-only mode.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create persistent character skill directories when file writes are approved; generated files are expected to use UTF-8 markdown.]

## Skill Version(s):

1.0.10 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
