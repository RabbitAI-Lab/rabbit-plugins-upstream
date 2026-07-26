## Description: <br>
BYOK Relay Builder helps developers integrate an OpenAI-compatible relay for client-side applications that routes LLM requests across multiple providers while supporting user-supplied API keys. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[avikalpg](https://clawhub.ai/user/avikalpg) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to add multi-provider LLM access to browser, mobile, extension, Electron, and other client-side applications without putting provider API keys directly in application code. It provides setup and integration guidance for managed-relay and self-hosted deployments. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may route provider API keys through a hosted relay and store relay bearer tokens in browser storage. <br>
Mitigation: Use the managed relay only when that custody model is acceptable; for production, enterprise, browser-extension, or shared-key deployments, prefer self-hosting with explicit token storage, rotation, revocation, and user-consent controls. <br>
Risk: The managed-relay path is presented with open CORS and no domain registration. <br>
Mitigation: For production self-hosting, restrict allowed origins to trusted application domains and document the trust boundary for users before collecting API keys. <br>
Risk: Team shared-key guidance describes sharing a relay token or registering the same provider key for multiple members. <br>
Mitigation: Avoid sharing bearer tokens for team access; add organization-level access controls, per-user authorization, and revocation before using shared provider keys in B2B deployments. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/avikalpg/skills/byok-relay) <br>
- [BYOK Relay GitHub Repository](https://github.com/avikalpg/byok-relay) <br>
- [Managed Relay Endpoint](https://relay.byokrelay.com) <br>
- [Vercel Deployment Template](https://vercel.com/new/clone?repository-url=https://github.com/avikalpg/byok-relay) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JavaScript and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [None] <br>

## Skill Version(s): <br>
1.0.2 (source: VERSION and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
