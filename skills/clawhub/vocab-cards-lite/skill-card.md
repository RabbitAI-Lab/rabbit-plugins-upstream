## Description:

Generates printable black-and-white English vocabulary flashcard PNG images from JSON word lists, including main cards, optional side cards, and optional Baidu Baike QR-code cards.

This skill is ready for commercial/non-commercial use.

## Publisher:

[51comic](https://clawhub.ai/user/51comic)

### License/Terms of Use:

MIT-0

## Use Case:

External users, educators, and developers use this skill to turn JSON vocabulary lists into printable English-study flashcard PNGs with bilingual definitions, examples, cultural notes, optional side-card details, and optional Baidu Baike QR variants.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Dependency advisories may affect the pinned image-processing stack over time.

Mitigation: Install in a virtual environment and review or update the pinned Pillow, fonttools, and qrcode dependencies against the deployment advisory database before use.

Risk: Installing Python packages into the system interpreter can affect other workloads.

Mitigation: Use `bash scripts/setup.sh --venv .venv`; only use `--allow-global` when system-wide installation is intentional and accepted.

Risk: Missing system CJK or DejaVu fonts can cause rendering failures or missing glyphs because the lite package bundles only IPA fonts.

Mitigation: Run the setup script's font checks and install NotoSansCJK and DejaVu system fonts before generating cards.

Risk: Very long vocabulary entries can exceed the 3200px canvas limit and be truncated.

Mitigation: Review WARN messages and shorten or split oversized entries before using generated cards.

Risk: Input `baike_url` values are encoded into QR-code card variants when provided.

Mitigation: Use trusted JSON word lists and review generated QR destinations before printing or distribution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/51comic/skills/vocab-cards-lite)
- [Publisher profile](https://clawhub.ai/user/51comic)
- [README.md](artifact/README.md)
- [SKILL.md](artifact/SKILL.md)
- [CHANGELOG.md](artifact/CHANGELOG.md)
- [REFERENCES.md](artifact/references/REFERENCES.md)
- [requirements.txt](artifact/requirements.txt)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Configuration instructions, Text]

**Output Format:** [PNG image files with console status text and optional shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates local 1000px-wide PNG main cards, optional QR-code cards, and optional side cards; reports per-entry OK, SKIP, FAIL, WARN, and summary messages.]

## Skill Version(s):

2.0.4 (source: server evidence release, SKILL.md frontmatter, _meta.json, and CHANGELOG.md; released 2026-08-11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
