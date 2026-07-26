## Description: <br>
Derives a Nostr identity (npub/nsec) from an existing Archon DID secp256k1 key so both identities use the same key. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[macterra](https://clawhub.ai/user/macterra) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and technically capable operators use this skill to derive and publish a Nostr keypair from an existing Archon DID wallet when they intentionally want the DID and Nostr identities unified. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow handles wallet-derived private keys and emits an nsec that can control the Nostr identity. <br>
Mitigation: Run only on a trusted machine, avoid logging or sharing the nsec, and store any generated secret with restrictive file permissions. <br>
Risk: The artifact includes curl-to-shell installation guidance and unpinned npm dependency installation paths. <br>
Mitigation: Audit downloaded scripts and dependencies before execution, and pin or vendor dependencies for repeatable use. <br>
Risk: Using the same key can intentionally tie the Archon DID and Nostr identity together. <br>
Mitigation: Install and run only when that linkage is desired, and review DID updates and relay publication commands before executing them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/macterra/skills/archon-nostr) <br>
- [nak install script referenced by the skill](https://raw.githubusercontent.com/fiatjaf/nak/master/install.sh) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown instructions with bash snippets and command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include sensitive nsec/private key material and commands that modify DID metadata or publish a Nostr profile.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
