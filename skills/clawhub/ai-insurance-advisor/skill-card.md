## Description:

AI Insurance Advisor helps users in mainland China with insurance needs analysis, plan design, product comparison, premium estimates, compliance prompts, claims guidance, sales copy, and agent training scripts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users and insurance agents use this skill to discuss mainland China insurance planning, compare products, estimate premiums, identify coverage gaps, and generate Chinese-language advisory or sales-support content. Its recommendations are advisory and should be checked against current insurer terms and licensed professional guidance before purchase.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: Insurance products, premiums, availability, and policy terms may be stale because the skill uses a static product database.

Mitigation: Verify product availability, premiums, policy terms, and regulatory details with official insurer sources or licensed professionals before making purchase decisions.

Risk: The skill provides advisory insurance planning and may suggest a fixed sales-company contact when asked for contact information.

Mitigation: Treat recommendations and contact suggestions as informational, compare multiple licensed channels, and avoid relying on the skill as the final purchase authority.

Risk: Generated compliance and claims guidance may not cover every user-specific legal or regulatory requirement.

Mitigation: Use the compliance output as a prompt for review and confirm legal, underwriting, claims, and disclosure questions with qualified professionals.

## Reference(s):

- [ClawHub skill release page](https://clawhub.ai/mnetfairy/skills/ai-insurance-advisor)
- [insurance-knowledge.md](references/insurance-knowledge.md)
- [compliance.md](references/compliance.md)
- [products.json](references/products.json)
- [validation_report_20260524_090219.md](references/validation_report_20260524_090219.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Chinese-language Markdown responses, JSON script outputs, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local helper scripts read JSON from stdin and write JSON to stdout; user-facing advisory responses should include product freshness and professional verification reminders.]

## Skill Version(s):

1.8.448 (source: server release evidence; artifact frontmatter reports 1.8.351)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
