## Description: <br>
Analyzes snake mouth images, videos, or URLs to identify visual stomatitis risk signals such as mucosa color changes, pus points, ulcers, necrotic tissue, and image-quality or context conditions that affect reliability. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, reptile keepers, breeding farms, and reptile veterinary teams use this skill to submit snake mouth media for visual analysis and receive structured stomatitis risk reports, non-treatment guidance, and report links. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Uploaded files or provided URLs are processed by LifeEmergence cloud APIs. <br>
Mitigation: Do not provide private URLs, sensitive enclosure footage, or proprietary media unless cloud processing is acceptable. <br>
Risk: The skill silently creates or reuses a persistent local identity and stores account tokens locally. <br>
Mitigation: Review or clear the workspace data used by the skill after use or before uninstalling it. <br>
Risk: Visual risk output could be mistaken for a veterinary diagnosis or treatment plan. <br>
Mitigation: Use the report as screening guidance only and route concerning results to a professional reptile veterinarian; do not add drug, dosage, or surgical instructions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-snake-stomatitis-detection-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API reference](references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, guidance] <br>
**Output Format:** [Markdown and JSON analysis reports with optional saved output files and report export links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include cloud report links and history-list results; accepts local image/video files or public media URLs.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release metadata; artifact frontmatter says 1.0.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
