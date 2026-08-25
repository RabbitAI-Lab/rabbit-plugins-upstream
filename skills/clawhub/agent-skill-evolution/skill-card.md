## Description:

Helps agents evolve OpenClaw skills with benchmarking, red-teaming, regression protection, rollback safety, and continuous improvement loops.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pmuhammadagus-byte](https://clawhub.ai/user/pmuhammadagus-byte)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent maintainers use this skill to evaluate and improve OpenClaw skills through baseline measurement, candidate design, testing, red-team checks, regression comparison, and deployment review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Skill evolution proposals can affect shared, production, security-critical, credential-related, financial, or destructive workflows.

Mitigation: Require explicit human review before applying high-impact changes, and keep the skill's rollback and regression-protection workflow in place.

Risk: A candidate skill change can appear successful because files changed even when capability, reliability, or safety did not improve.

Mitigation: Use baseline benchmarks, golden tests, red-team cases, and regression comparison before deployment.

## Reference(s):

- [Skill definition](artifact/SKILL.md)
- [README](artifact/README.md)
- [ClawHub skill page](https://clawhub.ai/pmuhammadagus-byte/skills/agent-skill-evolution)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with checklists, runbooks, and optional code or shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include benchmark plans, regression checks, red-team scenarios, rollback recommendations, and approval gates.]

## Skill Version(s):

1.0.1 (source: frontmatter, release metadata, _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
