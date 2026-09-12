## Description:

lgd-law-ethic provides an offline LGD Three Laws compliance gate for legal, law-firm, and legal-affairs AI systems, producing self-evaluation scores and a gate decision.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers, compliance reviewers, legal-operations teams, and legal AI builders use this skill to check whether a legal AI system has registration, evidence, and gating controls before it is treated as ready for use. The result is a structured self-assessment and PASS/FAIL gate signal, not professional legal advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Global install instructions are not pinned to a reviewed commit or release.

Mitigation: Install from a pinned, reviewed release and verify the artifact hash before placing the skill in a global agent skills directory.

Risk: A PASS result can be mistaken for authorization to deploy or release a legal AI system.

Mitigation: Treat the result as a preliminary checklist signal and require evidence review plus qualified professional oversight before deployment or release.

Risk: The gate is a checklist heuristic and may miss legal, regulatory, or jurisdiction-specific requirements.

Mitigation: Validate findings against current official requirements and require human review for legal or compliance decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/lgd-law-ethic)
- [LGD Hub homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Plain text or JSON compliance results, plus rubric guidance and shell command examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with no third-party runtime dependencies; uses exit codes 0, 1, and 2 for pass, findings, and usage or environment errors.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
