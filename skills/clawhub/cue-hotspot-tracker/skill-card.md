## Description:

Scans intraday A-share market themes and recent catalysts with Cue, then delivers a dashboard image, a report image, and a link to the full report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Traders and market researchers use this skill to review intraday A-share sector activity, recent catalysts, potential beneficiaries, and reported risks. It produces visual summaries and links to the underlying Cue report; it does not provide investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running cloned or updated external Cue code may execute code that changes after installation.

Mitigation: Install only if you trust the Cue/sensedeal runner source; review updates before running them.

Risk: The workflow uses a local Cue API key for cuecue.cn calls and writes reports under ~/cue-reports.

Mitigation: Create and manage the key yourself; review credential use and report storage before running the skill.

Risk: Scheduled runs may repeatedly execute the workflow with credentials.

Mitigation: Enable scheduling only after approving the exact command, timing, and credential use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/panting09266-ai/skills/cue-hotspot-tracker)
- [Dashboard data schema](artifact/references/sop-schema.md)
- [Cue platform](https://cuecue.cn)

## Skill Output:

**Output Type(s):** [Text, Markdown, Images, Links]

**Output Format:** [PNG dashboard and report images, Markdown report, and Cue report URL; HTML fallback when a compatible browser is unavailable]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are based on intraday A-share data and may include model-summarized fields; not investment advice.]

## Skill Version(s):

1.0.10 (source: server-resolved ClawHub release metadata; skill frontmatter says 1.3.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
