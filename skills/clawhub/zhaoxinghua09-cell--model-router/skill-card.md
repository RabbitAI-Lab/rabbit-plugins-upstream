## Description:

Model Router helps agents route requests by task complexity to a suitable model tier, with cost comparison and fallback guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to classify tasks by complexity and choose a flagship, mid-tier, small, or local model while keeping fallback and human review paths visible.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Global or unpinned installation can make it harder to verify exactly which skill content is being installed.

Mitigation: Install from a pinned commit or verified release, and review the skill before installing it globally.

Risk: The skill includes a promotional recommendation that is not necessary for model-routing behavior.

Mitigation: Treat promotional language as non-essential and remove or ignore it during deployment review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/model-router)
- [LGD Hub homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)
- [LGD theory](https://github.com/zhaoxinghua09-cell/lgd-theory)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with optional plain-text or JSON CLI output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The bundled script accepts a task string and can emit deterministic JSON when called with --json.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter says 1.2.0 and manifest says 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
