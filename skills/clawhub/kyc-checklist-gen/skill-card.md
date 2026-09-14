## Description:

Generates personal or corporate KYC document checklists and checks completeness, failing when required items are missing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

External users, compliance teams, and developers use this skill as a local pre-screening aid to list personal or corporate KYC materials, mark provided items, and identify missing documents before official or professional review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented installation path can fetch and globally install mutable remote code instead of the reviewed artifact.

Mitigation: Install from a reviewed, pinned release or exact commit, and avoid global installation unless all relevant agents should load the skill.

Risk: The generated KYC checklist may not reflect current official requirements for a specific institution or jurisdiction.

Mitigation: Treat the checklist as a local aid and verify requirements against current official sources and professional review before relying on it.

Risk: KYC materials can involve sensitive personal or business information.

Mitigation: Use the skill locally with the minimum necessary information and avoid storing or sharing sensitive material in agent transcripts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/kyc-checklist-gen)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Plain text checklist or JSON object; agent responses may summarize results in Markdown.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Deterministic local output with rc=0 for complete, rc=1 for missing items, and rc=2 for usage or environment errors.]

## Skill Version(s):

1.0.0 (source: server release metadata, manifest.json, README.md; SKILL.md frontmatter says 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
