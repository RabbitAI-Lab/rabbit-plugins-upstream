## Description:

Vocab Cards Lite generates black-and-white printable English vocabulary flashcard PNG files from JSON word data, including main cards, optional side cards, and optional Baidu Baike QR-code cards.

This skill is ready for commercial/non-commercial use.

## Publisher:

[51comic](https://clawhub.ai/user/51comic)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, educators, and learning-content creators use this skill to convert English vocabulary lists with pronunciation, definitions, examples, and cultural notes into printable study-card image sets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup script can install Python packages into the host environment and may fall back to system-package-protection bypass behavior.

Mitigation: Create and activate a virtual environment, then install requirements there instead of running scripts/setup.sh against system Python.

Risk: QR-code card outputs can embed externally resolvable Baidu Baike URLs supplied in input data.

Mitigation: Confirm each embedded URL is appropriate for the intended audience, or omit the baike_url field when QR output is not desired.

Risk: Dependencies are listed without pinned versions, which can introduce changing behavior in shared or managed environments.

Mitigation: Pin and audit pillow, fonttools, and qrcode[pil] before managed deployment.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/51comic/skills/vocab-cards-lite)
- [Publisher Profile](https://clawhub.ai/user/51comic)
- [README.md](artifact/README.md)
- [SKILL.md](artifact/SKILL.md)
- [CHANGELOG.md](artifact/CHANGELOG.md)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Guidance]

**Output Format:** [PNG image files generated from JSON input, with Markdown usage guidance and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generates one or more 1000px-wide PNG files per vocabulary item; card height expands with content up to a documented maximum.]

## Skill Version(s):

2.0.1 (source: SKILL.md frontmatter, _meta.json, evidence.release, and CHANGELOG.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
