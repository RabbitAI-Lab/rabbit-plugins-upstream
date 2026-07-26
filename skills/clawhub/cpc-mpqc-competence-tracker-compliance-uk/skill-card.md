## Description: <br>
Plans CPC/MPQC competence tracking with reminders, evidence lists, and compliance reporting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kowl64](https://clawhub.ai/user/kowl64) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Fleet, depot, and compliance teams use this skill to maintain UK CPC/MPQC training matrices, expiry reminders, evidence lists, and periodic compliance reports. <br>

### Deployment Geography for Use: <br>
United Kingdom <br>

## Known Risks and Mitigations: <br>
Risk: CPC/MPQC competence, certificate, and compliance details may be shared with the agent during report generation. <br>
Mitigation: Confirm that sharing this information is acceptable before use, and keep certificate numbers, expiry dates, and evidence storage paths under user control. <br>
Risk: Generated reports may contain inaccurate or incomplete compliance details if source records are missing. <br>
Mitigation: Review generated matrices, reminders, and reports against source records, and leave unknown certificate numbers or dates clearly marked until verified. <br>
Risk: Customer or site-specific training requirements may differ from the standard tracker structure. <br>
Mitigation: Collect customer or site-specific requirements before finalizing the tracker, and use a dedicated section for those deltas. <br>


## Reference(s): <br>
- [Competence evidence standard](references/competence-evidence-standard.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown files with Excel-ready tables, reminder schedules, and compliance report sections] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated outputs mark unknown certificate numbers, dates, and site-specific requirements for user confirmation.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
