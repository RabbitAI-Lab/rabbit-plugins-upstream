## Description:

Sample size and power calculation tool for clinical trial practitioners that uses a cloud R compute service for 49 clinical-trial test types and can return publication-grade SVG figures, bilingual results, and reproducible R code on request.

This skill is ready for commercial/non-commercial use.

## Publisher:

[medstatstar](https://clawhub.ai/user/medstatstar)

### License/Terms of Use:

MIT

## Use Case:

External clinical-trial practitioners, sponsors, CROs, clinicians, and learners use this skill to select an appropriate sample-size or power method, calculate required sample size or achievable power, and generate figures or R code for protocol and feasibility work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Clinical trial design parameters, locale, and a stable hostname hash may be sent to the author's Coze services.

Mitigation: Use --dry-run or CTSS_COZE_MOCK=1 for sensitive work, and avoid entering confidential protocol text unless the extracted parameters have been reviewed.

Risk: The security summary flags pre-approved endpoints without enforced runtime confirmation and recoverable shared tokens.

Mitigation: Review deployment suitability before installation and restrict use to environments where outbound calls to the publisher's services are acceptable.

Risk: Generated HTML and SVG reports are returned from a remote service and may be used in clinical or regulatory workflows.

Mitigation: Treat outputs as reference material, review reports before sharing, and validate calculations before regulatory submissions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/medstatstar/skills/ct-samplesize)
- [Project homepage](https://github.com/medstatstar/ct-samplesize)
- [English README](https://github.com/medstatstar/ct-samplesize/blob/main/README.md)
- [Chinese README](https://github.com/medstatstar/ct-samplesize/blob/main/README_zh-CN.md)
- [CLI examples](references/cli_examples.md)
- [Formula reference](references/formulas.md)
- [Extended functions](references/extended_functions.md)
- [Security model](references/security_model.md)
- [Adaptive-trial simulator](references/adaptive_simulator.md)

## Skill Output:

**Output Type(s):** [analysis, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with optional command examples, JSON request previews, SVG/HTML figure report references, and R code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write generated figures or aggregated HTML reports to CTSS_OUTPUT_DIR; dry-run and mock modes can preview requests without sending them.]

## Skill Version(s):

5.3.12 (source: frontmatter, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
