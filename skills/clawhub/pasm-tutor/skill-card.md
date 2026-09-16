## Description:

Learning tutor agents built on PASM that track per-topic mastery, select weak topics for practice, give encouraging next-step responses, and export machine-readable learning snapshots offline.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arronjack](https://clawhub.ai/user/arronjack)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, educators, and learning-product teams use this skill to add adaptive tutoring behavior that tracks knowledge-point mastery, recommends the next topic to practice, and returns structured student-progress snapshots.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on external pasm-agents and pasm-skills packages that are unreviewed and unpinned in the evidence.

Mitigation: Review both packages before installation, install in a virtual environment, and pin a known version or commit.

Risk: Tutor state may contain sensitive student learning data if deployed with real learners.

Mitigation: Avoid storing sensitive student information unless the deployment owner has reviewed where state is saved and how it can be deleted.

Risk: Mastery tracking does not include a built-in forgetting curve, so stale knowledge may remain overestimated after long gaps.

Mitigation: Use explicit reassessment or scheduled lower-score reports when recency decay is required.

Risk: Memory recall uses literal matching rather than semantic retrieval, so paraphrased mistakes may not be recalled reliably.

Mitigation: Use consistent topic tags and validate recall behavior for the target curriculum before relying on cross-attempt mistake association.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/arronjack/skills/pasm-tutor)
- [PASM Agents project homepage](https://github.com/arronJack/pasm-agents)
- [PASM Skills tutorial](https://github.com/arronJack/pasm-skills/blob/master/docs/TUTORIAL.md)
- [PASM Agents Gitee install source](https://gitee.com/arronzheng/pasm-agents)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration, JSON]

**Output Format:** [Markdown with Python examples, shell commands, and JSON-compatible learning snapshots]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can produce offline tutor replies, next-topic recommendations, mastery values, and persisted student snapshots.]

## Skill Version(s):

0.4.9 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
