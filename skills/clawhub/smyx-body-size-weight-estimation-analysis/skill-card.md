## Description: <br>
Estimates livestock body length and body weight from side-view videos or frames, tracking fattening progress in a contactless manner. | 通过视频视觉估测体长、体重，追踪育肥进度。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, farm operators, and livestock management teams use this skill to estimate livestock body measurements, body weight, and fattening stage from side-view images, videos, or media URLs. It can also retrieve cloud-hosted historical analysis reports associated with the current identity. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Livestock images, videos, URLs, and report history are sent to or retrieved from lifeemergence.com services. <br>
Mitigation: Use only media approved for third-party processing, and ask the publisher for data retention, deletion, and access-control details before sensitive farm or business use. <br>
Risk: The skill can silently create or reuse a remote account and store authentication tokens locally. <br>
Mitigation: Run it in an isolated workspace, protect or remove local identity and token stores after use, and confirm account creation and token storage controls with the publisher. <br>
Risk: Body-size and weight estimates can be affected by pose, occlusion, lighting, file quality, and reference-object accuracy. <br>
Mitigation: Use clear full side-view captures with a known reference object, and verify important production decisions with established weighing and farm management procedures. <br>


## Reference(s): <br>
- [ClawHub skill release page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-body-size-weight-estimation-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [Body size and weight estimation API documentation](references/api_doc.md) <br>
- [Common analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, files, guidance] <br>
**Output Format:** [Markdown or JSON text with analysis results, report links, and optional saved output files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Analysis uses a side-view livestock image, video, local path, or URL; history lookup returns cloud report records for the resolved identity.] <br>

## Skill Version(s): <br>
1.0.6 (source: ClawHub release metadata; SKILL.md frontmatter says 1.0.4) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
