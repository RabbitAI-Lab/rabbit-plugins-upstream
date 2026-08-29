## Description:

Sample size and power calculation tool for clinical trial practitioners, using a remote Coze R compute service for 49 test types with publication-grade SVG figures and bilingual Chinese or English output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[medstatstar](https://clawhub.ai/user/medstatstar)

### License/Terms of Use:

MIT-0

## Use Case:

Clinical-trial practitioners, clinicians, students, and statistical or regulatory staff use this skill to choose sample-size or power methods, calculate trial design parameters across common and advanced designs, and produce auditable reports, figures, and optional reproducible R code.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send trial-design parameters and a hostname-derived identifier to preapproved cloud endpoints without a reliably enforced confirmation.

Mitigation: Use --dry-run or CTSS_COZE_MOCK=1 for preview or local demo, review or remove auto-approved endpoints when explicit prompts are required, and send only non-confidential aggregate design parameters.

Risk: Bug-report descriptions are user-authored free text and may accidentally include confidential protocol details or identifiable information.

Mitigation: Review bug-report text before submission and omit identifiable people, institutions, subjects, or confidential protocol content.

Risk: Clinical sample-size and power outputs may be incorrect or insufficient for regulated submissions if assumptions or inputs are wrong.

Mitigation: Treat results as reference material and have a qualified statistician validate assumptions, inputs, and outputs before protocol, SAP, feasibility, or regulatory use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/medstatstar/skills/ct-samplesize)
- [Project Homepage](https://github.com/medstatstar/ct-samplesize)
- [README](README.md)
- [Command-Line Examples](references/cli_examples.md)
- [Security Model](references/security_model.md)
- [Formula Reference](references/formulas.md)
- [Report Template](references/report_template.md)
- [Adaptive Simulator](references/adaptive_simulator.md)
- [Data Format Guide](references/data_format_guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, files, guidance]

**Output Format:** [Markdown responses with optional R code blocks, JSON request previews, and generated SVG or HTML report files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return bilingual explanations, sample-size or power results, sensitivity curves, publication-grade SVG figures, and safe-preview request envelopes.]

## Skill Version(s):

5.3.14 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
