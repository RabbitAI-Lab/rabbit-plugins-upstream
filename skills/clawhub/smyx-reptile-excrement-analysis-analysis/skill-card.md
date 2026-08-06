## Description: <br>
Analyzes reptile enclosure images or video frames to identify urate area, color, and texture plus feces morphology, then returns a structured visual assessment with recommended next actions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External reptile keepers, farm operators, and developers use this skill to process enclosure camera images, video frames, or URLs and receive a structured urate and feces assessment before cleaning. It can also query cloud-hosted historical reports for trend review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends reptile media, URLs, report queries, and derived identity values to LifeEmergence cloud services. <br>
Mitigation: Use it only with data approved for cloud processing, and review the LifeEmergence service relationship before installation. <br>
Risk: The skill can silently create or reuse a local account identity and store service tokens in workspace data. <br>
Mitigation: Review or clear data/smyx-api-key.txt and the local smyx common database when identity reuse is not desired. <br>
Risk: Visual excrement assessments can be mistaken for medical diagnosis if used without review. <br>
Mitigation: Treat outputs as visual screening guidance only and confirm abnormal findings with a qualified reptile veterinarian. <br>


## Reference(s): <br>
- [API interface documentation](references/api_doc.md) <br>
- [LifeEmergence skill demo](https://lifeemergence.com/sample.html) <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-reptile-excrement-analysis-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, files, guidance] <br>
**Output Format:** [Structured JSON or Markdown text, with optional saved result files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports can include urate metrics, feces morphology, alert level, recommended actions, report links, and a disclaimer.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release metadata; artifact frontmatter says 1.0.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
