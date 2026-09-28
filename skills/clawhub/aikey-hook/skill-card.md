## Description:

AI KEY·开头前五秒 helps an agent diagnose whether short-form video content has enough substance, compare material-led and audience-suspense openings, and produce opening-hook candidates with the reasoning behind each choice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators and writing agents use this skill to evaluate whether a draft or topic can support a strong first-five-seconds hook, then generate concise hook candidates grounded in the available material and audience question.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can remember hook preferences or rejected styles across sessions when an agent has access to persistent AI KEY memory.

Mitigation: Review or disable write-back behavior before use when chat feedback should not become persistent rules.

Risk: The skill may read local AI KEY reference or vault files during its writing workflow.

Mitigation: Install only in workspaces where those local files are intended to be available to the agent.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/aikey-hook)
- [AI KEY upgrade README](https://github.com/iamzifei/aikey#老用户升级zmm-已改名为-ai-key)
- [大众悬念与兑现](artifact/references/大众悬念与兑现.md)
- [规则卡](artifact/references/规则卡.md)
- [aikey-hook 0.4.0 规则演练](artifact/evals/20260914-v0.4.0-规则演练.md)
- [0.4.1 编辑演练](artifact/evals/20260915-v0.4.1-规则演练.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Analysis]

**Output Format:** [Markdown with diagnostic notes and hook candidates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include recommended next steps, candidate grouping, rationale, and memory notes when the agent has access to a persistent vault.]

## Skill Version(s):

0.4.5 (source: ClawHub release metadata; artifact frontmatter lists 0.4.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
