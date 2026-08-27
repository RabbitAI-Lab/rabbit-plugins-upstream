## Description:

Multi-agent deep review for code PRs that orchestrates GitHub Copilot and parallel subagents with scope-based escalation, stale-finding triage, and a hard iteration cap.

This skill is ready for commercial/non-commercial use.

## Publisher:

[conorbronsdon](https://clawhub.ai/user/conorbronsdon)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to perform deeper pull request review by combining line-level review with adversarial, operational, and reference-comparison analysis. It is intended for non-trivial or high-stakes code changes where a single review pass may miss architectural or production risks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Ordinary code review phrasing may invoke the workflow unintentionally.

Mitigation: Confirm the review target and desired review depth before adding reviewers or taking repository actions.

Risk: The workflow can involve GitHub reviewer assignment, pushes, or issue creation in shared repositories.

Mitigation: Keep external state changes confirmation-gated and verify the current HEAD before acting on stale findings.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/conorbronsdon/skills/cot-code-review)
- [README](README.md)
- [Subagent prompt templates](patterns/subagent-prompts.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown review findings with inline shell commands and action guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May request GitHub reviewer assignment, pushes, or issue creation; external state changes are confirmation-gated by the skill workflow.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
