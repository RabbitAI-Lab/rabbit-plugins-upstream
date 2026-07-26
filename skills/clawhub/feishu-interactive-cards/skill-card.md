## Description: <br>
Create and send interactive Feishu (Lark) cards with buttons, forms, polls, and callback handling. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[leecyang](https://clawhub.ai/user/leecyang) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agents use this skill to present choices, confirmations, forms, todos, and polls in Feishu when a message needs structured user interaction instead of free-form text. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends Feishu messages using configured app credentials. <br>
Mitigation: Install and run it only for workspaces where the configured Feishu app is intended to send interactive cards, and keep app credentials scoped and protected. <br>
Risk: The callback server forwards interaction details to OpenClaw Gateway. <br>
Mitigation: Review the Gateway URL, token, and access controls before starting the callback server. <br>
Risk: Interactive cards can carry user-provided form, todo, and button-state data. <br>
Mitigation: Minimize sensitive data embedded in cards and validate callback values before acting on them. <br>
Risk: The skill's broad guidance to use cards for any uncertainty may be excessive for sensitive or routine replies. <br>
Mitigation: Use interactive cards where explicit user choice or confirmation is needed, and apply stricter review for sensitive workflows. <br>
Risk: The helper scripts rely on Node dependencies for Feishu API and HTTP behavior. <br>
Mitigation: Keep the Node dependencies updated and redeploy patched releases promptly. <br>


## Reference(s): <br>
- [Security Best Practices](references/security-best-practices.md) <br>
- [Gateway Integration Guide](references/gateway-integration.md) <br>
- [Card Design Guide](references/card-design-guide.md) <br>
- [Feishu Card Documentation](https://open.feishu.cn/document/ukTMukTMukTM/uczM3QjL3MzN04yNzcDN) <br>
- [OpenClaw Docs](https://docs.openclaw.ai) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON card templates, JavaScript examples, shell commands, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces Feishu interactive-card templates and helper commands that use configured Feishu app credentials and OpenClaw Gateway callbacks.] <br>

## Skill Version(s): <br>
1.0.2 (source: frontmatter, CHANGELOG, package.json, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
