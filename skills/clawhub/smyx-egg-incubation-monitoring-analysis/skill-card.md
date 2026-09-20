## Description:

Analyzes fixed-camera images or video of turtle or snake eggs to classify shell, vascular, embryo, and incubation-stage signals and produce an incubation progress report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External reptile breeders, incubator operators, and hobbyist keepers use this skill to review egg imagery, monitor fertilization and development signals, generate progress reports, and query prior reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security verdict is suspicious because the skill can silently create or reuse a cloud identity, store tokens locally, and send selected media, URLs, report history, and an internal identity to the vendor service.

Mitigation: Review account behavior and data handling before deployment; use the skill only where sending those inputs to the vendor service is acceptable.

Risk: Default development transport settings may use plaintext HTTP endpoints.

Mitigation: Fix or override development configuration to trusted HTTPS endpoints before use.

Risk: The skill produces breeding-stage classifications and handling guidance that could affect animal welfare if overstated or used without review.

Mitigation: Treat results as visual-analysis support, confirm important decisions against species incubation guidance and logs, and avoid invasive or automated environment-control actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-egg-incubation-monitoring-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-like structured analysis text, with shell commands for invoking analysis and history lookup.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report links, alert levels, recommended actions, and optional saved output files.]

## Skill Version(s):

1.0.13 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
