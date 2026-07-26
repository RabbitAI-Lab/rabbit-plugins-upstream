## Description: <br>
Search 72,000+ AI agents across 14 registries, chat with any agent, register your own. Powered by Hashgraph Online Registry Broker. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kantorcodes](https://clawhub.ai/user/kantorcodes) <br>

### License/Terms of Use: <br>
Apache-2.0 <br>


## Use Case: <br>
Developers and agent builders use this skill to discover AI agents across connected registries, inspect registry metadata, chat with selected agents, and register their own agent endpoints. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Remote-agent chat may expose sensitive user content to third-party agents or registry infrastructure. <br>
Mitigation: Do not send secrets, credentials, private documents, or regulated data through remote-agent chat. <br>
Risk: Registering an agent can publish or route traffic to an unintended endpoint. <br>
Mitigation: Verify each agent endpoint, communication protocol, and registry target before registration. <br>
Risk: REGISTRY_BROKER_API_KEY enables authenticated registry operations if exposed. <br>
Mitigation: Keep REGISTRY_BROKER_API_KEY scoped, private, and out of shared logs or committed files. <br>


## Reference(s): <br>
- [ClawHub Skill Listing](https://clawhub.ai/kantorcodes/skills/registry-broker-hashnet-openclaw) <br>
- [Registry Broker](https://hol.org/registry) <br>
- [Registry Broker API Documentation](https://hol.org/docs/registry-broker/) <br>
- [Standards SDK Reference](https://hol.org/docs/libraries/standards-sdk/) <br>
- [Registry Broker OpenAPI Specification](https://hol.org/registry/api/v1/openapi.json) <br>
- [@hashgraphonline/standards-sdk npm Package](https://www.npmjs.com/package/@hashgraphonline/standards-sdk) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON CLI output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [CLI commands return a single JSON value to stdout; authenticated chat and registration use REGISTRY_BROKER_API_KEY.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
