## Description:

Native Autonomous Discovery helps an agent run an open-ended hypothesis, experiment, evidence-scoring, and convergence loop over a candidate search space using a user-provided observer.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill when an open-ended problem needs autonomous hypothesis generation, experiment selection, evidence scoring, pruning, and best-effort convergence reporting. It is suited to local workflows where the observer function and search space are supplied by the user.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores local preference and history data in learned_patterns.json.

Mitigation: Avoid recording sensitive notes or personal data, and review retained local memory before sharing or publishing the skill directory.

Risk: The skill asks the agent to update skill instructions based on accumulated experience.

Mitigation: Require human review before allowing automatic SKILL.md edits or accepting proposed instruction changes.

Risk: Discovery quality depends on the supplied observer and search budget, so biased observations or insufficient sampling can produce misleading convergence.

Mitigation: Validate observer behavior, set an appropriate sampling budget, and treat low-confidence or non-converged results as best-effort rather than final conclusions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qq435912743/skills/native-autonomous-discovery)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Discovery results include the best hypothesis, confidence, round count, convergence flag, and evidence trajectory.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
