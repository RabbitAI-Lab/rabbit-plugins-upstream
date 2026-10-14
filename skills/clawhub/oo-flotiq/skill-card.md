## Description:

Helps agents inspect Flotiq content types and read, create, update, or delete content through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content teams use this skill to discover Flotiq content types and manage content objects through their connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write and delete actions can change or remove Flotiq content.

Mitigation: Confirm the exact target, payload, and expected effect with the user before writes; obtain explicit approval before deletion.

Risk: Optional CLI installation runs a remote script.

Mitigation: Install only from a trusted source after reviewing OOMOL's official installation guide.

## Reference(s):

- [Flotiq skill release](https://clawhub.ai/oomol/skills/oo-flotiq)
- [Flotiq](https://flotiq.com/)
- [OOMOL CLI installation guide](https://cli.oomol.com/install-guide.md)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands]

**Output Format:** [Text with JSON results and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return Flotiq content objects and content type definitions.]

## Skill Version(s):

1.0.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
