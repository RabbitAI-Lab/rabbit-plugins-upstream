## Description:

Compares multiple contracts signed from the same template by aligning clauses, identifying missing or extra clauses, summarizing per-clause text differences, and producing a clause comparison table with source text evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Legal, procurement, audit, and internal review users can compare several contracts based on the same template to find clause omissions and clause text changes. The skill supports local review workflows but does not provide legal advice or judge which version is more favorable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The artifact includes agent-actionable paid upgrade instructions that use an unpinned `npx ... @latest` installer and initiate a SkillPay purchase flow.

Mitigation: Do not allow an agent to run the upgrade installer or start a purchase until the package, source, payment terms, and installed contents have been independently reviewed and the human user explicitly confirms payment.

Risk: The skill compares contract text but does not provide legal advice, validate legal enforceability, or determine which clause is more favorable.

Mitigation: Use the output as a clause-difference aid and require qualified legal or business review before acting on contract conclusions.

Risk: The free version excludes key-field comparison, date logic, placeholder detection, and amount consistency checks.

Mitigation: Treat a clean result as limited to the listed free checks and use separate review for excluded contract risks.

Risk: Contract text can contain confidential or regulated information.

Mitigation: Run the local workflow only in an approved environment and avoid pasting sensitive contract text into unapproved external services.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/contract-comparison-free)
- [ClawHub publisher profile](https://clawhub.ai/user/chenqg618)
- [SkillPay marketplace referenced by artifact](https://skillpay.alipay.com/public/tokendidi)
- [SkillPay install and purchase guide referenced by artifact](https://skillpay.alipay.com/buildguide.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Console text by default, or structured JSON when the --json option is used.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Node.js standard-library code; reports insufficient input instead of fabricating a comparison conclusion.]

## Skill Version(s):

1.0.4 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
