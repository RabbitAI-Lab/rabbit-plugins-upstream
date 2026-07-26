## Description: <br>
Analyzes litter-box area video or video URLs to track cat entry and exit events, summarize usage frequency and visit duration, compare behavior with historical baselines, and return behavior-based urinary health alerts without providing a medical diagnosis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, pet-care teams, catteries, veterinary inpatient wards, and boarding centers use this skill to turn litter-box camera footage into per-cat usage frequency, visit duration, historical comparison, and behavior-alert reports. Results are behavior-statistics alerts and are not a substitute for veterinary diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Litter-box footage or video URLs may be processed by the vendor cloud service. <br>
Mitigation: Use only media appropriate for vendor processing, avoid footage containing people or sensitive household details, and review the vendor's retention and access practices before installation. <br>
Risk: Reports are associated with a persistent internal user identity. <br>
Mitigation: Use an appropriate workspace or account boundary for the intended user group, and avoid sharing workspace data where report association could expose private household or pet-health information. <br>
Risk: Local workspace data may contain service tokens or identity material used by the vendor service. <br>
Mitigation: Restrict access to the workspace, avoid committing local data stores, and remove local credential or token data before sharing or archiving the environment. <br>
Risk: Behavior-based alerts can be mistaken for veterinary diagnosis. <br>
Mitigation: Present outputs as monitoring signals only and direct users to consult a veterinarian for medical assessment or treatment decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-litter-box-usage-monitor-analysis) <br>
- [Publisher profile](https://clawhub.ai/user/smyx-sunjinhui) <br>
- [API interface documentation](artifact/references/api_doc.md) <br>
- [Common analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with structured JSON-like analysis content, cloud report links, and optional saved output files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports local video files or video URLs, historical report listing, configurable detail level, and optional output-file writing.] <br>

## Skill Version(s): <br>
1.0.4 (source: ClawHub release metadata; artifact frontmatter and release changelog mention 1.0.5) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
