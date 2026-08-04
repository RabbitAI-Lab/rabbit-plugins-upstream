## Description: <br>
Use when choosing best-value Nous Portal models. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sknewcomb](https://clawhub.ai/user/sknewcomb) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and Hermes Agent users use this skill to compare current Nous Portal model pricing, promotions, and workload fit, then receive one best-value recommendation plus a lower-cost alternative. It is intended for Nous Portal model-selection decisions and requires explicit approval before changing defaults or session model settings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Model-switch recommendations may affect quality or cost if approved without review. <br>
Mitigation: Review the recommendation and approve a switch only after checking the stated model, price evidence, and tradeoffs. <br>
Risk: Portal prices, discounts, and model availability can become stale. <br>
Mitigation: Refresh or inspect current Nous Portal evidence before relying on sale pricing or availability. <br>
Risk: Changing the default model affects future Hermes sessions. <br>
Mitigation: Use the skill approval gate and verify the resulting provider and default model after any persistent change. <br>


## Reference(s): <br>
- [Server-resolved GitHub provenance](https://github.com/sknewcomb/nous-model-deal-router) <br>
- [ClawHub skill page](https://clawhub.ai/sknewcomb/skills/nous-model-deal-router) <br>
- [Hermes Agent](https://github.com/NousResearch/hermes-agent) <br>
- [Raw skill install source](https://raw.githubusercontent.com/sknewcomb/nous-model-deal-router/main/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown recommendation with inline shell commands and configuration values] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Presents one recommended model and one lower-cost alternative; configuration changes are gated on explicit user approval.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
