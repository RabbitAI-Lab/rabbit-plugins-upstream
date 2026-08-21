## Description:

天工.skill(Tiangong Skill)智能体设计师。当用户需要设计、创建或优化AI智能体/Agent，或基于真实人物蒸馏思维框架创建人物Skill时使用。支持两种范式：人物蒸馏（由内而外，复刻心智模型）与岗位型专家（由外而内，定义岗位职责）。目标：创建专业领域专家角色，具备清晰人设和扎实交付力。

This skill is ready for commercial/non-commercial use.

## Publisher:

[ebandao777-oss](https://clawhub.ai/user/ebandao777-oss)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, prompt engineers, and agent builders use this skill to design, create, optimize, and validate professional AI agent roles. It supports persona distillation from public-source evidence and job-oriented expert role construction with templates, quality gates, and verification scripts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad trigger wording may route ordinary agent-creation requests into this skill.

Mitigation: Review and narrow trigger words when installing in environments where only specific creation workflows should activate.

Risk: Generated agent definitions may contain incorrect, overbroad, or misleading guidance.

Mitigation: Review generated SKILL.md content and run the included verification scripts before deploying or sharing the generated skill.

Risk: The skill can create local files under output/.

Mitigation: Inspect generated files before moving them into active skill directories or production workflows.

Risk: Persona research may use web search when authorized by the user.

Mitigation: Require explicit authorization for web research and prefer primary public sources when building persona-based skills.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/ebandao777-oss/skills/tiangong-skill)
- [Server-Resolved GitHub Source](https://github.com/ebandao777-oss/tiangong-skill)
- [README](artifact/README.md)
- [Quickstart](artifact/QUICKSTART.md)
- [Extraction Framework](artifact/references/extraction-framework.md)
- [Quality Verification](artifact/references/quality-verification.md)
- [Trigger Guide](artifact/references/trigger-guide.md)
- [Template Schema](artifact/assets/template-schema.json)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown role definitions, templates, validation guidance, and optional local files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create files under output/ and may propose validation script commands.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata; artifact frontmatter reports 3.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
