## Description:

Loan Rate Disclosure Check helps agents pre-screen loan marketing copy for annualized-rate disclosure and rates above four times a reference base rate.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers, compliance reviewers, and agent operators use this skill to run a local preliminary check of loan-rate copy for annualized-rate disclosure and a configured four-times-base-rate threshold. It is a structured screening aid and does not replace legal, investment, or official compliance review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented global npx install path is unpinned.

Mitigation: Install only from a pinned, reviewed release or commit and avoid elevated privileges during installation.

Risk: The security summary reports false PASS behavior for invalid numeric input.

Mitigation: Treat outputs as preliminary screening, validate numeric inputs independently, and require human review before compliance decisions.

Risk: The skill addresses loan-rate compliance screening in a regulated domain.

Mitigation: Use official current requirements and qualified professional review for final legal, investment, or compliance determinations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/loan-rate-disclosure)
- [Publisher profile](https://clawhub.ai/user/zhaoxinghua09-cell)
- [Project homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [Plain text terminal output or JSON, with process exit codes rc=0, rc=1, or rc=2.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local offline Python script with no third-party runtime dependencies; results require human review for regulated decisions.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact SKILL.md frontmatter reports 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
