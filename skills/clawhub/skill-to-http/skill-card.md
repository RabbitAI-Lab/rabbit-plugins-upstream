## Description: <br>
Exposes installed agent Skills as HTTP(S) REST API services with generated endpoints, sync or async execution, webhook callbacks, multi-engine execution, and a bilingual management console. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[songhonglei](https://clawhub.ai/user/songhonglei) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to expose locally installed agent Skills through HTTP or HTTPS APIs so external systems can invoke, monitor, and manage skill execution. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill exposes locally installed agent Skills through a persistent HTTP gateway, creating a broad remote execution surface. <br>
Mitigation: Install only in an isolated or trusted environment, expose an explicit allowlist instead of all Skills, bind to 127.0.0.1 unless remote access is required, and use deny lists for side-effecting Skills. <br>
Risk: Default HTTP mode can transmit API keys, prompts, and Skill outputs without encryption. <br>
Mitigation: Enable HTTPS for cross-host or production use and keep a strong API key in configuration or environment storage. <br>
Risk: Public API documentation and management controls can reveal or modify service behavior when exposed with weak access control. <br>
Mitigation: Disable public docs when authentication is configured, require API-key authentication for non-local access, and treat leaked API keys as service-control compromise. <br>
Risk: The optional LLM fallback can send Skill prompts and task data to an external provider. <br>
Mitigation: Do not enable the LLM fallback unless the endpoint is trusted and exposed Skill files are free of credentials, internal addresses, and sensitive content. <br>


## Reference(s): <br>
- [HTTPS Deployment Guide](references/https-deployment.md) <br>
- [Params Schema Reference](references/params-schema.md) <br>
- [TLS and Authentication Standard](references/tls-auth-standard.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown, JSON API responses, shell commands, and configuration files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The service output depends on the exposed downstream Skill and may include synchronous responses, asynchronous job status, or webhook callbacks.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence and CHANGELOG, released 2026-07-28) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
