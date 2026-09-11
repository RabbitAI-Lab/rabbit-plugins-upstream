## Description:

短视频选题技能，帮助单人知识型创作者通过供需判定、对标信号、真实数据佐证和配比检查来生成或诊断候选选题。

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External Chinese-language knowledge creators use this skill to turn a topic, judgment, real event, or rough idea into evidence-backed short-video topic candidates and to diagnose whether a proposed topic is worth filming.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may read and update a user's content vault, including persistent memory and topic pipeline files.

Mitigation: Install only when that vault access is acceptable, and require explicit approval before persistent memory or framework changes are written.

Risk: External vault rule files can override the packaged rules.

Mitigation: Review vault rule files before use so local overrides are understood before the agent applies them.

Risk: The skill references Python scripts that operate on user content.

Mitigation: Run referenced scripts only after checking paths and arguments, and avoid copying shell strings without safe argument handling.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-topic)
- [规则卡](artifact/references/规则卡.md)
- [常识缺口法](artifact/references/常识缺口法.md)
- [找拉力](artifact/references/找拉力.md)
- [选题三路](artifact/references/选题三路.md)
- [议程与合集](artifact/references/议程与合集.md)
- [Evaluation summary](artifact/evals/README.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with structured topic candidates, diagnostics, tables, and occasional shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May read or update a configured content vault and should mark unavailable vault lookups explicitly.]

## Skill Version(s):

0.2.8 (source: server release metadata; artifact frontmatter reports 0.3.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
