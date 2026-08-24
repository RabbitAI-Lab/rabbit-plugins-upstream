## Description:

Instinct-based learning system for OpenClaw that analyzes scoped session history, detects behavior and error patterns, creates confidence-scored learnings, and suggests optimizations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[adelpro](https://clawhub.ai/user/adelpro)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to analyze OpenClaw session history, identify recurring patterns or errors, and produce bounded learning suggestions for self-improving automation workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Session-history analysis can expose sensitive workflow details if run broadly or retained longer than intended.

Mitigation: Use --agent for narrow review, reserve --all for intentional broad scans, inspect generated memory/learning files, and run prune when stored learning data should be deleted.

Risk: Learning suggestions may be incorrect or may overfit to recent sessions if applied without review.

Mitigation: Review optimization and instinct outputs before changing agent behavior, and do not let high-confidence suggestions modify agents without human approval.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/adelpro/skills/continue-learning)
- [Artifact README](artifact/README.md)
- [Artifact Skill Definition](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [text, configuration, guidance]

**Output Format:** [CLI text reports with JSON and JSONL learning files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js. Analysis is scoped with --agent or --all, stores redacted bounded summaries, and supports pruning stored learning data.]

## Skill Version(s):

1.3.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
