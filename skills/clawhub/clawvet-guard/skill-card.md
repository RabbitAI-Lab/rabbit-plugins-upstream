## Description:

Scan a third-party agent skill with ClawVet and act on its grade before installing, enabling, or running it. Use when the user asks to scan, vet, or check a skill they did not write, or whether a skill from ClawHub or another untrusted source is safe to install.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mohibshaikh](https://clawhub.ai/user/mohibshaikh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to assess third-party agent skills before installing, enabling, or running them. It guides local and remote ClawVet scans and explains how to interpret scan coverage, recommendations, and findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An unpinned ClawVet invocation could use a changing upstream version.

Mitigation: Review the dependency before installation and use an installed, verified ClawVet version as the skill directs.

Risk: The supplied scan had partial coverage because two local path-like references were unresolved, so its evidence is incomplete.

Mitigation: Resolve the references and confirm complete scan coverage before relying on the result to install or enable a skill.

## Reference(s):

- [ClawVet repository](https://github.com/MohibShaikh/clawvet)
- [ClawHub skill page](https://clawhub.ai/mohibshaikh/skills/clawvet-guard)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.0.7 (source: server-resolved release, frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
