## Description:

把用户提供的 A 股监管问询函拆成逐条核对清单，匹配问题、要求材料、回复要点和回复文件，并标出未答问题与缺失材料；不代拟回复或作合规判断。

This skill is ready for commercial/non-commercial use.

## Publisher:

[huhoo](https://clawhub.ai/user/huhoo)

### License/Terms of Use:

MIT-0

## Use Case:

处理 A 股监管问询回复的员工与外部顾问，可用它逐问整理所需材料、回复要点、回复文件和未解决缺口，并保留原句与来源锚点。

### Deployment Geography for Use:

China (A-share regulatory disclosures)

## Known Risks and Mitigations:

Risk: Security evidence rates the release suspicious with medium confidence, citing reported home-directory usage markers unrelated to the stated task and a mismatch between reported capabilities and the described workflow; scanner coverage is incomplete.

Mitigation: Review the suspicious verdict and the reported behavior against the source before installing; treat scan coverage as incomplete and do not infer malicious intent from the scanner results alone.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/huhoo/skills/cue-cn-inquiry-letter-reply)
- [Cuecue MCP catalog](https://cuecue.cn/api/mcp-catalog)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Markdown checklist]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Question-by-question entries retain source quotes and anchors, flag unanswered items and missing documents, and do not draft replies or issue compliance judgments.]

## Skill Version(s):

0.1.0 (source: SKILL.md frontmatter, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
