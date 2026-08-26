## Description:

Builds an inventory of AI capability an organization actually runs across purchases, in-house builds, vendor features, integrations, and free tools, then classifies ePHI contact, third-party disclosure, ownership, agreements, verification, and risk-analysis scope.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dangsllc](https://clawhub.ai/user/dangsllc)

### License/Terms of Use:

MIT-0

## Use Case:

Healthcare compliance, privacy, security, and operations teams use this skill to identify AI-enabled tools and workflows that may touch organizational work product or ePHI. It produces a defensible asset-identification inventory and findings for agreement coverage, ownership, verification, and risk-analysis scope, while leaving legal breach determinations and full risk analysis to qualified reviewers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Respondents could disclose passwords, tokens, patient data, email contents, or screenshots while answering inventory questions.

Mitigation: Frame the run to request only tool names, access categories, and high-level findings, and decline patient-level or credential material.

Risk: Own-account connected-app and browser-extension checks are samples and may be mistaken for tenant-wide audit evidence.

Mitigation: Label n=1 checks as sampling, report the tenant-wide count as unknown, and reserve tenant-wide OAuth, IdP, or MDM exports for an approved follow-up pass.

Risk: Findings about free tools or consumer signups may raise breach or notification questions beyond the skill's scope.

Mitigation: State that the skill performs asset identification, not breach determination or full risk analysis, and direct reportability questions to qualified legal or regulatory counsel.

## Reference(s):

- [AI Tooling Inventory Skill](https://clawhub.ai/dangsllc/skills/ai-tooling-inventory)
- [Publisher Profile](https://clawhub.ai/user/dangsllc)
- [Interview Question Bank](references/interview-questions.md)
- [Vendor AI Feature Inquiry Letter Template](references/vendor-letter.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown with structured JSON-style inventory and finding records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces one inventory array and one findings array; may also provide follow-up vendor questions and coverage caveats.]

## Skill Version(s):

2.0.0 (source: server release metadata; artifact frontmatter lists 2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
