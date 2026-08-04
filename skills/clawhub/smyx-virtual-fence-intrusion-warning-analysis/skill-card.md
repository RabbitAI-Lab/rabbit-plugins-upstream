## Description: <br>
Customizes safety zones, identifies babies crawling out or approaching dangerous areas such as bedsides or windowsills, and returns immediate virtual-fence crossing alerts for infant home safety. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Parents, caregivers, and agent operators use this skill to analyze home monitoring video or image inputs for baby safety-zone exits, proximity to dangerous areas, and historical alert reports. It is intended as an auxiliary safety alert and does not replace physical safeguards or active human supervision. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive baby or home monitoring media and report history may be processed through LifeEmergence cloud endpoints. <br>
Mitigation: Run the skill only with explicit user consent for cloud processing, avoid unnecessary sensitive inputs, and confirm retention and deletion expectations before deployment. <br>
Risk: The skill can create or reuse local identity records and tokens in the workspace with limited user-facing controls. <br>
Mitigation: Restrict workspace file access, periodically review and clear stored identity or token data, and prefer releases that expose user-managed identity and report controls. <br>
Risk: Virtual-fence alerts are auxiliary and may miss hazards or produce incorrect alerts. <br>
Mitigation: Use the output as a supplemental safety signal only, maintain physical safeguards, and keep active human supervision for infant safety. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-virtual-fence-intrusion-warning-analysis) <br>
- [Publisher profile](https://clawhub.ai/user/18072937735) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [Virtual fence API documentation](references/api_doc.md) <br>
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON] <br>
**Output Format:** [Markdown text with structured JSON report content and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports local video files or public video URLs, history-list queries, and optional file output; artifact evidence lists mp4, avi, and mov inputs up to 10 MB.] <br>

## Skill Version(s): <br>
1.0.9 (source: server release evidence; artifact SKILL.md reports 1.0.10) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
