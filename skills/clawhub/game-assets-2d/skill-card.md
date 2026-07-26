## Description: <br>
Generate 2D game art that stays visually consistent across a whole set: sprites, die-cut stickers, item icons, parallax pieces, and asset sheets. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[runware](https://clawhub.ai/user/runware) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and game artists use this skill to guide an agent through producing cohesive 2D game asset packs, including sprites, icons, stickers, parallax layers, and transparent PNG cutouts. It is useful when a project needs multiple assets to share one style while preserving silhouettes or structures from references. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and reference images may be sent to external image-generation services through the referenced Runware tools. <br>
Mitigation: Avoid using private, confidential, or sensitive artwork unless that provider workflow is acceptable. <br>
Risk: Generated assets may vary in style, silhouette, or cutout quality across a set. <br>
Mitigation: Keep the chosen base model and style LoRA consistent, use Canny guidance when preserving structure, remove backgrounds last, and review outputs before use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/runware/skills/game-assets-2d) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with tool and parameter recommendations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide generation of transparent PNG game assets through external image-generation services.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
