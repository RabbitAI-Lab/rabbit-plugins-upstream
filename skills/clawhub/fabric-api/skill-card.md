## Description: <br>
Create, search, and manage Fabric resources via the Fabric HTTP API, including notepads, folders, bookmarks, files, and tags. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tristanmanchester](https://clawhub.ai/user/tristanmanchester) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to read, search, create, and manage content in a user's Fabric workspace through the Fabric HTTP API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read and modify a user's Fabric workspace when a valid Fabric API key is available. <br>
Mitigation: Use a scoped or revocable Fabric API key where available and install only when workspace access is intended. <br>
Risk: Secrets could be exposed if API keys are pasted into prompts, URLs, client-side code, or logs. <br>
Mitigation: Provide FABRIC_API_KEY through the runtime environment or skill configuration, and avoid placing tokens in URLs or logged text. <br>
Risk: Changing FABRIC_BASE or using --with-key with an arbitrary absolute URL could send credentials to an untrusted endpoint. <br>
Mitigation: Keep FABRIC_BASE pointed at trusted Fabric-compatible endpoints and do not use --with-key for arbitrary URLs. <br>
Risk: Delete, recover, bulk-write, and file-upload operations can change or remove workspace content. <br>
Mitigation: Review destructive, recovery, bulk-write, and file-upload operations before running them. <br>


## Reference(s): <br>
- [Fabric homepage](https://fabric.so) <br>
- [Fabric API OpenAPI spec](fabric-api.yaml) <br>
- [Fabric API skill reference](references/REFERENCE.md) <br>
- [Troubleshooting Fabric API requests](references/TROUBLESHOOTING.md) <br>
- [ClawHub skill page](https://clawhub.ai/tristanmanchester/skills/fabric-api) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, JSON request bodies, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call the Fabric HTTP API using Node or Python helper scripts when FABRIC_API_KEY is configured.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence, released 2026-02-26) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
