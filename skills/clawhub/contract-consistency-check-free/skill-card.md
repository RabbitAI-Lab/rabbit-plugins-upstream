## Description:

Checks contract text locally for mechanically verifiable consistency issues, including party names, dates, amounts, placeholders, broken clause references, and defined-term hygiene, with findings tied to source evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External users, legal operations teams, procurement staff, and developers use this skill to run local consistency checks on Chinese or English contract text before final review. The skill reports evidence-backed contradictions and hygiene issues, but it does not provide legal advice or assess whether terms are fair.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The server security summary flags that documentation and normal output steer users toward an agent-driven paid install using an unpinned remote package.

Mitigation: Use the free checker only for local contract consistency review and prefer `--json` when output without promotional text is needed.

Risk: The bundled purchase prompt asks an agent to install and purchase a separate paid skill through SkillPay and an Alipay package source.

Mitigation: Do not paste that prompt into an agent unless you separately trust SkillPay, the Alipay package source, the paid skill, and the risk of running an unpinned remote installer under your user account.

Risk: A CLEAN verdict only means the free version did not find issues in its six implemented consistency checks.

Mitigation: Review the cited evidence manually and do not treat the output as legal advice, legal validity review, fairness review, or complete contract approval.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/contract-consistency-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)
- [SkillPay public shelf](https://skillpay.alipay.com/public/tokendidi)
- [Purchase instructions referenced by artifact](https://chenqg618.github.io/compliance-skills/buy.html)
- [Alipay agent-payment build guide referenced by artifact](https://skillpay.alipay.com/buildguide.md)

## Skill Output:

**Output Type(s):** [text, json, guidance]

**Output Format:** [Human-readable console text or structured JSON findings with levels, categories, line numbers, advice, evidence, executed checks, withheld checks, and summary verdict.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs on local contract text supplied as text, content, a plain text file, or JSON input; --json suppresses promotional console text and returns structured output.]

## Skill Version(s):

1.0.12 (source: artifact/SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
