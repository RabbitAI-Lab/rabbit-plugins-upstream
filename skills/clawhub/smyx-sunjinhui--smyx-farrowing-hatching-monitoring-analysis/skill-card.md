## Description: <br>
Monitors farrowing and poultry hatching video for reproductive events such as water breaking, straining, piglet delivery, egg pipping, and chick emergence, then returns event reminders. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External farm and hatchery operators use this skill to monitor fixed-camera footage from farrowing pens or hatching areas, identify key reproductive milestones, and review current or historical event reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Monitoring footage and report retrieval may depend on external Smyx/LifeEmergence services. <br>
Mitigation: Review endpoint, retention, and access-control documentation before using sensitive farm or hatchery video. <br>
Risk: The security review reports under-disclosed cloud identity, credential-file, token storage, and account-provisioning behavior. <br>
Mitigation: Approve installation only after credential-handling, token storage, and opt-out behavior are documented and acceptable. <br>
Risk: Event recognition is for monitoring and may be wrong or incomplete. <br>
Mitigation: Treat reminders as decision support and follow local farm procedures and qualified veterinary or reproduction staff guidance. <br>


## Reference(s): <br>
- [Farrowing/Hatching Monitoring Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-farrowing-hatching-monitoring-analysis) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [API Interface Documentation](references/api_doc.md) <br>
- [Analysis API Documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or JSON analysis reports with event details, reminder levels, report links, and command examples.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save report output to a file when an output path is supplied.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata; skill frontmatter says 1.0.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
