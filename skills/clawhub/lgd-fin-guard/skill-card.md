## Description:

lgd-fin-guard helps agents assess finance and licensed-institution AI systems against LGD registered, evidenced, and gated compliance checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers, compliance teams, and agents use this skill to run a local self-assessment for finance AI systems such as investment advisory, risk-control, and anti-money-laundering workflows. It produces structured gate results and missing-evidence prompts for human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented install path uses an unpinned remote CLI and global installation from a mutable repository.

Mitigation: Install only reviewed lgd-fin-guard files from an immutable commit or release, and verify contents before adding the skill to a global agent skills directory.

Risk: Finance compliance checklist results may be incomplete or outdated for a specific regulated deployment.

Mitigation: Use the output as structured self-check guidance only; require human review and current official regulatory or licensed professional guidance before decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/lgd-fin-guard)
- [Project homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Plain text or JSON, with Markdown instructions and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Deterministic local output with exit codes rc=0, rc=1, or rc=2]

## Skill Version(s):

1.0.0 (source: server release metadata and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
