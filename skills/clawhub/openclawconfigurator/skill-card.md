## Description: <br>
A smart assistant specialized in helping users configure OpenClaw by clarifying requirements and generating Markdown configuration content for BOOTSTRAP.md, AGENTS.md, SOUL.md, IDENTITY.md, USER.md, TOOLS.md, HEARTBEAT.md, and MEMORY.md. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[qomob](https://clawhub.ai/user/qomob) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to turn personal assistant requirements into a complete OpenClaw workspace configuration package. It guides users through persona, identity, memory, tooling, heartbeat, onboarding, and channel-security choices before producing the final Markdown files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated USER.md, MEMORY.md, or other configuration files may include sensitive personal data if the user provides it. <br>
Mitigation: Review generated content before saving, avoid plaintext secrets or sensitive identifiers, and use environment variables or a secrets manager for credentials. <br>
Risk: Public-channel or daemon settings can expose the assistant more broadly than intended. <br>
Mitigation: Enable daemon and public-channel settings only after confirming access controls such as dmPolicy and allowFrom. <br>
Risk: Configuration text may encode incorrect personal, memory, or security preferences if requirements were unclear. <br>
Mitigation: Confirm persona, main tasks, user identity, and channel-security preferences before accepting the generated package. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/qomob/skills/openclawconfigurator) <br>
- [Server-resolved GitHub source](https://github.com/qomob/OpenclawConfigurator) <br>
- [OpenClaw homepage](https://openclaw.ai) <br>
- [OpenClaw onboarding documentation](https://openclaw.ai/docs/onboarding) <br>
- [OpenClaw security documentation](https://openclaw.ai/docs/security) <br>
- [Output schema](artifact/schemas/output-schema.json) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Configuration, Guidance] <br>
**Output Format:** [Markdown configuration package with content for eight OpenClaw workspace files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated content is intended for ~/.openclaw/workspace/ and should conform to artifact/schemas/output-schema.json.] <br>

## Skill Version(s): <br>
0.1.1 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
