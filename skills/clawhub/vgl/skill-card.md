## Description: <br>
Vgl helps agents convert natural-language image requests into structured VGL JSON for precise control over object placement, lighting, camera angle, lens focal length, composition, color scheme, style, and edit instructions for Bria FIBO models. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[galbria](https://clawhub.ai/user/galbria) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, designers, and agent builders use this skill to produce reproducible VGL structured prompts for image generation, editing, masked editing, captioning, and prompt refinement. The skill is useful when natural-language prompts need to be converted into explicit JSON fields before sending to a compatible image model. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated image prompts may contain inaccurate, sensitive, or unsuitable descriptions, especially when they describe people. <br>
Mitigation: Review VGL JSON before sending it to an image model and revise fields that affect identity, appearance, text rendering, or sensitive attributes. <br>
Risk: The skill references API usage that depends on a Bria API key. <br>
Mitigation: Keep API keys under user-controlled secret management and avoid embedding credentials in prompts, generated JSON, logs, or shared artifacts. <br>
Risk: Broad trigger wording may activate the skill for image-prompt tasks where structured VGL output is not desired. <br>
Mitigation: Confirm that the requested output should be VGL JSON before using the generated structure in a downstream image workflow. <br>


## Reference(s): <br>
- [VGL Output Schema Reference](artifact/references/schema-reference.md) <br>
- [ClawHub Vgl skill page](https://clawhub.ai/galbria/skills/vgl) <br>
- [Bria image generate endpoint](https://engine.prod.bria-api.com/v2/image/generate) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Guidance] <br>
**Output Format:** [Structured JSON object with supporting Markdown guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces a single VGL prompt object with required image-description, lighting, aesthetics, photographic, text-rendering, and edit-instruction fields.] <br>

## Skill Version(s): <br>
1.2.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
