## Description:

Qingtian Buddhism is a Chinese Early Buddhism and Theravada study assistant that recommends daily stories, reads and explains suttas, teaches core doctrines and Pali terms, guides meditation practice, introduces the Buddha and early disciples, supports practice logging, and answers questions with cited excerpts from the Pali-Chinese Tipitaka corpus.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wangdaozhenren](https://clawhub.ai/user/wangdaozhenren)

### License/Terms of Use:

MIT-0

## Use Case:

External users and practitioners use this skill for Chinese-language study of Early Buddhism and Theravada topics, including daily readings, sutta lookup, doctrinal explanations, Pali vocabulary, meditation guidance, and practice logging with source citations. Developers may also use the included scripts to download the public corpus and run keyword, semantic, hybrid, and citation-verification workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First setup downloads a large Buddhist text corpus, search index files, and optional model files.

Mitigation: Run setup in a trusted local environment with adequate bandwidth and storage, and review the configured public data source before use.

Risk: The skill creates local cache files and a local practice log that may contain user-entered practice notes.

Mitigation: Keep the generated data directory private, exclude it from published packages, and review practice-log contents before sharing a workspace.

Risk: Imported search cache files such as bm25.idx could be untrusted if copied from another environment.

Mitigation: Prefer rebuilding or downloading index artifacts from the documented source instead of importing cache files from unknown origins.

Risk: Some religious stories or practice discussions may be distressing or may touch on health-related concerns.

Mitigation: Review sensitive outputs before relying on them, and treat the skill as study guidance rather than medical, mental-health, or crisis support.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wangdaozhenren/skills/qingtian-buddhism)
- [ModelScope Pali-Chinese Tipitaka dataset](https://modelscope.cn/datasets/Wangzhenren/pali2026-06-21txt)
- [Content sources and copyright record](references/_sources.md)
- [Corpus index](references/canon-index.md)
- [Sutta reference index](references/suttas/README.md)
- [Maintenance and setup README](README.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance, configuration, files]

**Output Format:** [Markdown responses with cited excerpts, occasional shell commands, and local practice-log entries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local data, index, cache, readiness-marker, and practice-log files during setup and use.]

## Skill Version(s):

1.5.7 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
