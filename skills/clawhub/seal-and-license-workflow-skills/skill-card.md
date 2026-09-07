## Description:

Seal skill packages and workflow folders so they execute only on authorized nodes -- no read, no modify, no resell -- using local, single-node-bound MGC Blackbox delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zkeviny](https://clawhub.ai/user/zkeviny)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and workflow authors use this skill to package, seal, license, and deliver MGC-backed skill or workflow folders for execution on a specific authorized node without exposing implementation files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill normalizes running opaque received code without enough documented verification or sandboxing controls.

Mitigation: Review before installing or using the skill, run sealed capsules only from trusted publishers, and prefer a sandboxed or low-privilege environment.

Risk: Capsule provenance, signatures, capabilities, and dependency versions may be unclear to consumers.

Mitigation: Ask the publisher how capsule signatures, provenance, capabilities, and dependency versions are verified before executing a sealed package.

Risk: The optional node_pub trial request links a persistent public identifier with contact information.

Mitigation: Do not email private keys, tokens, secrets, or credentials; treat node_pub sharing as disclosure of a persistent public identifier.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zkeviny/skills/seal-and-license-workflow-skills)
- [MGC Blackbox Repository](https://github.com/zkeviny/MGC-Blackbox)
- [MGC Blackbox Issues](https://github.com/zkeviny/MGC-Blackbox/issues)
- [Artifact README](artifact/README.md)
- [Artifact Skill Definition](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [Markdown with inline Python and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill produces procedural author-side and consumer-side instructions for MGC Blackbox package sealing, import, discovery, and execution.]

## Skill Version(s):

1.0.0 (source: server release metadata, artifact frontmatter, manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
