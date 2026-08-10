## Description:

Token Usage Tracker reads WorkBuddy trace files after model calls and reports per-response token usage, duration, estimated cost, and optional DeepSeek balance notifications.

This skill is ready for commercial/non-commercial use.

## Publisher:

[abc1317679842-ui](https://clawhub.ai/user/abc1317679842-ui)

### License/Terms of Use:

MIT

## Use Case:

WorkBuddy desktop users use this skill to see token counts, latency, estimated model costs, and DeepSeek balance context for completed responses. It is intended for Windows WorkBuddy environments where hooks and local trace files are available.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is designed to run from broad WorkBuddy hooks and may execute on every prompt or response.

Mitigation: Review the hook configuration before enabling it, keep only the UserPromptSubmit or Stop hook modes you need, and remove the hooks to disable automatic execution.

Risk: Balance checks read a DeepSeek API key from local WorkBuddy model configuration and call DeepSeek's balance endpoint.

Mitigation: Install only in environments where local API-key use and outbound calls to DeepSeek are acceptable; avoid use on shared or locked-down machines.

Risk: Pricing refresh can contact OpenRouter and update local pricing data.

Mitigation: Review outbound network policy before installation and verify estimated pricing against official provider pricing for billing-sensitive use.

Risk: The automatic notification path depends on WorkBuddy trace files, hooks, and Windows toast support.

Mitigation: Use it only with WorkBuddy desktop on Windows for automatic notifications; treat other environments as manual or unsupported.

## Reference(s):

- [Server-resolved source repository](https://github.com/abc1317679842-ui/workbuddy-token-tracker)
- [ClawHub skill page](https://clawhub.ai/abc1317679842-ui/skills/workbuddy-token-tracker)
- [OpenRouter model pricing API](https://openrouter.ai/api/v1/models)
- [DeepSeek balance endpoint](https://api.deepseek.com/user/balance)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON hook configuration; hook modes return JSON or notification text.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires WorkBuddy desktop traces and hooks, Windows for automatic toast notifications, and Node.js >= 20.]

## Skill Version(s):

0.1.1 (source: server release metadata; artifact manifest.yaml reports internal version 2.22.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
