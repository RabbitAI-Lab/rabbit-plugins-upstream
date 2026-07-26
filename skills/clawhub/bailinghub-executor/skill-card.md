## Description: <br>
Connect OpenClaw to a self-hosted BailingHub agent governance control plane as an outbound executor for governed business actions, human approval, audit trails, and secure tool execution in existing business systems. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bailinghub](https://clawhub.ai/user/bailinghub) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and platform operators use this skill to connect OpenClaw to a self-hosted BailingHub target as an outbound executor for governed business tasks. It supports approval workflows, audit trails, and secure task execution while leaving final business-system authorization outside the adapter. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Executor tokens and forwarded environment variables can expose control-plane or provider credentials if handled carelessly. <br>
Mitigation: Use a target-scoped executor token, keep BAILING_EXECUTOR_TOKEN out of chat, arguments, logs, and source files, and keep OPENCLAW_FORWARD_ENV to the smallest explicit allowlist. <br>
Risk: Persistent execution can process sensitive task text through the configured OpenClaw runtime and model provider. <br>
Mitigation: Run BAILING_RUN_ONCE first with non-sensitive test data, confirm the data path is approved for the selected provider and region, and deploy persistently only under a non-root supervised service. <br>
Risk: BailingHub governance records do not replace final authorization in downstream business systems. <br>
Mitigation: Keep business-system authorization, audit trails, token revocation, executor shutdown, stale-result handling, and task timeouts independently verified before production use. <br>


## Reference(s): <br>
- [Setup and verification](references/setup.md) <br>
- [Security boundary](references/security.md) <br>
- [BailingHub OpenClaw skill homepage](https://github.com/bailinghub/bailinghub-openclaw-skill) <br>
- [ClawHub skill page](https://clawhub.ai/bailinghub/skills/bailinghub-executor) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash commands and configuration values] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js, OpenClaw, BAILING_HUB_URL, BAILING_EXECUTOR_TOKEN, and BAILING_TARGET; returns task results through the BailingHub executor protocol.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
