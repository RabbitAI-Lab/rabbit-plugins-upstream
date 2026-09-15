## Description:

Helps agents evaluate AI claims by organizing supplied evidence by source type, independent verifiability, credibility, and support level without deciding whether the claim is true.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers, analysts, and agent users use this skill to structure claim-checking workflows, score whether submitted evidence is independently verifiable, and identify claims that should not be treated as supported conclusions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented global installation path can fetch mutable, unpinned remote content.

Mitigation: Review the exact source commit before installation and prefer a pinned version or verified checksum.

Risk: The tool scores evidence quality but does not determine whether a claim is true.

Mitigation: Treat output as decision support and have a human review original sources before relying on a conclusion.

Risk: Internal or assertion-based evidence may be insufficiently verifiable.

Mitigation: Require official, paper, or data evidence for higher-confidence conclusions and mark unsupported claims as not ready for conclusion.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zhaoxinghua09-cell/skills/evidence-chain-builder)
- [LGD Hub Homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown or JSON evidence-chain assessment with command-line usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Deterministic local output; returns rc=0 for pass, rc=1 for detected support issues, and rc=2 for usage or environment errors.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata and artifact manifest; artifact SKILL.md frontmatter says 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
