## Description:

Issues cryptographic proof that a digital artifact existed at a specific time by notarizing its SHA-256 hash and returning a publicly verifiable PDR.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gitserge-crypto](https://clawhub.ai/user/gitserge-crypto)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, agents, and operators use this skill to create or verify proof-of-existence records for specific documents, code, AI outputs, datasets, logs, or other digital artifacts. It should be invoked only when a user explicitly requests notarization or proof for a known artifact.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Artifact hashes, verification identifiers, and payment metadata are sent to AOTrust and may become publicly verifiable.

Mitigation: Use the skill only for intended artifacts, avoid sensitive low-entropy content, and confirm user consent before notarization.

Risk: Paid notarization uses an irreversible external payment flow.

Mitigation: Show the artifact hash and cost before paid notarization, and require manual wallet approval for every payment.

Risk: Issued PDR records are immutable and cannot be changed after creation.

Mitigation: Verify that the hash was computed from the exact artifact bytes before submitting the notarization request.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gitserge-crypto/skills/aotrust-pdr-notarization)
- [AOTrust MCP endpoint](https://api.aotrust.link/mcp)
- [AOTrust HTTP notarization endpoint](https://api.aotrust.link/notarize)
- [AOTrust PDR verification endpoint](https://api.aotrust.link/v1/pdr/verify)
- [AOTrust public verifier](https://verify.aotrust.link)
- [PDR binary specification](https://github.com/GitSerge-crypto/aotrust-skills/blob/main/pdr-spec.md)
- [Standalone PDR parser](https://github.com/GitSerge-crypto/aotrust-skills/blob/main/pdr_parser.py)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with endpoint details, JSON examples, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces instructions and request examples for notarization and verification workflows; the external service returns PDR receipts and verification results.]

## Skill Version(s):

3.8.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
