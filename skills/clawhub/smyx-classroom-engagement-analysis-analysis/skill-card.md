## Description: <br>
Analyzes fixed classroom camera images or video to estimate class-level engagement, emotion distribution, low-engagement seat coordinates, heatmaps, alerts, teacher suggestions, and historical report links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Teachers, school operators, and education platform teams use this skill to analyze classroom video or images for aggregate engagement signals and anonymous seat-level prompts. It is intended for real-time teaching support and historical report review, not student identity recognition or individual performance ranking. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill processes sensitive classroom video involving students and may create historical behavioral records. <br>
Mitigation: Use only with school or organizational approval, required consent, defined retention rules, and a documented account model before processing classroom media. <br>
Risk: The artifact creates or reuses hidden account state and stores authentication tokens. <br>
Mitigation: Review the local data directory and token storage behavior before deployment, restrict filesystem access, and rotate or remove stored credentials when no longer needed. <br>
Risk: Engagement and emotion estimates can be misleading if used as individual student assessment or ranking. <br>
Mitigation: Treat results as aggregate teaching-support signals only, preserve the documented no-identity constraint, and require teacher review before acting on low-engagement prompts. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-classroom-engagement-analysis-analysis) <br>
- [Publisher profile](https://clawhub.ai/user/18072937735) <br>
- [API interface documentation](artifact/references/api_doc.md) <br>
- [SMYX analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, JSON, Files, Shell commands, Guidance] <br>
**Output Format:** [Markdown and JSON with structured classroom engagement results, anonymous seat coordinates, heatmap/report links, and optional saved output files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs can include engagement scores, emotion distributions, alert levels, teacher suggestions, historical report records, and export URLs.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata; artifact frontmatter says 1.0.7) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
