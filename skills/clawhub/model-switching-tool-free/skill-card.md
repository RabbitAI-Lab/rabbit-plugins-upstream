## Description: <br>
模型切换工具(免费版) helps individual developers choose among Claude Haiku, Sonnet, and Opus tiers with a three-level decision framework for matching task complexity to cost. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and agent users use this skill to choose an appropriate Claude model tier for personal projects, sub-agent task routing, and scheduled tasks. It is intended for cost-conscious model selection guidance, not automated enforcement or high-stakes decision making. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests read, write, and command-execution authority that is broader than its model-selection guidance requires. <br>
Mitigation: Review before installing, prefer read-only or explicit-invocation use where possible, and grant write or exec permissions only when a concrete workflow requires them. <br>
Risk: API keys or model-provider credentials may be exposed if users place them directly in prompts, files, or command history. <br>
Mitigation: Keep API keys in secure environment variables or a secret manager, and avoid embedding secrets in generated examples or logs. <br>
Risk: Model pricing and availability guidance can become stale as providers update models and rates. <br>
Mitigation: Confirm current provider pricing and available model tiers before making budget or production routing decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/model-switching-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with text, decision trees, tables, JSON examples, and code snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include model-tier recommendations, cost-comparison guidance, configuration examples, and execution logs.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
