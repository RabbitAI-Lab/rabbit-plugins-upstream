## Description:

Scan a third-party agent skill with ClawVet and act on its grade before installing, enabling, or running it. Use when the user asks to scan, vet, or check a skill they did not write, or whether a skill from ClawHub or another untrusted source is safe to install.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mohibshaikh](https://clawhub.ai/user/mohibshaikh)

### License/Terms of Use:

MIT

## Use Case:

Developers use ClawVet Guard to assess third-party agent skills before installation, enabling, or execution. It interprets the scan status, coverage, recommendation, and findings to guide the next step.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence notes a version-unpinned npx clawvet reference, which leaves the executed package version uncertain.

Mitigation: Use an installed, reviewed ClawVet version and confirm its version before scanning.

Risk: Two local path-like references were unresolved, so the scan was marked partial and leaves uncertainty about those references.

Mitigation: Resolve the referenced paths and stage the full skill locally before relying on scan results.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/mohibshaikh/skills/clawvet-guard)
- [ClawVet project](https://github.com/MohibShaikh/clawvet)

## Skill Output:

**Output Type(s):** [JSON, Markdown, Shell commands, Guidance]

**Output Format:** [ClawVet JSON scan results and a concise Markdown assessment with findings and recommended next steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include shell commands for local or remote scanning.]

## Skill Version(s):

1.0.9 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
