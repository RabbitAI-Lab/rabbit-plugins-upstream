## Description:

Analyzes turtle or snake egg images or videos from an incubator to classify visible shell, vascular, embryo, mold, and reliability signals and produce an incubation progress report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Breeders, hobbyists, and smart-incubator operators use this skill to analyze macro or candling media, track egg development by egg ID, identify unreliable observations or warning signs, and generate progress reports. Important breeding decisions should also consider species-specific incubation guidance, temperature and humidity logs, and qualified reptile breeding or veterinary advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded egg images or videos are sent to the configured analysis service.

Mitigation: Use only media approved for that processing path and review or change the configured endpoint before deployment.

Risk: The skill can create or reuse a local identity and store tokens in the workspace data directory.

Mitigation: Run it only in workspaces where this account-linking behavior is intended, and avoid workspaces containing sensitive identity files.

Risk: The scanner verdict is suspicious because remote or private-network services may be used without clear user confirmation.

Mitigation: Require operator review of service configuration and data-flow expectations before installation or execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-egg-incubation-monitoring-analysis)
- [Publisher profile](https://clawhub.ai/user/18072937735)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface reference](references/api_doc.md)
- [SMYX analysis API reference](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance]

**Output Format:** [Markdown or JSON reports with analysis status, visible incubation signals, alert level, recommended actions, disclaimers, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write the report to a requested output file and may query historical reports through the configured service.]

## Skill Version(s):

1.0.10 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
