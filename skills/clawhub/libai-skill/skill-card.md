## Description:

李白.Skill:润色专家 检测并消除中文文本中的AI生成痕迹，将生硬的机器输出转化为自然流畅的人类文笔。融合规则检测、分层改写和质控流水线，确保最终文本通过人工审查。

This skill is ready for commercial/non-commercial use.

## Publisher:

[ebandao777-oss](https://clawhub.ai/user/ebandao777-oss)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to diagnose and rewrite Chinese text so it reads more natural and less machine-generated, with lightweight, full, or diagnostics-only delivery modes. It is intended for expression-level editing and requires human review for factual accuracy, sensitive domains, and disclosure-sensitive contexts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can be used to hide AI authorship and mislead reviewers.

Mitigation: Use it only for disclosed rewriting or clarity editing, and prefer diagnostics-only mode where disclosure, academic integrity, editorial policy, or professional review matters.

Risk: The workflow can inject human-sounding details or personal cues that were not present in the source text.

Mitigation: Require human review of revised text for factual accuracy, source faithfulness, personal details, and domain-specific obligations before use.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/ebandao777-oss/libai-skill)
- [ClawHub skill page](https://clawhub.ai/ebandao777-oss/skills/libai-skill)
- [README.md](artifact/README.md)
- [QUICKSTART.md](artifact/QUICKSTART.md)
- [faq.md](artifact/faq.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance]

**Output Format:** [Markdown or plain text responses, with optional JSON diagnosis reports and Markdown file outputs in full mode.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default lightweight mode returns revised text plus a concise change summary; diagnostics-only mode does not rewrite.]

## Skill Version(s):

0.1.0 (source: server release metadata; artifact frontmatter describes upstream skill v2.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
