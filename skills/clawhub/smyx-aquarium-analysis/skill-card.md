## Description: <br>
Analyzes aquatic pet images, videos, or video URLs through a publisher cloud API to identify visible health indicators, potential disease signs, care suggestions, and report links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External aquarium owners and developers use this skill to submit aquatic pet images, videos, or video URLs for cloud-assisted health analysis, receive structured health reports, and query previous account-linked reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Aquarium photos, videos, and account-linked metadata are sent to publisher cloud APIs for analysis. <br>
Mitigation: Use the skill only when cloud processing by the publisher is acceptable, and avoid submitting sensitive media. <br>
Risk: The artifact silently manages identity and stores tokens locally. <br>
Mitigation: Review identity handling and local token storage before deployment, restrict runtime storage access, and clear local data when it is no longer needed. <br>
Risk: History report behavior is account-scoped and the artifact contains inconsistent history-query command text. <br>
Mitigation: Verify history queries against the intended cloud account and document the correct command before operational use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-aquarium-analysis) <br>
- [Publisher profile](https://clawhub.ai/user/smyx-sunjinhui) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API interface documentation](references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, JSON, Shell commands, Files, Guidance] <br>
**Output Format:** [Markdown health report or JSON structured result, with optional saved output file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports may include health indicators, warnings, care suggestions, cloud report links, or account-scoped history listings.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release metadata; artifact frontmatter reports 1.0.10) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
