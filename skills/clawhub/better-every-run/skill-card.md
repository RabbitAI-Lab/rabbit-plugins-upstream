## Description:

Better Every Run: capture explicit /ber corrections, review them, and promote only the lessons that deserve durable memory, skill rules, or evals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[leostehlik](https://clawhub.ai/user/leostehlik)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to capture explicit corrections, review lesson proposals, and promote only selected lessons into durable memory, skill behavior, or eval fixtures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local correction logs may contain private workspace context if users intentionally capture it.

Mitigation: Review .better-every-run contents before sharing a project and never publish local lessons, event logs, or private corrections.

Risk: A poor correction could become durable memory, skill behavior, or eval coverage if promoted without review.

Mitigation: Use the lesson card and promotion flow only for lessons that should persist; require a stable target hash and clean scanner verdict before durable writes.

Risk: Direct durable writes from capture commands could bypass review if allowed.

Mitigation: The skill blocks direct --target writes for fix and remember, retires apply-memory-patch, and routes eval durability through eval-fixture under tests/ or evals/.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/leostehlik/skills/better-every-run)
- [Better Every Run Workflow](references/workflow.md)
- [Report Template](references/report-template.md)
- [Upstream Loop Demo](examples/upstream-loop.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown chat summaries with inline shell commands, local markdown lesson cards, and JSON or JSONL eval fixtures when explicitly promoted.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Normal fix and remember actions record local evidence only; durable memory, skill, or eval outputs require the reviewed promotion flow.]

## Skill Version(s):

0.5.7 (source: SKILL.md frontmatter and evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
