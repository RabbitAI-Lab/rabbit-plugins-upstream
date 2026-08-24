## Description:

Zero-exposure cross-device script authorization using MGC Blackbox seal functionality, where scripts are encrypted with a target node's RSA public key, transferred as ciphertext, and decrypted only during execution on the authorized node.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zkeviny](https://clawhub.ai/user/zkeviny)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to seal, transfer, store, and run MGC Blackbox scripts across devices without exposing plaintext script content. It is intended for cross-organization script sharing, trusted partner automation, and delegated task execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sealed scripts are opaque to the receiving agent and can execute unreviewable code on the target machine.

Mitigation: Only run sealed scripts from independently trusted parties, confirm provenance through a separate mechanism, and execute under a least-privilege or sandboxed account.

Risk: The documented capsule transfer flow protects confidentiality but does not by itself prove integrity.

Mitigation: Verify capsule integrity out of band and use a trusted transfer channel before storing or running the sealed script.

Risk: Overwrite workflows can replace an existing same-name script without enough operator review.

Mitigation: Avoid overwrite-by-default use, check the target script identifier before saving, and require explicit approval when replacing an existing sealed script.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zkeviny/skills/cross-node-script-auth)
- [MGC Blackbox Repository](https://github.com/zkeviny/MGC-Blackbox)
- [MGC Blackbox Issues](https://github.com/zkeviny/MGC-Blackbox/issues)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Python and JSON code blocks and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only skill; generated guidance may include MGC tool calls and local execution steps.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter reports 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
