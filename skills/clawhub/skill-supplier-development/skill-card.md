## Description: <br>
Generates structured supplier improvement plans for SQE and supplier quality managers, covering diagnosis, corrective actions, tracking, and verification in Markdown and plain text. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[duding-engicool](https://clawhub.ai/user/duding-engicool) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
SQE teams and supplier quality managers use this skill to turn underperforming supplier issues into actionable improvement plans with owners, deadlines, KPIs, milestones, and validation gates. It is suited for corrective action, post-complaint supplier support, new supplier onboarding, and joint supplier capability improvement. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated plans may contain sensitive supplier performance details. <br>
Mitigation: Use an explicit approved output folder, apply normal access controls, and review or redact the documents before sharing. <br>
Risk: The example command references a helper script that is not bundled in the artifact. <br>
Mitigation: Confirm the script path and inspect available files before running any command. <br>
Risk: Improvement targets or KPI thresholds can be misleading if the user has not supplied real performance data. <br>
Mitigation: Require user-provided metrics and leave unknown targets clearly marked for enterprise completion. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/duding-engicool/skills/skill-supplier-development) <br>
- [Server-Resolved GitHub Source](https://github.com/duding-engicool/skill-supplier-development) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown and plain text supplier improvement plan documents, with inline shell command examples.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces dated supplier assistance plan files; real supplier performance data must be provided by the user and unknown targets should remain marked for enterprise completion.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
