## Description:

Scans a local skill ecosystem for invalid frontmatter, Python syntax errors, stale skills, near-duplicate skill descriptions, and orphaned meta-skills, then reports health findings for repair, merge, or retirement decisions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent maintainers use this skill to audit a skill directory before release or during periodic ecosystem maintenance. It helps identify broken, stale, duplicate, or orphaned skills that may need repair, consolidation, or removal.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The main audit path reads local skill directories and may expose skill contents in generated findings.

Mitigation: Run it only against intended skill roots and review the target path before execution.

Risk: The bundled learner.py tool can write persistent usage, error, note, and preference data into skill directories.

Mitigation: Prefer the main ecosystem_auditor.py audit path unless persistent local learning state is explicitly desired.

Risk: Staleness and near-duplicate findings are heuristic and may produce false positives or miss issues.

Mitigation: Treat audit results as triage signals and review findings before repairing, merging, or retiring skills.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/qq435912743/skills/ecosystem-auditor)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [JSON health report with a concise human-readable summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports broken, stale, duplicate, and orphaned skills; learner.py can persist local usage, error, note, and preference data when explicitly invoked.]

## Skill Version(s):

1.0.0 (source: frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
