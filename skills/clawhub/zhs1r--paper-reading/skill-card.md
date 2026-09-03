## Description:

八要素法文献阅读 helps agents guide Chinese-first deep reading of academic papers using the Eight-Elements method, producing structured literature notes, critical questions, and literature-map updates without fabricating missing details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhs1r](https://clawhub.ai/user/zhs1r)

### License/Terms of Use:

MIT-0

## Use Case:

External researchers, students, and developers use this skill to turn a provided paper, PDF path, title, DOI, or link into deep-reading notes, guided critique, and cumulative literature-map entries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may fetch paper metadata or abstracts online, including for restricted links.

Mitigation: Use it only with sources you are authorized to access, and avoid local curl fetching for restricted links unless permission is clear.

Risk: The skill can store literature notes and user reflections in a workspace Markdown file.

Mitigation: Confirm the notes location before saving, especially when papers or personal reflections are sensitive.

Risk: Paper details may be unavailable from abstracts or incomplete source material.

Mitigation: Keep the skill's required labels such as [全文待补], [未能获取], and inferred markers instead of filling gaps with unsupported details.

## Reference(s):

- [Output Templates and Format Rules](references/output_templates.md)
- [ClawHub Skill Page](https://clawhub.ai/zhs1r/skills/paper-reading)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown notes, tables, critique prompts, and literature-map summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Defaults to Chinese; labels unavailable, incomplete, inferred, or AI-drafted content.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
