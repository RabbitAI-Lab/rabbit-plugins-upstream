## Description: <br>
Make one transparent animated sticker package from one static reference image and one natural-language motion prompt. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wufei-png](https://clawhub.ai/user/wufei-png) <br>

### License/Terms of Use: <br>
Apache-2.0 <br>


## Use Case: <br>
External users and developers use this skill to turn a single static reference image and motion prompt into a transparent looping sticker package, including source frames, motion metadata, validation reports, and optional platform exports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Dependency hygiene issues can arise if the environment resolves an outdated Pillow release. <br>
Mitigation: Install in an isolated environment and ensure dependency resolution selects a current patched Pillow version. <br>
Risk: Sticker packages may contain user-derived image material, and optional reference inclusion can copy the original image into the package. <br>
Mitigation: Treat generated packages as user-content artifacts and use reference inclusion only when the original image is intentionally needed in the output. <br>


## Reference(s): <br>
- [Motion plan](references/motion-plan.md) <br>
- [Transparency branch](references/transparency.md) <br>
- [Validation](references/validation.md) <br>
- [Platform exports](references/platform-exports.md) <br>
- [Agent Skills specification](https://agentskills.io/specification) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Animated WebP sticker package with PNG source frames, JSON metadata, validation reports, and optional platform GIF or preview exports.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires one static reference image and one motion prompt; generated packages may contain user-derived image material.] <br>

## Skill Version(s): <br>
0.8.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
