## Description:

Helps an agent recognize validated corrections, feature requests, knowledge gaps, and resolved errors, then maintain reusable local knowledge and experience notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zzusp](https://clawhub.ai/user/zzusp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to preserve confirmed, reusable learning from corrections, stable capability expectations, verified knowledge gaps, and resolved errors in a local knowledge store.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive, customer, credential, or confidential information could be preserved in the local ~/.agent-knowledge/ memory store if users allow it into memory entries.

Mitigation: Review entries before saving and redact sensitive personal, customer, credential, and confidential data.

Risk: Unverified corrections or unresolved failures could become misleading future guidance.

Mitigation: Save only entries backed by explicit confirmation, authoritative evidence, or a converged diagnosis, and leave unsupported observations out of the knowledge store.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zzusp/skills/evolve-self-improving)
- [Publisher profile](https://clawhub.ai/user/zzusp)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown files and shell validation commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes local knowledge and experience entries under ~/.agent-knowledge/ only when evidence and validation criteria are met.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
