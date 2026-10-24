## Description:

Guides agents through requesting and collecting deterministic simulated-world video from a compatible paid rendering service using an open client and protocol.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nohn3043-arch](https://clawhub.ai/user/nohn3043-arch)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this client to request simulated-world video, handle payment handoff, and collect render artifacts and reproducibility records from a compatible service. The bundled mock service supports testing the protocol without a renderer or real payment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A render service may supply unsafe artifact names that cause writes outside the selected output directory, or mismatched digests.

Mitigation: Use the mock service or a sandbox first; do not make real payments until artifact names are safely constrained and digest mismatches fail closed.

Risk: The recommended payment-capability installation uses an unpinned remote package.

Mitigation: Pin and verify the installer before use, and review the skill and payment flow before connecting a real account.

Risk: An untrusted render endpoint could return malicious or misleading responses.

Mitigation: Use only a trusted compatible service, and review outputs before relying on them.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/nohn3043-arch/skills/second-reality-video)
- [API contract](artifact/references/api.md)
- [Determinism and verification notes](artifact/references/determinism.md)
- [Shot-file specification](artifact/references/shot-files.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Text]

**Output Format:** [Markdown with command examples and structured payment requests]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A compatible service supplies video and verification artifacts; the bundled mock service supplies placeholders, not a rendered film.]

## Skill Version(s):

1.0.1 (source: frontmatter, package.json, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
