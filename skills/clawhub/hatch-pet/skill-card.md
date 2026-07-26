## Description: <br>
Turns a keyword or reference image into a complete installable Codex v2 pet package with standard animation rows, look directions, QA artifacts, and packaging. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[harven-droid](https://clawhub.ai/user/harven-droid) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and Codex users use this skill to generate, repair, validate, package, and install custom Codex v2 pets from keywords or reference images. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow can create run folders and install generated files into the user's Codex pets directory. <br>
Mitigation: Review requested output paths and generated package contents before installation. <br>
Risk: Brand-based pet requests can raise trademark or logo-copying concerns. <br>
Mitigation: Use public brand cues only, avoid logos and readable marks, and review generated pets for trademark-sensitive elements. <br>
Risk: Optional brand discovery may use web research to collect visual and personality cues. <br>
Mitigation: Keep research narrow, prefer official sources, and avoid copying protected brand assets into the generated pet. <br>


## Reference(s): <br>
- [Codex Pet Generator release page](https://clawhub.ai/harven-droid/skills/hatch-pet) <br>
- [V2 Animation Rows](artifact/references/animation-rows.md) <br>
- [Codex V2 Pet Contract](artifact/references/codex-pet-contract.md) <br>
- [V2 Pet QA Rubric](artifact/references/qa-rubric.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, Files] <br>
**Output Format:** [Markdown guidance with shell command blocks and generated pet package files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create run folders, QA artifacts, pet.json, spritesheet.webp, and optional ZIP packages.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
