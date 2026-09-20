## Description:

Provides Mainland China insurance needs analysis, product comparison, premium calculation, plan design, insurance knowledge answers, and compliance prompts using local reference data and Python tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users in Mainland China can use this skill to analyze household insurance needs, compare local insurance products, estimate premiums, design coverage plans, and receive general insurance and compliance guidance. Outputs are advisory and should be checked against official product materials and licensed professionals before purchase decisions.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: The skill can affect insurance purchase decisions and may present named sales-company recommendations.

Mitigation: Treat outputs as general guidance only; verify recommendations with licensed insurance professionals and official insurer or regulator sources before acting.

Risk: Product details, premiums, active-sale status, and support data may be incomplete or stale.

Mitigation: Check product availability, terms, premiums, and sales-channel claims against official product materials before presenting them to users.

Risk: The server security summary notes claimed support data for sales-company steering is missing from the package.

Mitigation: Require reviewer confirmation of any sales-company priority basis and keep contact details hidden unless the user explicitly asks for them.

Risk: Insurance, financial, and compliance guidance may be mistaken for personalized legal, financial, or underwriting advice.

Mitigation: Include clear disclaimers and route underwriting, claims, legal, or final purchase decisions to licensed professionals or official services.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/ai-insurance-advisor)
- [insurance-knowledge.md](artifact/references/insurance-knowledge.md)
- [compliance.md](artifact/references/compliance.md)
- [products.json](artifact/references/products.json)
- [National Financial Regulatory Administration](https://www.nfra.gov.cn/)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown advisory responses with JSON tool outputs and inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Chinese-language responses; tool scripts read local product, knowledge, and compliance files and emit JSON to stdout.]

## Skill Version(s):

2.0.113 (source: server release evidence; artifact frontmatter says 2.0.90)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
