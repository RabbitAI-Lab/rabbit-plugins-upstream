## Description:

A Chinese-first early Buddhism and Theravada study assistant for daily stories, scripture reading, doctrine lookups, meditation guidance, Pali lessons, Buddhist figures, practice check-ins, Q&A retrieval, and daily Dhammapada verses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wangdaozhenren](https://clawhub.ai/user/wangdaozhenren)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to answer Chinese-language study questions about early Buddhist and Theravada material with source-cited scripture excerpts, curated doctrine entries, meditation prompts, Pali term explanations, and optional corpus-backed retrieval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill downloads a large public scripture corpus and search index locally during first setup.

Mitigation: Install only where external downloads are acceptable; review the setup script and ModelScope source URLs when supply-chain integrity matters.

Risk: Practice check-ins may create local notes in the skill data directory.

Mitigation: Avoid entering sensitive personal information, and review or remove local practice-log data according to the user's privacy needs.

Risk: Meditation or religious-study guidance may be mistaken for medical or mental-health advice.

Mitigation: Keep the skill's stated boundary that it does not replace professional care, especially for depression, trauma, or illness.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/wangdaozhenren/skills/qingtian-buddhism)
- [ModelScope Pali-Chinese Corpus Dataset](https://modelscope.cn/datasets/Wangzhenren/pali2026-06-21txt)
- [Content Sources and Copyright Record](references/_sources.md)
- [Canon Index](references/canon-index.md)
- [Maintenance README](README.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with cited scripture excerpts and inline shell commands when setup or retrieval actions are needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Chinese-first responses; cited Pali-Chinese source excerpts; optional local corpus and semantic-index retrieval; local practice-log entries when users request check-ins.]

## Skill Version(s):

1.5.2 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
