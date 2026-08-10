## Description:

Translate Minecraft Java Edition mod content from English to Chinese using a community-maintained dictionary (Dict-Sqlite.db, 900K+ entries from i18n-Dict-Extender) and zh.minecraft.wiki for vanilla game terms.

This skill is ready for commercial/non-commercial use.

## Publisher:

[csctacg](https://clawhub.ai/user/csctacg)

### License/Terms of Use:

MIT

## Use Case:

Developers, modpack authors, and localization maintainers use this skill to translate Minecraft Java Edition mod language files, FTB Quests SNBT, config descriptions, Patchouli books, and related mod text from English to Simplified Chinese while preserving file structure and mod terminology.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can download a large community-maintained SQLite dictionary from GitHub.

Mitigation: Use the documented update flow deliberately, and pin or verify the dictionary source when reproducibility matters.

Risk: Fallback lookups may send individual terms to zh.minecraft.wiki.

Mitigation: Use the documented --no-wiki option for local-only dictionary lookups.

Risk: Automated translation can leave incorrect terms or damage structured mod files if edits are not reviewed.

Mitigation: Review translated output for remaining English text, valid JSON/SNBT/lang structure, and terminology consistency before release.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/csctacg/skills/mc-mod-translate)
- [Source repository](https://github.com/CSCTACG/mc-mod-translate)
- [i18n-Dict-Extender dictionary source](https://github.com/VM-Chinese-translate-group/i18n-Dict-Extender)
- [i18n-Dict-Extender releases](https://github.com/VM-Chinese-translate-group/i18n-Dict-Extender/releases)
- [zh.minecraft.wiki API](https://zh.minecraft.wiki/api.php)
- [CFPA i18n-dict](https://github.com/CFPATools/i18n-dict)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and translated text or file-content edits]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May emit TSV or JSON lookup results from helper scripts; translated artifacts should preserve source file formats and encoding.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
