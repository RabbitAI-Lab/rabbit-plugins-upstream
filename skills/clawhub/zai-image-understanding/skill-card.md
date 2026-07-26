## Description: <br>
图片理解技能，使用 Z.ai (智谱 AI) GLM-4V Vision API 进行图片分析。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[internettrollwatt](https://clawhub.ai/user/internettrollwatt) <br>

### License/Terms of Use: <br>
MIT License <br>


## Use Case: <br>
Developers and agents use this skill to analyze local images, image URLs, or base64 data URIs with the Z.ai GLM-4V Vision API and return image understanding results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected images, image URLs, and prompts are sent to Z.ai's cloud API for analysis. <br>
Mitigation: Use only images and prompts that are acceptable to share with Z.ai, and avoid confidential screenshots or private documents unless that data handling is approved. <br>
Risk: Analysis results may be saved as Markdown files and could retain sensitive image-derived content. <br>
Mitigation: Review saved output paths and generated Markdown before retaining, sharing, or committing them. <br>
Risk: The release uses external Python dependencies for HTTP requests, image processing, and environment loading. <br>
Mitigation: Install with reviewed or patched pinned dependencies when deploying in controlled environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/internettrollwatt/skills/zai-image-understanding) <br>
- [Z.ai Open Platform](https://open.bigmodel.cn/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [JSON responses by default, with optional Markdown files saved locally.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses a configurable prompt and model, reports token usage when available, and can save Markdown output under the user's local data directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
