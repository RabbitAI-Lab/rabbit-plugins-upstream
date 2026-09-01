## Description:

Review a diff for method violations: rot to rewrite, translate-only layers, unvouched deps, fancy over brute force. One line per finding.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rajnandan1](https://clawhub.ai/user/rajnandan1)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to review diffs for narrow method violations such as repeated patching, unnecessary layers, unvouched dependencies, over-complex algorithms, and process ceremony.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat ken-review findings as a complete code review even though the skill excludes correctness, security, and performance issues.

Mitigation: Use ken-review only for its narrow method-violation scope and run a normal review pass when broader correctness, security, or performance issues matter.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/rajnandan1/skills/ken-review)
- [Project homepage](https://github.com/rajnandan1/ken)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Plain text or Markdown review findings, usually one line per finding with an optional net summary.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Does not apply fixes; reports findings only.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
