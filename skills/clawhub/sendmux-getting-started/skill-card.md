## Description: <br>
Set up Sendmux for agents, choose MCP, CLI, SDK, or HTTP, validate scoped credentials, and make the first harmless call. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sendmux.ai](https://clawhub.ai/user/sendmux.ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to connect agents to Sendmux, select the right access surface and credential type, install the relevant package, and verify setup with a harmless first call. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sendmux API keys, claim tokens, or agent credential bundles could be exposed through chat, logs, repo files, screenshots, or memory-only handling. <br>
Mitigation: Use existing environment variables, local profiles, or trusted secret managers; rotate any credential that appears in chat or logs before continuing. <br>
Risk: Root keys can grant account-level management access when a narrower mailbox or agent token would be sufficient. <br>
Mitigation: Prefer scoped mailbox or agent tokens for mailbox and sending workflows, and reserve root keys for management-only tasks. <br>


## Reference(s): <br>
- [Sendmux ClawHub skill page](https://clawhub.ai/sendmux.ai/skills/sendmux-getting-started) <br>
- [Sendmux skills homepage](https://github.com/Sendmux/skills) <br>
- [Sendmux agent authentication guide](https://app.sendmux.ai/auth.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with shell commands, TypeScript examples, HTTP endpoint guidance, and setup decision tables] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guidance emphasizes scoped credentials, JSON CLI output, harmless validation calls, and secure secret storage.] <br>

## Skill Version(s): <br>
1.0.3 (source: ClawHub release metadata; artifact frontmatter reports 1.3.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
