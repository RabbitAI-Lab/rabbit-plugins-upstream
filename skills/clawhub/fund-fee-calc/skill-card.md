## Description:

Estimates asset-management, custody, and sales fees and illustrative net returns, and flags selected guaranteed-return claims.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (Python code only; documentation and theory all rights reserved)

## Use Case:

Agents assisting investors or financial reviewers can estimate total fees and illustrative net returns from principal, annual rates, and holding period, then screen marketing claims for selected guarantee language. Results are a preliminary aid, not investment or legal advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Illustrative returns or claim screening could be mistaken for investment or legal advice.

Mitigation: Label figures as estimates, and have a qualified professional review consequential financial or compliance decisions.

Risk: Documented installation steps and remote badge links access external networks.

Mitigation: Review external destinations and installation commands before running them; the included calculator itself runs locally.

Risk: Reusing documentation as though it were MIT-licensed may conflict with the package's layered terms.

Mitigation: Review the Chinese licensing notes and confirm permitted reuse separately for code and documentation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhaoxinghua09-cell/skills/fund-fee-calc)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Plain text or JSON calculator results; agent responses may be Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes fees, illustrative gross and net returns, a claim-screening result, and a financial disclaimer; CLI status 0/1/2 indicates pass/fail/usage error.]

## Skill Version(s):

1.0.2 (source: server-resolved ClawHub release; bundled SKILL.md and manifest.json list different versions)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
