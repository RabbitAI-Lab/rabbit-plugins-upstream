## Description:

A distilled meta-skill for analyzing agent cognitive architecture as a directed graph, diagnosing architecture issues, proposing restructuring actions, and adding self-verification, reflection, orchestration, and learning loops.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent engineers use this skill to inspect an agent architecture, detect cycles, bottlenecks, orphan modules, duplicate roles, and missing roles, then produce restructuring guidance with a health-score check. It is also intended to support self-reflection and local learning across repeated architecture review tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local learner can retain invocation notes in learned_patterns.json.

Mitigation: Do not pass secrets, credentials, or private prompt text as learner notes; review or delete learned_patterns.json when retained local history is not desired.

Risk: The skill is distilled from a teacher skill and may not cover all implicit teacher knowledge.

Mitigation: Review key restructuring decisions against the original teacher skill or other authoritative architecture guidance before relying on high-impact changes.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qq435912743/skills/meta-cognitive-architecture-reconstruct)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, guidance]

**Output Format:** [Markdown guidance with optional JSON diagnostic output from the bundled Python scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The learner script can create or update a local learned_patterns.json file when invoked.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
