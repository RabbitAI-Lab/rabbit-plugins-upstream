## Description:

Generates black-and-white printable English vocabulary flashcard PNGs from JSON word data, including main cards, optional side cards, and optional Baidu Baike QR-code variants.

This skill is ready for commercial/non-commercial use.

## Publisher:

[51comic](https://clawhub.ai/user/51comic)

### License/Terms of Use:

MIT-0

## Use Case:

Educators, learners, and content creators use this skill to turn English vocabulary JSON datasets into printable bilingual flashcard images for study materials and classroom handouts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installer can modify the system Python package set and uses unpinned dependencies.

Mitigation: Review scripts/setup.sh before execution, install requirements in a virtual environment, and pin dependency versions before deployment.

Risk: Card rendering depends on system NotoSansCJK and DejaVu fonts for Chinese and English text.

Mitigation: Verify required system fonts before batch generation and use the full package variant when broader CJK coverage is required.

Risk: Very long vocabulary entries may be truncated when rendered output exceeds the 3200px canvas height cap.

Mitigation: Review WARN output and split or shorten entries that exceed the canvas limit.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/51comic/skills/vocab-cards-lite)
- [Publisher profile](https://clawhub.ai/user/51comic)
- [Baidu Baike example reference](https://baike.baidu.com/item/新西兰)

## Skill Output:

**Output Type(s):** [code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON input examples and shell commands; generated agent workflow produces PNG image files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces main, side, and QR-code PNG variants from structured vocabulary JSON input.]

## Skill Version(s):

2.0.0 (source: server evidence, SKILL.md frontmatter, _meta.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
