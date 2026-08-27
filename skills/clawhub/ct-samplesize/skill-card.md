## Description:

ct-samplesize helps clinical-trial practitioners calculate sample size and power across 49 trial-design scenarios using a remote Coze R compute service, with bilingual results, publication-grade SVG figures, and optional reproducible R code.

This skill is ready for commercial/non-commercial use.

## Publisher:

[medstatstar](https://clawhub.ai/user/medstatstar)

### License/Terms of Use:

MIT

## Use Case:

External clinical trial statisticians, investigators, trial designers, medical and regulatory affairs teams, publication authors, students, and methodologists use this skill to plan protocols, SAPs, feasibility assessments, and audit trails by calculating aggregate sample-size and power scenarios without installing local R.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live calculations can send trial-design parameters, a stable hostname hash, and locale to cloud endpoints.

Mitigation: Use preview or mock mode, inspect the payload before live computation, and avoid cloud computation for confidential protocols unless the user explicitly approves the specific payload.

Risk: The security assessment notes inconsistent preview and consent behavior around outbound computation.

Mitigation: Require first-use outbound disclosure and prefer dry-run inspection before triggering remote compute on pre-approved endpoints.

Risk: Clinical-trial sample-size and power outputs may affect protocol or regulatory decisions.

Mitigation: Have a qualified statistician validate assumptions, formulas, generated code, and results before protocol, SAP, publication, or regulatory use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/medstatstar/skills/ct-samplesize)
- [Project homepage](https://github.com/medstatstar/ct-samplesize)
- [CLI examples](artifact/references/cli_examples.md)
- [Data format guide](artifact/references/data_format_guide.md)
- [Formulas](artifact/references/formulas.md)
- [Security model](artifact/references/security_model.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown responses with numeric results, JSON request previews, inline SVG or PNG figure outputs, and optional R code blocks.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write figures to CTSS_OUTPUT_DIR; live cloud calculations can send aggregate trial-design parameters, a stable hostname hash, and locale.]

## Skill Version(s):

5.1.0 (source: SKILL.md frontmatter, CHANGELOG, and server release metadata; released 2026-08-22)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
