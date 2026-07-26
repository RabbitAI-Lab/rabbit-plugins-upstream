## Description: <br>
Analyzes pet drying box videos through a cloud API to detect heat-stress signals such as panting intensity, tongue color, and movement frequency, then returns risk levels and intervention guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to analyze pet drying box video files or URLs for early heat-stress warning signals and to receive structured safety-oriented recommendations. It is intended for pet drying boxes, grooming stores, and pet hospitals, and does not provide veterinary diagnosis or treatment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends pet videos, video URLs, and related analysis requests to the LifeEmergence cloud service. <br>
Mitigation: Use only when the user accepts cloud processing of the submitted media and avoid submitting sensitive video unless the service is trusted for that data. <br>
Risk: The skill may create or reuse a local identity and store authentication tokens in the workspace data directory. <br>
Mitigation: Avoid shared workspaces for sensitive use, review local data storage expectations before installation, and clear workspace credentials when rotating users or environments. <br>
Risk: The skill can retrieve historical cloud reports associated with the local identity. <br>
Mitigation: Confirm that historical report access through the local identity is appropriate for the workspace and user before enabling report-list workflows. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-pet-drying-box-heat-stress-analysis) <br>
- [Publisher profile](https://clawhub.ai/user/18072937735) <br>
- [API documentation](references/api_doc.md) <br>
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, guidance] <br>
**Output Format:** [Markdown or JSON analysis reports with risk levels, observed signals, recommendations, and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write a report to a user-specified output file and may return historical report lists from the cloud service.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata; artifact frontmatter reports 1.0.6) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
