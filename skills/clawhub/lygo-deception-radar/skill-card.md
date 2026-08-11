## Description:

LYGO Deception Radar rebuilds an anonymized radar feed and static HTML dashboard from public labeled discourse samples, showing strong, weak calibration, and clear bands at an operational threshold of 0.65.

This skill is ready for commercial/non-commercial use.

## Publisher:

[deepseekoracle](https://clawhub.ai/user/deepseekoracle)

### License/Terms of Use:

MIT No Attribution (MIT-0)

## Use Case:

Developers and analysts use this skill to rebuild a public-sample Ops Detector proof dashboard and inspect anonymized discourse-signal bands. It is intended for public labeled samples only, not private communications, doxing, or person-level verdicts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Dashboard bands or scores could be misread as verdicts about real people or private communications.

Mitigation: Use public labeled samples only, keep outputs anonymized, and treat weak calibration bands as ranking signals rather than production alerts or person-level findings.

Risk: The builder can import a nearby Ops Detector module from local paths or LYGO_STACK_ROOT.

Mitigation: Point LYGO_STACK_ROOT only at a trusted LYGO checkout and review any external labeled suite before using it.

Risk: Generated JSON or HTML could expose unsuitable content if private or identifying samples are provided.

Mitigation: Review inputs and generated static files before publishing, and avoid private mail, private logs, or person-identifying datasets.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/deepseekoracle/skills/lygo-deception-radar)
- [Project homepage from ClawHub metadata](https://github.com/DeepSeekOracle/lygo-protocol-stack/tree/main/docs/skills/lygo-deception-radar)
- [Live Deception Radar dashboard](https://deepseekoracle.github.io/lygo-protocol-stack/deception-radar/)
- [Security notes](references/SECURITY.md)

## Skill Output:

**Output Type(s):** [Files, JSON, HTML, Shell commands, Guidance]

**Output Format:** [Markdown guidance with bash commands; generated radar_feed.json and static HTML when scripts run]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are based on public labeled samples and include anonymized sample ids, text previews, scores, bands, and summary stats.]

## Skill Version(s):

1.0.0 (source: frontmatter, claw.json, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
