## Description: <br>
Detects falls in target areas from video streams to support real-time home safety monitoring for elderly people living alone. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and safety-monitoring developers use this skill to analyze local videos or video URLs for fall events and to request structured reports or history for elderly home-safety monitoring. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends fall-detection videos, video URLs, identity values, and report history requests to configured LifeEmergence/Open API services. <br>
Mitigation: Use it only when those data transfers are acceptable, and prefer explicit user confirmation before uploads or history queries. <br>
Risk: The skill silently creates or reuses local identities and persists tokens or report-related records. <br>
Mitigation: Review the local data directory before deployment and clear generated records or tokens according to the user's retention policy. <br>
Risk: Fall-detection results are advisory and may be incorrect or incomplete. <br>
Mitigation: Require human confirmation and appropriate caregiver or medical follow-up before relying on alerts for safety decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-fall-detection-video-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [Fall detection API documentation](references/api_doc.md) <br>
- [Common analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown summaries and tables, JSON detail output, and optional saved text or JSON result files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include report links and history-list tables; supports basic, standard, and json detail levels.] <br>

## Skill Version(s): <br>
1.0.9 (source: server release evidence; artifact frontmatter lists 1.0.6) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
