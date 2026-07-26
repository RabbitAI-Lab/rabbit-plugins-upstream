## Description: <br>
Oee Analysis helps users calculate OEE metrics from equipment operating data, diagnose six major loss categories, check data credibility, and produce improvement priorities with explicitly labeled ROI assumptions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[duding-engicool](https://clawhub.ai/user/duding-engicool) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Operations, manufacturing, and equipment engineering teams use this skill to review monthly or quarterly equipment efficiency, identify whether availability, performance, or quality losses dominate, and prepare OEE improvement reports. It is also useful when users need a credibility check on reported OEE values or an initial ROI estimate for an improvement project. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may process operational production metrics that are business-sensitive. <br>
Mitigation: Handle uploaded or pasted production data according to the organization's data handling and access-control requirements. <br>
Risk: Incorrect or incomplete inputs can lead to misleading OEE, loss distribution, or ROI estimates. <br>
Mitigation: Review source data, confirm missing enterprise parameters, and treat ROI and improvement ranges as assumption-based planning inputs rather than final decisions. <br>
Risk: The artifact references report and calculation scripts that were not included, so runtime behavior may depend on files outside the submitted artifact. <br>
Mitigation: Confirm the complete release package includes the referenced calculation and report-generation files before relying on automated execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/duding-engicool/skills/skill-oee-analysis) <br>
- [Server-resolved source repository](https://github.com/duding-engicool/skill-oee-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, HTML, Guidance] <br>
**Output Format:** [Markdown and HTML diagnostic reports with metric tables, warning lists, prioritized actions, and ROI estimates.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Flags missing enterprise parameters and labels assumptions used for ROI or improvement estimates.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata; artifact frontmatter reports 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
