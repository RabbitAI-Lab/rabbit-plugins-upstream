## Description: <br>
Guides OcuClaw installation, updates, rollback, and troubleshooting for the OpenClaw plugin, phone app, Tailscale private networking, and optional Soniox voice input, Even AI, and bug-report integrations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ocuclaw](https://clawhub.ai/user/ocuclaw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to set up and maintain OcuClaw for Even Realities G2 smart glasses, including plugin installation, private phone-to-host networking, updates, rollback, and guided troubleshooting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Setup can change local OpenClaw configuration, install or update the OcuClaw plugin, configure Tailscale private networking, and restart services. <br>
Mitigation: Review each proposed phase before approval, prefer official package-manager or signed-installer Tailscale instructions when desired, and verify service status after changes. <br>
Risk: Relay, Soniox, and Even AI tokens are sensitive. <br>
Mitigation: Keep tokens private, have the user enter secrets directly, and rely on redacted presence checks instead of reading stored values. <br>
Risk: Optional Soniox, Even AI, and debug-upload features add extra configuration or sharing behavior. <br>
Mitigation: Enable optional integrations only after explicit review, keep debug upload opt-in, and confirm what was enabled at wrap-up. <br>


## Reference(s): <br>
- [OcuClaw website](https://ocuclaw.com) <br>
- [ClawHub skill page](https://clawhub.ai/ocuclaw/skills/ocuclaw-assist) <br>
- [OcuClaw fresh install - Steps 1-13](references/fresh-install.md) <br>
- [Updating OcuClaw](references/update.md) <br>
- [OcuClaw beta channel and rollback](references/beta.md) <br>
- [OcuClaw troubleshooting - named cases](references/troubleshooting.md) <br>
- [OcuClaw quick reference](references/quick-reference.md) <br>
- [OcuClaw wrap-up and feedback](references/wrap-feedback.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes phase checkpoints, verification steps, restart warnings, and secret-handling guardrails.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata and guide version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
