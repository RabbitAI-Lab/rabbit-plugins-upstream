## Description:

Audits public websites for answer-engine readiness and produces an evidence-backed score with prioritized fixes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aureliusclaw](https://clawhub.ai/user/aureliusclaw)

### License/Terms of Use:

MIT-0

## Use Case:

Website owners, content teams, and developers use this skill to check whether public pages are accessible, readable, and quotable by answer engines, then prioritize improvements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A local engine override can execute arbitrary Python if an untrusted party controls the runtime environment or nearby plugin files.

Mitigation: Install and run in a trusted environment; restrict who can set the engine override or modify plugin files.

Risk: Saved reports may be written to an unintended directory.

Mitigation: Check the report output directory and its permissions before enabling saved reports.

Risk: English-biased quotability scoring and technical checks may overstate real-world citation readiness.

Mitigation: Treat scores as diagnostic guidance, not proof of citations; review non-English pages and crawler access separately.

## Reference(s):

- [geo-scan ClawHub release](https://clawhub.ai/aureliusclaw/skills/geo-scan)
- [Project homepage listed in skill metadata](https://github.com/AureliusClaw/geo-scan)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Markdown, JSON]

**Output Format:** [Markdown report and JSON scan results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a 0–100 score, per-axis evidence, sampled pages, and prioritized actions; reports can be saved to disk.]

## Skill Version(s):

1.2.0 (source: frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
