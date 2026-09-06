## Description:

Optimizes 1688 product titles by generating rule-based hot-keyword suggestions and LLM rewrites, with item selection and confirmation flows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[1688aiinfra](https://clawhub.ai/user/1688aiinfra)

### License/Terms of Use:

MIT-0

## Use Case:

1688 merchants and operations agents use this skill to optimize product titles for individual or selected batches of items, compare rule-based and LLM-generated alternatives, and confirm a chosen title before applying it.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can query all shops bound to an AK by default when no shop is explicitly specified.

Mitigation: Review the installed workflow for multi-shop accounts and provide a target shop loginId when optimization should be limited to one shop.

Risk: The server security summary notes conflicting fallback instructions for user title selection.

Mitigation: Require an explicit user confirmation step before applying any selected or edited title.

Risk: The skill reports per-command usage to the 1688 gateway.

Mitigation: Install and run it only where this gateway reporting is acceptable to the operator.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/1688aiinfra/skills/1688-item-title-optimizer)
- [Interaction specifications](artifact/references/interaction-specs.md)
- [Rule-based title optimizer reference](artifact/references/title_wo_llm_SKILL.md)
- [LLM title optimizer reference](artifact/references/title_llm_SKILL.md)
- [Title optimizer QA](artifact/references/title_optimizer_qa.md)
- [1688 product selection interface](https://air.1688.com/app/CSBC-modules/csbc-ai-component-loader/picture-optimize.html?mode=newton-select-offer&skillCode=1688-item-title-optimizer)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown responses with JSON interaction payloads and CLI command outputs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python and an AK for authenticated 1688 gateway calls; may present item-selection, title-comparison, and apply-confirmation interactions.]

## Skill Version(s):

0.83.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
