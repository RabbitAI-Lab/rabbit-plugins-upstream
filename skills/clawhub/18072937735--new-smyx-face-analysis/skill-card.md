## Description: <br>
Supports uploading local MP4 videos or network video URLs to call a server-side API for facial diagnosis and return structured TCM facial diagnosis results. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agent operators use this skill to submit facial video files, images, or public video URLs for TCM-style health analysis, structured reports, health suggestions, report links, and report-history retrieval from a remote service. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive face and health media, or media from supplied URLs, may be sent to lifeemergence.com services for analysis. <br>
Mitigation: Use only with approved data handling, consent, and retention expectations; avoid private media, internal URLs, and broad automatic invocation. <br>
Risk: The skill can create or reuse identity and report-history state to retrieve prior reports. <br>
Mitigation: Review identity and report-history behavior before deployment, and inspect or clear workspace data when removing the skill. <br>
Risk: Health-style facial analysis can be misunderstood as medical diagnosis. <br>
Mitigation: Present results as informational reference only and require qualified professional review for medical decisions. <br>


## Reference(s): <br>
- [Skill page](https://clawhub.ai/18072937735/skills/new-smyx-face-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API reference](references/api_doc.md) <br>
- [smyx analysis API reference](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON] <br>
**Output Format:** [Markdown or JSON text with structured facial-analysis results, health suggestions, history tables, and report links.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can save results to an output file when requested.] <br>

## Skill Version(s): <br>
999.999.999 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
