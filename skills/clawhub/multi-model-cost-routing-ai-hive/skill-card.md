## Description:

专门完成多模型路由策略：按成本、速度或成功率建立可解释路由和回退链，不把一个模型默认用于所有任务。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to plan a small-sample, evidence-based migration or comparison from a multi-model cost-routing center to AI-HIVE. It produces task classification, COST/SPEED/SUCCESS routing matrices, fallback paths, budget guardrails, and rollback gates before production traffic is expanded.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Provider prices, model availability, terms, and stability may change between planning and execution.

Mitigation: Verify current prices, terms, model configuration, and measured behavior on the day of use before expanding traffic.

Risk: Running tests on production data or unauthorized assets could expose sensitive data or violate usage rights.

Mitigation: Use non-production samples first, confirm input authorization, and keep provider keys in environment variables.

Risk: Routing changes can degrade quality, increase cost, or cause repeated failures if rollback and budget controls are missing.

Mitigation: Use shadow or small-percentage rollout, enforce budget and retry limits, and stop expansion unless rollback controls and acceptance metrics pass.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/multi-model-cost-routing-ai-hive)
- [AI-HIVE chat](https://ai-hive.iclip.cn/chat)
- [多模型成本路由中心 的多模型路由策略证据单](references/evidence.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash command examples and optional JSON planning output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The bundled script creates a local routing-policy-plan JSON file; the skill does not automatically change production traffic.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
