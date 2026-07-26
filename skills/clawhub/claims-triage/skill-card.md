## Description: <br>
Triage an incoming insurance claim by checking the coverage trigger against policy wording, banding severity and complexity, screening for fraud indicators, setting a first-pass reserve range, and routing with an SLA. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mohitagw15856](https://clawhub.ai/user/mohitagw15856) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Claims handlers and insurance operations teams use this skill for first-pass triage of FNOLs and new claims. It produces analytical support for coverage trigger review, severity banding, fraud-indicator screening, first-pass reserving, and routing decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Claim files can contain sensitive personal, financial, medical, or policy information. <br>
Mitigation: Use the skill only in environments approved for claim data and follow the organisation's data-handling and retention controls. <br>
Risk: The skill provides triage support and could be mistaken for a final coverage, reserving, SIU, or counsel referral decision. <br>
Mitigation: Require human claims handlers to verify policy wording, regulatory requirements, reserve decisions, and referrals before acting. <br>


## Reference(s): <br>
- [Claims Triage ClawHub Page](https://clawhub.ai/mohitagw15856/skills/claims-triage) <br>
- [Claims Triage Homepage](https://mohitagw15856.github.io/pm-claude-skills/skill/claims-triage.html) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, guidance] <br>
**Output Format:** [Markdown structured triage note] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes coverage view, severity band, indicator screen, reserve range, routing recommendation, SLA, information gaps, and a support-not-determination disclaimer.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
