## Description: <br>
Enable Azure OpenAI integration with OpenClaw through a lightweight local proxy that fixes Azure's required api-version URL structure for chat completion requests. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[benediktschackenberg](https://clawhub.ai/user/benediktschackenberg) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and engineers use this skill to configure OpenClaw with Azure OpenAI through a local proxy that forwards chat completion requests to the configured Azure deployment URL. It is useful when OpenClaw's normal base URL handling cannot represent Azure's required api-version query parameter. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: OpenClaw prompts, responses, and Azure API keys pass through the local proxy to the configured Azure OpenAI resource. <br>
Mitigation: Install and run the proxy only when this routing is intended, and protect the OpenClaw configuration that stores the Azure API key. <br>
Risk: Changing the bind address from 127.0.0.1 can expose the proxy beyond the local machine. <br>
Mitigation: Keep AZURE_PROXY_BIND set to 127.0.0.1 unless deliberate network exposure is required and separately protected. <br>
Risk: Enabling the optional systemd service keeps the proxy running across sessions. <br>
Mitigation: Review the service file and enable it only after deciding that persistent proxy operation is desired. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/benediktschackenberg/skills/azure-proxy) <br>
- [README](artifact/README.md) <br>
- [Skill Instructions](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, code] <br>
**Output Format:** [Markdown guidance with bash commands, JSON configuration snippets, and JavaScript proxy code] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runs a local HTTP proxy bound to 127.0.0.1 by default and forwards chat completion requests to Azure OpenAI.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
