## Description: <br>
Identifies weed species and coverage density from field top-view images or video and returns structured heatmap data for precision weeding decisions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Farm operators, agronomy teams, and agent users can use this skill to analyze field imagery, estimate weed pressure, and produce structured weed distribution data for precision weeding workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Field images, videos, or media URLs are sent to the LifeEmergence service for analysis. <br>
Mitigation: Install and use the skill only when this transfer is acceptable for the field imagery involved; avoid sensitive farm imagery unless approved. <br>
Risk: The skill can create or reuse an internal account identity and persist account tokens locally. <br>
Mitigation: Review or remove the automatic identity and token persistence behavior before using the skill in a shared workspace or regulated environment. <br>
Risk: Weed detection and density results may be incomplete or inaccurate under poor image conditions or crop-specific edge cases. <br>
Mitigation: Use the output as field-management reference data and validate operational or herbicide decisions against agronomy procedures and qualified personnel. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/18072937735/skills/smyx-farmland-weed-identification-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API documentation](references/api_doc.md) <br>
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands] <br>
**Output Format:** [Markdown and structured JSON returned from an API-backed analysis workflow] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include weed species lists, density estimates, heatmap data, historical report records, and report links.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
