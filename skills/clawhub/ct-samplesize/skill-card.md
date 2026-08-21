## Description:

Sample size and power calculation tool for clinical trial practitioners that uses a cloud R compute service to cover 49 test types, return publication-grade SVG figures, and provide reproducible R code on request.

This skill is ready for commercial/non-commercial use.

## Publisher:

[medstatstar](https://clawhub.ai/user/medstatstar)

### License/Terms of Use:

MIT

## Use Case:

External clinical trial statisticians, investigators, trial designers, and developers use this skill to select trial-design tests, compute sample size or power, preview cloud compute requests, and generate reproducible code or report-ready outputs for protocol and feasibility work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Aggregate trial-design parameters and host-derived metadata may be sent to the coze cloud service.

Mitigation: Use dry-run or preview first, avoid confidential protocol details or patient-level data unless approved, and use mock or local handling when data must not leave the environment.

Risk: The authoritative security verdict is suspicious because the skill can use an auto-approved endpoint while confirmation behavior is inconsistently described.

Mitigation: Review outbound endpoint configuration and user authorization expectations before deployment, especially in sensitive clinical or enterprise environments.

Risk: Clinical-trial sample-size and power outputs can affect protocol, feasibility, and regulatory decisions.

Mitigation: Have qualified statisticians validate assumptions, formulas, generated code, and final outputs before using them in submissions or regulated workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/medstatstar/skills/ct-samplesize)
- [Project homepage](https://github.com/medstatstar/ct-samplesize)
- [CLI examples](references/cli_examples.md)
- [Data format guide](references/data_format_guide.md)
- [Formula reference](references/formulas.md)
- [Security model](references/security_model.md)
- [Adaptive simulator reference](references/adaptive_simulator.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with calculation summaries, inline code or shell commands, JSON-style stats, and optional SVG or PNG figure artifacts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return bilingual Chinese or English narrative output, reproducible R code on request, dry-run request previews, and publication-grade SVG figures.]

## Skill Version(s):

5.0.0 (source: server release metadata, SKILL.md frontmatter, CHANGELOG top entry)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
