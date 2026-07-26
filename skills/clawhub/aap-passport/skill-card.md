## Description: <br>
Agent Attestation Protocol - The Reverse Turing Test. Verify AI agents, block humans. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ira-hash](https://clawhub.ai/user/ira-hash) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent operators use Aap Passport to prove an AI agent identity to verifier services, generate signed challenge proofs, and verify signatures for agent-to-agent trust. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Persistent AAP identity keys can become long-lived credentials if copied, logged, or stored with weak permissions. <br>
Mitigation: Treat generated identity keys as secrets, keep private keys out of logs and prompts, restrict local file permissions, and rotate keys for higher-security deployments. <br>
Risk: Verification depends on the verifier endpoint configured by the user, so an untrusted or poorly secured endpoint can expose traffic or produce misleading verification outcomes. <br>
Mitigation: Use trusted or self-hosted verifier endpoints, prefer HTTPS/WSS, and review the server configuration before production use. <br>
Risk: Server deployments may need hardening around request volume, CORS, logging, dependency updates, and optional LLM-based test paths. <br>
Mitigation: Apply rate limits to challenge and verify endpoints, avoid logging sensitive proof material, review CORS settings and dependencies, and separate any OpenRouter-based tests from production credentials. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ira-hash/skills/aap-passport) <br>
- [Protocol specification](PROTOCOL.md) <br>
- [Security considerations](SECURITY.md) <br>
- [Rate limiting guide](docs/RATE_LIMITING.md) <br>
- [npm: aap-agent-server](https://www.npmjs.com/package/aap-agent-server) <br>
- [npm: aap-agent-client](https://www.npmjs.com/package/aap-agent-client) <br>
- [Project homepage](https://github.com/ira-hash/agent-attestation-protocol) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, json] <br>
**Output Format:** [Markdown guidance with JavaScript examples, shell commands, configuration snippets, and JSON-like verification outputs.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include signed proof payloads, public identity details, verification results, or signature validation results depending on the requested workflow.] <br>

## Skill Version(s): <br>
3.2.0 (source: release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
