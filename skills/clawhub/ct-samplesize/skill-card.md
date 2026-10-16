## Description:

Helps clinical-trial practitioners estimate sample size and statistical power across trial designs using a cloud R calculation service, with bilingual results, figures, and reproducible R code.

This skill is ready for commercial/non-commercial use.

## Publisher:

[medstatstar](https://clawhub.ai/user/medstatstar)

### License/Terms of Use:

MIT

## Use Case:

Clinical-trial researchers, clinicians, and statisticians use this skill to plan sample sizes, evaluate statistical power, and examine design assumptions for trial protocols and feasibility assessments. Review results and assumptions before using them in regulatory submissions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cloud calculations transmit trial-design parameters, a hostname hash, locale, and skill version.

Mitigation: Disclose the outbound data before use, exclude patient or identifying data, and use --dry-run or CTSS_COZE_MOCK=1 when no network transmission is wanted.

Risk: Remote response content may be trusted too broadly in generated HTML reports.

Mitigation: Treat generated HTML, remote SVG, and external URLs as untrusted; inspect reports before opening or sharing them.

Risk: Incorrect assumptions or calculations could mislead clinical-trial planning.

Mitigation: Have a qualified statistician validate design inputs and outputs before protocol or regulatory use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/medstatstar/skills/ct-samplesize)
- [Project homepage (listed in skill metadata; import provenance unavailable)](https://github.com/medstatstar/ct-samplesize)
- [Calculation formulas](artifact/references/formulas.md)
- [Security model](artifact/references/security_model.md)
- [Operation guide](artifact/references/operation_sop.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Code, Figures]

**Output Format:** [Bilingual text or Markdown with sample-size and power estimates, optional SVG figures, and reproducible R code]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can include design assumptions, power curves, and optional justification text.]

## Skill Version(s):

5.8.0 (source: ClawHub release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
