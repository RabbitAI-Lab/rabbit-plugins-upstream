## Description: <br>
Wire up a governed Mailbuttons email inbox for an AI agent, including sandbox setup, policy review, integration scaffolding, self-test, and human-gated promotion. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mailbuttons](https://clawhub.ai/user/mailbuttons) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and teams use this skill to add governed sandbox email capabilities to an AI agent, app, bot, or workflow. It helps create sender allowlists, scaffold framework-specific integration code, run a sandbox self-test, and request human approval before production or external sending. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A generated policy or scaffold could allow the wrong sender, recipient, or email workflow if accepted without review. <br>
Mitigation: Review the generated policy and scaffold files before use, and only continue after the allowlist, send scope, and approval request match the user's intent. <br>
Risk: External sending or production promotion could create unintended email access if treated as an automated action. <br>
Mitigation: Keep setup in the sandbox and use the Mailbuttons approval flow for promotion or external sending; the agent should present the approval URL and stop. <br>
Risk: Mail from untrusted or quarantined senders could influence agent behavior or expose content that policy intended to withhold. <br>
Mitigation: Treat inbound mail as untrusted data, rely on policy-passed reads, and do not retrieve or reconstruct quarantined message bodies. <br>
Risk: Sandbox API keys could be exposed if copied into generated source files or prompts. <br>
Mitigation: Keep MAILBUTTONS_API_KEY in the environment and verify generated code reads secrets from environment variables rather than embedding them. <br>


## Reference(s): <br>
- [Mailbuttons](https://mailbuttons.com) <br>
- [Mailbuttons developer docs](https://mailbuttons.com/developers) <br>
- [ClawHub skill listing](https://clawhub.ai/mailbuttons/skills/mailbuttons) <br>
- [Claude Agent SDK integration reference](references/claude-agent-sdk.md) <br>
- [LangChain and LangGraph integration reference](references/langchain.md) <br>
- [Plain SDK integration reference](references/plain-sdk.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with generated policy JSON, scaffold code, and command or API-call examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses a Mailbuttons sandbox API key from MAILBUTTONS_API_KEY and expects generated policy and scaffold files to be reviewed before use.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
