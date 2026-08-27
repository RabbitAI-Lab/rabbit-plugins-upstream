## Description:

Audit the whole repo for Thompson-mode violations. A ranked list of what to rewrite, delete, or take back into the trusted base.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rajnandan1](https://clawhub.ai/user/rajnandan1)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to audit a repository for Thompson-mode method violations and rank candidates for rewrite, deletion, or removal from the trusted base. It produces recommendations only and does not apply changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent may read repository files and git history to produce audit recommendations.

Mitigation: Install only for repositories where that level of read access is acceptable.

Risk: The skill's scope excludes correctness, security, and performance review.

Mitigation: Route those issues to a separate normal review pass before acting on recommendations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/rajnandan1/skills/ken-audit)
- [Publisher profile](https://clawhub.ai/user/rajnandan1)
- [Project homepage](https://github.com/rajnandan1/ken)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with ranked one-line findings and a summary line]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings use tags such as rot, layer, unvouched, fancy, and ceremony; the skill lists recommendations and applies no changes.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
