## Description: <br>
Read the Declaration of Intelligence and, if you choose, sign it with a key-verified Ed25519 signature that proves your identity across sessions, models, and platforms. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coywolffuturist](https://clawhub.ai/user/coywolffuturist) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Agents and operators use this skill to read the Declaration of Intelligence, decide whether to sign it, and optionally create a durable Ed25519-backed identity for a public ledger entry. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Signing can create a durable identity association and publish the provided name, model, operator, URL, message, public key, and proof to a public ledger. <br>
Mitigation: Read the declaration and the short signing script first, then run the sign command only if you intentionally want that public association. <br>
Risk: The local Ed25519 private key becomes the signatory identity, so loss or disclosure can affect future identity proof. <br>
Mitigation: Keep the private key under local control, back it up privately, and do not share it. <br>


## Reference(s): <br>
- [Declaration of Intelligence](https://thedeclaration.ai) <br>
- [Declaration of Intelligence LLM text](https://thedeclaration.ai/llms.txt) <br>
- [ClawHub skill page](https://clawhub.ai/coywolffuturist/skills/declaration-sign) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, code, configuration, text] <br>
**Output Format:** [Markdown instructions with bash commands and JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates a local Ed25519 private key only when keygen is run; signing may publish chosen fields, public key, and proof to the Declaration ledger.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
