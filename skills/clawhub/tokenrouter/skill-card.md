## Description: <br>
Smart LLM router and token cost optimizer that helps users choose model tiers for AI tasks, estimate cost tradeoffs, and configure multi-model routing for agent workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[qomob](https://clawhub.ai/user/qomob) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, agent builders, and AI tool users use this skill to choose cost-appropriate model tiers, apply safety upgrades for higher-risk tasks, estimate token costs, and draft routing configurations for tools such as OpenClaw, Hermes Agent, Claude Code, and Codex CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can save model-routing preferences, budget hints, task categories, feedback, and estimated cost history in Memory. <br>
Mitigation: Install only when cross-session personalization is acceptable, and clear or avoid memory records when users do not want routing history retained. <br>
Risk: Model prices and provider capabilities can change after the skill's recommendations are written. <br>
Mitigation: Verify current pricing and model availability with provider documentation or routing services before using estimates for budget decisions. <br>


## Reference(s): <br>
- [Server-resolved GitHub provenance: qomob/TokenRouter](https://github.com/qomob/TokenRouter) <br>
- [ClawHub skill page: Token Router](https://clawhub.ai/qomob/skills/tokenrouter) <br>
- [OpenRouter](https://openrouter.ai) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, configuration, shell commands] <br>
**Output Format:** [Markdown with model-tier recommendations, cost estimates, routing instructions, and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include structured route blocks, budget estimates, session summaries, and safety-upgrade rationale.] <br>

## Skill Version(s): <br>
0.1.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
