## Description: <br>
Analyzes fixed-camera kindergarten or early-education video to identify child social-interaction events, summarize pairwise frequency and duration, and generate social-interaction reports and heatmaps. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Teachers, school staff, parents, and education-support developers use this skill to analyze classroom, playground, or early-education video for pairwise child interaction counts, durations, initiators, heatmaps, and low-interaction candidates. Outputs are educational support signals and should not be treated as medical, psychological, or autism-screening results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill processes sensitive video or URL inputs involving children through a remote analysis service. <br>
Mitigation: Use only with clear guardian and school consent, confirm that remote processing is permitted, and handle source media and report links according to the organization's child privacy requirements. <br>
Risk: Social-interaction statistics or low-interaction flags could be mistaken for clinical, psychological, or autism-screening conclusions. <br>
Mitigation: Present outputs as educational support signals only and direct users to qualified child-development or medical professionals for any developmental concerns. <br>
Risk: The evidence flags automatic identity/account handling, history access, and persistent tokens with limited user control. <br>
Mitigation: Review account binding, token storage, report retention, and history-access permissions before installing or operating the skill. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-child-social-interaction-analysis-analysis) <br>
- [Child social interaction API documentation](references/api_doc.md) <br>
- [SMYX analysis API error documentation](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Guidance] <br>
**Output Format:** [Markdown summaries with optional JSON detail and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include interaction statistics, initiator summaries, low-interaction candidate flags, heatmap URLs, exported report links, and historical report tables.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release metadata; artifact frontmatter reports 1.0.5) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
