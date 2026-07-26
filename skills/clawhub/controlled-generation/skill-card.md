## Description: <br>
Controlled Generation helps agents generate images that preserve a source image's composition through structural maps while changing style, subject, material, or finish. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[runware](https://clawhub.ai/user/runware) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and image-generation agents use this skill to preserve pose, outline, depth, or scene layout from a source image while producing a new visual treatment. It is suited for controlled asset variations, interior redesign, sketch-to-render workflows, and composition-locked restyling. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: User-provided images and prompts may be sent to a Runware-backed generation workflow. <br>
Mitigation: Use only images and prompts allowed by provider terms and workspace policy; avoid sensitive private images unless approved. <br>
Risk: Image-generation workflows can incur normal API costs and may be subject to content-policy limits. <br>
Mitigation: Review provider pricing, quota, and content policy before using the skill in a production workflow. <br>
Risk: ControlNet guidance can overconstrain or underconstrain a generation if the map type or step settings are mismatched. <br>
Mitigation: Select the map type that matches the intent and adjust thresholds, weight, startStep, and endStep based on the output quality bar. <br>


## Reference(s): <br>
- [Controlled generation worked recipes](references/examples.md) <br>
- [ClawHub skill page](https://clawhub.ai/runware/skills/controlled-generation) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, code, configuration, shell commands] <br>
**Output Format:** [Markdown with JSON examples and workflow guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces schema-oriented image-generation workflow guidance; final image outputs come from the connected generation service.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
