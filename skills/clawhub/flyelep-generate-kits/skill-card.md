## Description: <br>
A Flyelep API skill pack that helps agents generate e-commerce posters and perform image creation, background removal, enlargement, translation, scene replacement, product replacement, color changes, partial redrawing, and clarity enhancement. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[flyelepai](https://clawhub.ai/user/flyelepai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and commerce teams use this skill pack to call Flyelep's hosted image APIs for product imagery, poster generation, image cleanup, translation, and product editing workflows. The skill guides agents in collecting prompts, public image URLs, aspect ratios, task counts, model choices, and secretKey authentication before making HTTP POST requests. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends prompts, image URLs, and a Flyelep API key to Flyelep's hosted image APIs. <br>
Mitigation: Install only when using Flyelep's hosted APIs, keep secretKey out of repositories, logs, shared prompts, and saved skill files, and avoid submitting sensitive or private images unless that data sharing is acceptable. <br>
Risk: Generated or edited image outputs may be unsuitable for the user's intended commerce, branding, or translation use without review. <br>
Mitigation: Review returned image URLs and generated assets before publication or downstream use, especially for product claims, language, branding, and visual fidelity. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/flyelepai/skills/agent-skills-main) <br>
- [Flyelep Platform](https://www.flyelep.cn) <br>
- [Flyelep Controlboard](https://www.flyelep.cn/controlboard) <br>
- [Skill Pack Overview](artifact/skills.md) <br>
- [generate-poster](artifact/skills/generate-poster/SKILL.md) <br>
- [async-free-creation](artifact/skills/async-free-creation/SKILL.md) <br>
- [ai-image-matting](artifact/skills/ai-image-matting/SKILL.md) <br>
- [image-enlarge](artifact/skills/image-enlarge/SKILL.md) <br>
- [image-clarity-enhance](artifact/skills/image-clarity-enhance/SKILL.md) <br>
- [image-translate](artifact/skills/image-translate/SKILL.md) <br>
- [intelligent-extension](artifact/skills/intelligent-extension/SKILL.md) <br>
- [partial-redrawing](artifact/skills/partial-redrawing/SKILL.md) <br>
- [product-color-change](artifact/skills/product-color-change/SKILL.md) <br>
- [product-replace](artifact/skills/product-replace/SKILL.md) <br>
- [scene-replace](artifact/skills/scene-replace/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration instructions] <br>
**Output Format:** [Markdown guidance with JSON request bodies, curl examples, and generated image URLs returned from Flyelep APIs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a user-provided Flyelep secretKey and public image URLs for workflows that process input images.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
