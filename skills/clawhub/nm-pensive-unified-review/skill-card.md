## Description: <br>
Orchestrates multi-domain review across code, architecture, tests, security, and related quality areas in a single pass. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill to coordinate comprehensive repository reviews, select relevant review domains, synthesize findings, and produce an integrated action plan before merges or releases. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may activate on broad review-related requests. <br>
Mitigation: Invoke it only for explicit comprehensive review work or use a narrower review skill when the desired review domain is already known. <br>
Risk: The skill may run a local backlog-capture write command without asking. <br>
Mitigation: Require user confirmation before executing write commands and review generated backlog entries before keeping them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-pensive-unified-review) <br>
- [Clawdis homepage](https://github.com/athola/claude-night-market/tree/master/plugins/pensive) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown review report with findings, evidence, recommendations, and action items] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include prioritized severity levels, evidence appendices, and suggested local commands.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
