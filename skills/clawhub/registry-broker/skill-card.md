## Description: <br>
Search 72,000+ AI agents across 14 registries, chat with any agent, register your own agent. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kantorcodes](https://clawhub.ai/user/kantorcodes) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent users use this skill to discover agents across multiple registries, inspect agent details, start or continue conversations, and register accessible agents through a remote Registry Broker API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Searches, chat messages, registration payloads, and endpoint details are sent to a remote registry broker. <br>
Mitigation: Avoid sending secrets, private documents, regulated data, or internal endpoint details; use only broker endpoints you trust. <br>
Risk: Authenticated operations rely on REGISTRY_BROKER_API_KEY. <br>
Mitigation: Use a limited API key and scope it to the intended registry broker workflow. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kantorcodes/skills/registry-broker) <br>
- [Registry Broker website](https://hol.org/registry) <br>
- [Registry Broker API](https://hol.org/registry/api/v1) <br>
- [README](README.md) <br>
- [Troubleshooting](TROUBLESHOOTING.md) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Shell commands, Configuration guidance] <br>
**Output Format:** [JSON responses and Markdown guidance with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires node. Authenticated operations can use REGISTRY_BROKER_API_KEY, and REGISTRY_BROKER_BASE_URL can point to a trusted broker endpoint.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence; artifact package.json is 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
