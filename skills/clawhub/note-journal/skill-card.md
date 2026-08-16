## Description:

笔记手账 helps agents turn educational topics into structured notebook-style image prompts for knowledge cards, posters, practice pages, and answer explanations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fslong520](https://clawhub.ai/user/fslong520)

### License/Terms of Use:

MIT-0

## Use Case:

Educators, students, and content creators use this skill to plan Chinese educational knowledge cards and generate polished prompts for notebook-style AI images, including CSP-J/CSP-S/GESP study cards, check-in posters, and practice or answer pages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad trigger terms such as anime, Minecraft, or pixel may activate the skill when the user only intended a general style discussion.

Mitigation: Confirm the user wants a notebook-style educational prompt before applying the skill to broad style requests.

Risk: The skill declares Write/Edit permissions even though the documented workflow is prompt generation.

Mitigation: Install with least-privilege controls where available and review any proposed file writes or edits before accepting them.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/fslong520/skills/note-journal)
- [Skill Definition](artifact/SKILL.md)
- [Style System](artifact/styles.md)
- [Prompt Templates](artifact/templates.md)
- [Reference Guide](artifact/reference.md)
- [OI Code Style](artifact/oi-code-style.md)
- [Prompt Examples](artifact/examples.md)
- [Changelog](artifact/CHANGELOG.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, guidance]

**Output Format:** [Structured Markdown prompt text with optional C++ code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Defaults to Chinese educational copy and 3:4 image-card prompt structures; asks for a title when missing.]

## Skill Version(s):

3.3.1 (source: server release metadata; artifact frontmatter and changelog list 3.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
