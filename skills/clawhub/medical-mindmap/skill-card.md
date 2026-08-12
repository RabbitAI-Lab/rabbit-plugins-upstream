## Description:

神经病学/脑电图医学知识图谱mindmap系统。适合管理疾病、症状、检查、药物等医学知识，支持脑电图波形分析，输出模板包含核心要点、对比、临床意义、鉴别诊断价值、异常提示、本质总结。

This skill is ready for commercial/non-commercial use.

## Publisher:

[languang2026](https://clawhub.ai/user/languang2026)

### License/Terms of Use:

MIT-0

## Use Case:

External users studying neurology or EEG use this skill to create, link, query, and summarize medical concepts in a local knowledge graph. It is best suited for organizing study notes and structured medical knowledge, not for storing patient-identifying health records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-entered medical facts and relationships are saved in local JSON/JSONL files without evidence of encryption, retention controls, or deletion tooling.

Mitigation: Avoid patient-identifying health information and confidential clinical records; manage retention and deletion of local memory files outside the skill.

Risk: Medical and EEG summaries may be incomplete, outdated, or unsuitable for patient care decisions.

Mitigation: Use the skill for learning and knowledge organization, and verify medical content against authoritative clinical sources before any clinical use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/languang2026/skills/medical-mindmap)
- [ClawHub publisher profile](https://clawhub.ai/user/languang2026)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Chinese prose and Markdown with CLI examples; local JSON/JSONL files for stored graph data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Persists user-created entities, relationships, facts, and summaries under local memory/mindmap paths.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
