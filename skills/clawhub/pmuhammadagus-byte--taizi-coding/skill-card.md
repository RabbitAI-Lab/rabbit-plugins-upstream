## Description:

Taizi Coding helps agents remember explicitly confirmed coding preferences, store them locally, and apply them to future coding responses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pmuhammadagus-byte](https://clawhub.ai/user/pmuhammadagus-byte)

### License/Terms of Use:

MIT

## Use Case:

Developers and coding agents use this skill to capture explicit coding style, stack, and structure preferences after user confirmation, then apply or query those preferences in later coding work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Preference memory could store unwanted or incorrect coding guidance if updated without deliberate user approval.

Mitigation: Store preferences only after explicit confirmation, keep entries concise, and approve writes to ~/coding/ deliberately.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/pmuhammadagus-byte/skills/taizi-coding)
- [Publisher Profile](https://clawhub.ai/user/pmuhammadagus-byte)
- [criteria.md](artifact/criteria.md)
- [dimensions.md](artifact/dimensions.md)
- [memory-template.md](artifact/memory-template.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands and local preference-file guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose local writes under ~/coding/ only after explicit user approval.]

## Skill Version(s):

1.0.4 (source: metadata.openclaw.version and release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
