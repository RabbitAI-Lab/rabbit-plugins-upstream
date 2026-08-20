## Description:

Zhongkui Skill helps agents review agent skills for security risks through static audit, behavior-simulation guidance, and supply-chain provenance checks, then returns a structured security verdict.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ebandao777-oss](https://clawhub.ai/user/ebandao777-oss)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security reviewers use this skill to inspect an agent skill directory before installation or release. It supports quick static checks and structured review reports for suspicious or malicious skill behavior.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads files from a user-supplied skill directory as part of its review workflow.

Mitigation: Run it only on explicit skill directories and avoid broad private folders or unrelated workspaces.

Risk: The security verdict is heuristic and may not fully match the broader behavior-simulation and supply-chain claims in the documentation.

Mitigation: Treat results as review assistance and require human security review before installation, release, or blocking decisions.

Risk: The artifact frontmatter version differs from the server release version.

Mitigation: Use the server release version for this card and verify version alignment during release review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ebandao777-oss/skills/zhongkui-skill)
- [Server-resolved source repository](https://github.com/ebandao777-oss/zhongkui-skill)
- [README](README.md)
- [Quickstart](QUICKSTART.md)
- [Technical reference](REFERENCE.md)
- [Static audit checklist](references/static-audit.md)
- [Risk taxonomy](references/risk-taxonomy.md)
- [Behavioral emulation scenarios](references/behavioral-emulation.md)
- [Supply-chain review](references/supply-chain.md)
- [Scoring and verdicts](references/scoring.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown security verdict report with tables and optional shell command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include a verdict, score, short conclusion, deductions with file and line references, and review guidance.]

## Skill Version(s):

1.0.3 (source: ClawHub release metadata; artifact frontmatter reports 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
