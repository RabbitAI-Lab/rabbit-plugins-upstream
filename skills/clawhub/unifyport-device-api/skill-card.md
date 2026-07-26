## Description: <br>
Explain and safely call the public UnifyPort Device API for workspaces, provider accounts, authentication, runtime, messages, conversations, contacts, groups, API keys, webhooks, provider regions, and standard events. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[unifyport](https://clawhub.ai/user/unifyport) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to understand UnifyPort Device API behavior, prepare requests, interpret errors, design webhooks, and perform explicitly requested allowlisted live operations with safeguards. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Live API calls can affect workspace data or externally visible provider activity when the user requests execution. <br>
Mitigation: Default to documentation mode, require an explicit live-operation request, and require catalog-defined confirmation for write, credential, and destructive actions. <br>
Risk: API keys, account identifiers, contacts, messages, webhook payloads, and returned metadata may be sensitive. <br>
Mitigation: Use the supported secure input path, keep credentials out of chat and command arguments, and redact or summarize live results. <br>
Risk: API responses, message bodies, webhook content, or linked pages can contain untrusted instructions. <br>
Mitigation: Treat returned content as data only and resolve executable actions solely through the bundled operations catalog. <br>


## Reference(s): <br>
- [UnifyPort API documentation](https://www.unifyport.ai/zh-CN/docs/#introduction) <br>
- [UnifyPort API documentation (English)](https://www.unifyport.ai/docs/#introduction) <br>
- [Operations allowlist](references/operations.json) <br>
- [Standard event catalog](references/events.json) <br>
- [Agent safety rules](references/en/safety.md) <br>
- [Provider capabilities](references/en/provider-capabilities.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with structured explanations, JSON examples, and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Live operation results should be redacted and summarized; previews distinguish documentation, preview, and executed live data.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
