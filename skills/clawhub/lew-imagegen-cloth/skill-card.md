## Description: <br>
Generates ecommerce clothing imagery for apparel and model-based products, including white-background, model, lifestyle, selling-point, A+ content, and size-chart images from user-provided clothing references. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lienong1122334](https://clawhub.ai/user/lienong1122334) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and ecommerce operators use this skill to turn clothing or model reference images into single product images or coordinated image sets for apparel listings. It guides an agent through image URL validation, prompt construction, optional text generation, image generation, and result delivery. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill runs local Python helper scripts and coordinates downstream Linkfox skills. <br>
Mitigation: Install and run it only in an environment where the local artifact and sibling Linkfox skills are reviewed and trusted. <br>
Risk: Session files can contain product imagery metadata, prompts, generated outputs, and task state. <br>
Mitigation: Use a controlled workspace and review generated data files before sharing or reusing them outside the session. <br>
Risk: Edited prompts or state files could influence script paths or downstream execution. <br>
Mitigation: Do not allow untrusted users to modify prompt, parameter, or state files before dispatch; review state files when resuming or rerunning work. <br>
Risk: The authentication recovery path may install a remote onboarding skill. <br>
Mitigation: Require explicit approval and review before downloading or installing the remote onboarding artifact. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/lienong1122334/skills/lew-imagegen-cloth) <br>
- [Skill instructions](artifact/SKILL.md) <br>
- [Runtime workflow index](artifact/references/runtime/00-index.md) <br>
- [Delivery guidance](artifact/references/runtime/03-deliver.md) <br>
- [White-background image type](artifact/references/types/white-bg.md) <br>
- [Model image type](artifact/references/types/model-image.md) <br>
- [Lifestyle scene image type](artifact/references/types/scene.md) <br>
- [Selling-point image type](artifact/references/types/selling-point.md) <br>
- [A+ image type](artifact/references/types/aplus.md) <br>
- [Size-chart image type](artifact/references/types/size.md) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, shell commands, configuration, files, guidance] <br>
**Output Format:** [Markdown with inline image references, JSON parameter or state files, and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write session files containing image URLs, prompts, task state, task results, manifests, and generated image paths.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and artifact/_meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
