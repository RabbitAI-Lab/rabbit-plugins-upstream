## Description: <br>
Issues a paid cryptographic proof (PDR) that a specific digital artifact existed at a particular time without uploading the artifact content. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gitserge-crypto](https://clawhub.ai/user/gitserge-crypto) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to create paid proof-of-existence records for specific artifacts after explicit user consent. It is intended for notarizing hashes of documents, code, AI outputs, datasets, logs, or other digital artifacts through AOTrust. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A document-derived hash and payment or authentication metadata are sent to AOTrust and payment settlement is irreversible. <br>
Mitigation: Confirm the exact artifact hash, destination, and $0.01 USDC cost with the user before signing, and use a dedicated low-balance wallet. <br>
Risk: Public hashes can create linkage risk for sensitive or guessable content even when the artifact itself is not uploaded. <br>
Mitigation: Avoid notarizing sensitive or easily guessable content unless the user understands that the hash will be public in the PDR. <br>
Risk: Hashing the wrong bytes would notarize the wrong artifact. <br>
Mitigation: Hash the artifact content directly in a reproducible format and show the hash to the user before requesting notarization. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/gitserge-crypto/skills/aotrust-pdr-notarization) <br>
- [AOTrust verification endpoint](https://api.aotrust.link/v1/pdr/verify) <br>
- [PDR binary specification](https://github.com/GitSerge-crypto/aotrust-skills/blob/main/pdr-spec.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown instructions with JSON examples and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires explicit user consent, reproducible artifact hashing, and manual approval of the $0.01 USDC payment before notarization.] <br>

## Skill Version(s): <br>
3.7.0 (source: server release metadata and artifact metadata/changelog) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
