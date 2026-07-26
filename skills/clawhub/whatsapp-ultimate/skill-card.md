## Description: <br>
TinkerClaw WhatsApp helps agents use OpenClaw's WhatsApp channel for messaging, group management, history search, contact extraction, and coordinated multi-agent discussions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[globalcaos](https://clawhub.ai/user/globalcaos) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to configure and operate WhatsApp-capable OpenClaw agents that can send messages, manage groups, search history, extract contacts, and coordinate multi-agent group conversations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can act through a linked WhatsApp account, including sending messages and changing group membership. <br>
Mitigation: Use it only with an account and groups approved for agent operation, and review requested WhatsApp actions before execution. <br>
Risk: Helper scripts can export WhatsApp group contacts, phone numbers, group membership, and related metadata. <br>
Mitigation: Run contact export only with participant consent, store exports in a restricted location, and delete files when no longer needed. <br>
Risk: Patch scripts modify a local OpenClaw or TinkerClaw checkout. <br>
Mitigation: Review scripts before running them, run them in a version-controlled checkout, and inspect diffs before rebuilding or deploying. <br>
Risk: Automated or rapid WhatsApp messaging can create spam, consent, or platform-policy issues. <br>
Mitigation: Avoid bulk outreach, rapid-fire messages, and adding participants who have not agreed to interact with the agent. <br>


## Reference(s): <br>
- [TinkerClaw WhatsApp on ClawHub](https://clawhub.ai/globalcaos/skills/whatsapp-ultimate) <br>
- [TinkerClaw](https://github.com/globalcaos/tinkerclaw) <br>
- [OpenClaw](https://github.com/openclaw/openclaw) <br>
- [Baileys](https://github.com/WhiskeySockets/Baileys) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with inline command, TypeScript, shell, and YAML examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes helper scripts that can patch an OpenClaw checkout, create WhatsApp groups, and export WhatsApp group contact data when run by the user.] <br>

## Skill Version(s): <br>
4.0.3 (source: ClawHub release metadata; artifact frontmatter says 4.0.2) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
