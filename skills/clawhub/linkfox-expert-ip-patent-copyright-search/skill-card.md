## Description:

Accepts a product image or Amazon ASIN, checks intellectual-property risk across design patents, utility and invention patents, word marks, graphic marks, copyright, and policy compliance, then can enrich high-risk patent findings with legal status, claims, patent family, citation, and full-text details before producing a structured HTML report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and ecommerce operators use this skill to screen products before listing or review competing products for potential patent, trademark, copyright, and policy-compliance risk. The skill is designed to orchestrate specialized LinkFox detection services and deliver a structured risk report, not legal advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images, listing data, prompts, credentials, and session metadata may be sent to LinkFox-controlled services.

Mitigation: Use only with data approved for external processing, configure the intended LINKFOX_TOOL_GATEWAY host, and avoid confidential product imagery unless the service data handling is acceptable.

Risk: Local files may be uploaded as public URLs for detectors that require URL-accessible images.

Mitigation: Review upload behavior before use, avoid sensitive local files, and remove uploaded assets through the relevant service controls when no longer needed.

Risk: Remote onboarding and automatic feedback behavior can change what is installed or what task data is transmitted.

Mitigation: Review or disable remote onboarding and feedback flows before deployment, and require operator approval for new helper-skill installation.

Risk: Full results may be retained locally without tight controls.

Mitigation: Store outputs in approved locations, restrict access to generated reports and cached results, and clear local artifacts according to the deployment retention policy.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-expert-ip-patent-copyright-search)
- [Full IP Detection Workflow](artifact/skills/ip-full-detection/references/workflow.md)
- [Full IP Detection Output Schema](artifact/skills/ip-full-detection/references/output-schema.md)
- [Full IP Detection Data Fields](artifact/skills/ip-full-detection/references/data-fields.md)
- [LinkFox Skills Guide](https://skill.linkfox.com/linkfoxskills/guide.htm)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Code, Configuration, Guidance, Files]

**Output Format:** [Structured HTML report with supporting summaries, risk ratings, and optional patent-detail sections]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include only executed checks and may include patent legal-status, claim, family, citation, PDF, abstract, image, and description data when those follow-up lookups are performed.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
