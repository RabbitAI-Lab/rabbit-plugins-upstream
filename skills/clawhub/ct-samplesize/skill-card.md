## Description:

Clinical Trial Sample Size & Power helps clinical-trial practitioners compute sample size and power across 49 trial-design scenarios using natural language, cloud R computation, reproducible R code, and publication-grade SVG figures.

This skill is ready for commercial/non-commercial use.

## Publisher:

[medstatstar](https://clawhub.ai/user/medstatstar)

### License/Terms of Use:

MIT

## Use Case:

External clinical-trial practitioners, clinicians, medical students, and statistical teams use this skill to select trial-design methods and compute defensible sample-size, power, curve, and figure outputs from aggregate design parameters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Normal compute commands may send trial-design parameters, locale, and a stable hostname hash to a cloud endpoint.

Mitigation: Use --dry-run explicitly before computation and avoid confidential protocol details unless extracted design parameters may leave the machine.

Risk: The remote service may return URLs that the skill can fetch or follow.

Mitigation: Restrict response-followed URLs to trusted hosts and review network behavior before deployment.

Risk: Generated sample-size, power, and figure outputs may be used in regulated clinical-trial decisions.

Mitigation: Treat outputs as reference material and validate calculations before protocol, SAP, or regulatory submission use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/medstatstar/skills/ct-samplesize)
- [Project homepage from release metadata](https://github.com/medstatstar/ct-samplesize)
- [README](README.md)
- [Chinese README](README_zh-CN.md)
- [Routing menu](references/menu.md)
- [CLI examples](references/cli_examples.md)
- [Security model](references/security_model.md)
- [Default figures specification](references/default_figures.md)
- [Advanced reference](docs/ADVANCED.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Bilingual Markdown with numeric results, reproducible R code, command previews, and optional SVG or PNG figure files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses aggregate trial-design parameters; optional figures are written to the configured output directory.]

## Skill Version(s):

5.6.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
