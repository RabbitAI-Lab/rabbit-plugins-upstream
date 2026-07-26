## Description: <br>
Through fixed enclosure cameras or supplied image and video inputs, this skill analyzes a snake's open-mouth imagery for visual signs associated with stomatitis risk, including mucosa color, pus points, ulcers, necrotic tissue, image quality, and contextual exclusion signals. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, reptile keepers, breeders, reptile veterinary teams, and developers can use this skill to analyze snake mouth images or videos, produce structured visual risk reports, and query cloud-hosted historical reports. It is intended to support observation and escalation to a qualified reptile veterinarian, not to diagnose disease or prescribe treatment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Snake mouth images, videos, URLs, and account-linked report queries are sent to a remote Life Emergence/SMYX cloud service. <br>
Mitigation: Use the skill only with media and URLs approved for remote processing, and confirm the service's retention, deletion, and access controls before deployment. <br>
Risk: The skill can silently create or reuse local identity records and tokens. <br>
Mitigation: Avoid shared workspaces or existing smyx-api-key.txt/user databases unless identity reuse is intended; isolate deployments by workspace and review stored credentials before installation. <br>
Risk: Visual health analysis may be mistaken for veterinary diagnosis or treatment advice. <br>
Mitigation: Present outputs as visual risk observations only, avoid drug or procedure recommendations, and direct urgent or repeated findings to a qualified reptile veterinarian. <br>
Risk: Poor image quality or missing context can produce unreliable findings. <br>
Mitigation: Require clear, well-lit open-mouth imagery, species and husbandry context, and return an unreliable-signal result when the mouth is obscured, under-resolution, reflective, or captured during feeding. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-snake-stomatitis-detection-analysis) <br>
- [API Documentation](references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, guidance] <br>
**Output Format:** [Structured analysis report, Markdown history table, JSON detail mode, and optional output file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports include visual findings, risk level, recommended non-prescriptive actions, disclaimers, and report links when available.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
