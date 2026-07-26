## Description: <br>
Identifies obesity, emaciation, external injuries, skin abnormalities, and abnormal mental states to help pet owners detect potential health issues promptly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Pet owners and care workflows use this skill to analyze pet images or videos for body-condition concerns, visible injuries, skin abnormalities, abnormal mental state, and historical report lookup. The output is health-reference guidance and should not replace professional veterinary diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pet images, videos, and report history are processed through the Life Emergence cloud service. <br>
Mitigation: Use only with media and report data appropriate for cloud processing, and inform users that outputs are health-reference guidance rather than veterinary diagnosis. <br>
Risk: The skill can silently create or reuse a cloud-linked identity and store authentication tokens locally. <br>
Mitigation: Review local workspace data and token storage before deployment, especially where credential handling, deletion controls, or shared workspaces are sensitive. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-pet-body-health-analysis) <br>
- [Publisher profile](https://clawhub.ai/user/18072937735) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API documentation](references/api_doc.md) <br>
- [Detailed API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and JSON-style structured health analysis reports, including report links for historical queries.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Accepts local image/video files or media URLs; documented media formats include jpg, png, jpeg, mp4, avi, and mov with a 10 MB limit.] <br>

## Skill Version(s): <br>
1.0.9 (source: ClawHub release evidence; artifact frontmatter reports 1.0.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
