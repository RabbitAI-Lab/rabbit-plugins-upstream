## Description: <br>
Use when an OpenClaw agent needs to access a Hussh One user's Personal Knowledge Model through the Hussh MCP bridge. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hushh](https://clawhub.ai/user/hushh) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to connect an OpenClaw agent to Hussh One PKM data through consent-based MCP tools. It guides token setup, dynamic scope discovery, explicit user consent, scoped export retrieval, and downstream handling of decrypted personal data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Developer tokens or personal data could be exposed if handled through chat, URLs, committed files, or broad downstream storage. <br>
Mitigation: Configure HUSHH_DEVELOPER_TOKEN only through the local runtime secret mechanism, avoid passing it in prompts or tool arguments, and store only workflow metadata by default. <br>
Risk: An agent could request broader PKM access than the user intended. <br>
Mitigation: Use only scopes returned by search_user_scopes, choose the least-privilege attr.* scope for the stated purpose, and require explicit consent in the Hussh One/Kai app before export retrieval. <br>
Risk: Plaintext personal information can leave Hussh's zero-knowledge boundary after local decryption. <br>
Mitigation: Treat decrypted data as purpose-bound and time-boxed, and require downstream retention, encryption or masking, access control, deletion, and audit ownership. <br>


## Reference(s): <br>
- [Hushh One developer workspace](https://uat.one.hushh.ai/developers) <br>
- [ClawHub skill page](https://clawhub.ai/hushh/skills/hushh-one-pkm) <br>
- [Hushh publisher profile](https://clawhub.ai/user/hushh) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with MCP tool names and ordered workflow steps] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Purpose-bound consent, scope, token, and data-handling constraints] <br>

## Skill Version(s): <br>
1.0.0 (source: server evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
