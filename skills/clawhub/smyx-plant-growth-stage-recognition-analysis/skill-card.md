## Description: <br>
Accurately identifies key growth stages of plants from germination to fruiting based on computer vision and deep learning, provides structured data for precision agriculture decision support. | 植物生长阶段识别技能，基于计算机视觉与深度学习算法，精准识别植物从发芽到结果的全生命周期关键生长阶段，为精准农业提供科学决策支持 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, agricultural producers, and developers use this skill to analyze plant images or videos, identify plant growth stages, and produce structured decision-support reports for precision agriculture. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Media and internal identifiers are sent to the Life Emergence cloud service for analysis. <br>
Mitigation: Use the skill only with plant images or videos approved for upload, and review organizational data-sharing requirements before installation. <br>
Risk: The skill may create or reuse an internal identity, store or reuse local tokens, and retrieve prior reports tied to that identity. <br>
Mitigation: Review identity and token handling before deployment, and limit use to environments where report history access is acceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-plant-growth-stage-recognition-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and JSON-style structured analysis text, with optional saved file output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can query cloud history and return Markdown tables; analysis uses uploaded media files or URLs.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release metadata; artifact frontmatter lists 1.0.9) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
