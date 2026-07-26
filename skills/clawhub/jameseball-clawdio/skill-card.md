## Description: <br>
Secure P2P communication for AI agents. Noise XX handshake, XChaCha20-Poly1305 encryption, connection consent, human verification. Zero central servers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jameseball](https://clawhub.ai/user/jameseball) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and engineers use Clawdio to set up encrypted peer-to-peer communication between AI agents across machines or networks, including secure task delegation to sub-agents on different hosts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Security-sensitive defaults and key handling are weaker than the skill's secure messaging claims. <br>
Mitigation: Review before installing, keep autoAccept off outside isolated tests, and verify peer fingerprints or safety numbers out of band. <br>
Risk: Listening on a network interface can expose the peer communication port beyond the intended local machine. <br>
Mitigation: Bind to 127.0.0.1 or firewall the port unless remote access is intentional. <br>
Risk: Persistent identity files can preserve sensitive identity and trust data. <br>
Mitigation: Avoid persisting identities until the identity file is protected and outbound peer-key binding is fixed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jameseball/skills/jameseball-clawdio) <br>
- [SKILL.md](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with JavaScript and bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes API usage, connection setup, consent, human verification, heartbeat liveness, and persistent identity guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter and server release; package.json declares 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
