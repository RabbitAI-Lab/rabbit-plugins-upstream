## Description:

Scans a skills directory for missing self-improvement scaffolding, invalid YAML frontmatter, or missing learner modules, then proposes and can apply sandbox-tested patches with audit logging.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill maintainers use this skill to scan installed skill directories, review proposed improvements, and optionally apply bounded patches that add learner support, self-evolution sections, or basic YAML frontmatter.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can rewrite or augment other installed skills when apply mode is used.

Mitigation: Run scan and propose first, use apply only on a small backed-up test skill directory, and review diffs before deploying changed skills.

Risk: The security summary states that write behavior is broader and less safely bounded than the documentation claims.

Mitigation: Treat apply mode as a privileged maintenance action and restrict it to skill directories where file changes are expected and recoverable.

Risk: The learner component can record preferences in learned_patterns.json.

Mitigation: Avoid recording personal or sensitive preferences unless retaining them in the skill directory is acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qq435912743/skills/recursive-self-improve)
- [Publisher profile](https://clawhub.ai/user/qq435912743)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and command-line text, with JSON memory files written by the skill scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can modify files under a selected skills directory when apply mode is used.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
