## Description: <br>
Supplier due diligence assistant that helps procurement and project teams assess a company's qualifications, delivery capacity, bid history, partner relationships, public risk signals, and side-by-side supplier comparisons using tender and bidding data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Procurement teams, tender owners, general contractors, and business reviewers use this skill to investigate suppliers or subcontractors before selection or onboarding. It produces company background reports and two-supplier comparisons focused on verifiable bidding records, customer relationships, delivery history, and public risk disclosures. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Company search terms are sent to the Zhiliaobiaoxun vendor API. <br>
Mitigation: Install and use the skill only when sending supplier or company names to Zhiliaobiaoxun is acceptable for the due-diligence task. <br>
Risk: Auto-registration can store an API key in ~/.zlbx/config.json. <br>
Mitigation: Prefer a preconfigured ZLBX_API_KEY when credential persistence is not desired, and protect any local config file that contains an API key. <br>
Risk: Generated reports, signed sk links, recharge auto-login links, and returned phone numbers may expose sensitive account or business information. <br>
Mitigation: Treat generated reports and links as sensitive, share them only with authorized reviewers, and use contact lookup only for legitimate procurement or due-diligence needs. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/zhiliaobiaoxun/skills/supplier-qualification-checker) <br>
- [Tool Quick Reference](references/api-quick.md) <br>
- [Auto Registration Flow](references/auto-register.md) <br>
- [Report Template](references/report-template.md) <br>
- [Seven-Step Workflow](references/workflow.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Files, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown due-diligence reports with optional self-contained HTML report files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May require ZLBX_API_KEY, may store an API key in ~/.zlbx/config.json after user-approved auto-registration, and writes generated reports under ~/zlbx-company-intel-files/.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
