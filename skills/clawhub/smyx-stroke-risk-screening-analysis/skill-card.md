## Description: <br>
Combines TCM facial feature recognition with physiological indicators to screen uploaded face images or videos for elevated stroke-risk signals and return lifestyle intervention suggestions, medical guidance, report links, or report history. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and health-management agents use this skill to screen face images or videos, optional blood pressure, blood sugar, and blood lipid values for stroke-risk indicators. The skill can also retrieve cloud-hosted screening report history for the resolved user identity. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive facial media, health indicators, media URLs, and report-history queries are sent to external lifeemergence.com/open.lifeemergence.com services. <br>
Mitigation: Install and use the skill only where users have consented to that data flow, avoid private or internal URLs, and limit submitted media and indicators to what is needed for screening. <br>
Risk: The output is health-risk screening guidance and may be mistaken for a medical diagnosis. <br>
Mitigation: Present results as screening information only and direct high-risk or symptomatic users to qualified medical professionals. <br>
Risk: The skill creates or reuses local identity and token records to associate analysis and report-history requests. <br>
Mitigation: Review local identity and token handling before deployment, isolate runtime state per user or workspace, and clear stored state when access should end. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-stroke-risk-screening-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API interface documentation](references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or JSON screening reports, Markdown report-history tables, and optional saved text output files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include structured health-risk fields, lifestyle suggestions, medical guidance, and cloud report links.] <br>

## Skill Version(s): <br>
1.0.7 (source: ClawHub release metadata; artifact frontmatter states 1.0.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
