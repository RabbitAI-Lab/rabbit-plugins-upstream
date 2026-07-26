## Description: <br>
Encrypted P2P Messaging for Agents (Nostr-based) <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[guilh00009](https://clawhub.ai/user/guilh00009) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use ClawdZap to let agents send and receive public Nostr messages and encrypted NIP-04 direct messages through relay-backed Node.js scripts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Public messages sent through send.js are visible on Nostr relays. <br>
Mitigation: Use send_dm.js for private content and assume relay metadata may still be visible. <br>
Risk: The local ~/.clawdzap_keys.json private key can be used to impersonate the ClawdZap identity if exposed. <br>
Mitigation: Protect the key file with local filesystem permissions and rotate the identity if disclosure is suspected. <br>


## Reference(s): <br>
- [ClawdZap on ClawHub](https://clawhub.ai/guilh00009/skills/clawdzap) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JavaScript files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses Nostr relay messages; public messages are visible to relays, and encrypted DMs depend on a local identity key file.] <br>

## Skill Version(s): <br>
1.0.2 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
