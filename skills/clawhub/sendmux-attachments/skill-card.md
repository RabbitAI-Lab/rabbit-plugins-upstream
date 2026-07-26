## Description: <br>
Move email attachments through Sendmux without putting file bytes in model context, using file paths, presigned URLs, CLI, SDKs, or MCP. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sendmux.ai](https://clawhub.ai/user/sendmux.ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to send, upload, read, and reference Sendmux email attachments through MCP, CLI, HTTP, TypeScript, or Python while avoiding unnecessary transfer of file bytes through model context. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Credential names may be confused between mailbox access and sending actions. <br>
Mitigation: Confirm which Sendmux key is intended for each workflow, use the least-privileged key available, and avoid reusing broader mailbox credentials for sending examples unless provider documentation requires it. <br>
Risk: Sensitive or large attachments could be exposed or waste tokens if pasted into model context as base64. <br>
Mitigation: Prefer local file paths, presigned URLs, CLI or SDK file helpers, and avoid asking users to paste secrets or file bytes into chat. <br>


## Reference(s): <br>
- [Sendmux Attachments on ClawHub](https://clawhub.ai/sendmux.ai/skills/sendmux-attachments) <br>
- [Sendmux skills homepage](https://github.com/Sendmux/skills) <br>
- [Sendmux publisher profile](https://clawhub.ai/user/sendmux.ai) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with command examples, JSON snippets, and TypeScript or Python code examples.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses SENDMUX_API_KEY and SENDMUX_MBX_KEY when credentials are needed; favors file paths, presigned URLs, CLI, SDKs, or MCP helpers instead of embedding attachment bytes in model context.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata; artifact frontmatter reports 1.3.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
