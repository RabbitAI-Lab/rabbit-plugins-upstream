## Description: <br>
Create, revise, and render layered paper-cutout or collage animations in Remotion using independent PNG layers, staged entrances, parallax, captions, narration, and audio effects. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tobewin](https://clawhub.ai/user/tobewin) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External creators, developers, and video teams use this skill to plan layered paper-collage scenes, prepare PNG assets, validate manifests, and render Remotion videos for explainers, brand stories, city narratives, and similar visual storytelling. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow runs local Python utilities and Remotion/npm video tooling on project media files. <br>
Mitigation: Review generated assets, manifests, and commands before rendering, and install Pillow and npm dependencies only in an environment approved for local video tooling. <br>
Risk: Layered video outputs can have clipped subjects, missing alpha channels, incorrect z-order, obstructed captions, or mistimed audio. <br>
Mitigation: Run the bundled project validator, inspect still frames and entrances, and verify final video streams before relying on the rendered output. <br>


## Reference(s): <br>
- [Paper Collage Remotion on ClawHub](https://clawhub.ai/tobewin/skills/paper-collage-remotion) <br>
- [Paper Collage Remotion Skill Repository](https://github.com/ToBeWin/paper-collage-remotion-skill.git) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands, JSON manifests, and TypeScript/Remotion code snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide creation or revision of Remotion starter files, script manifests, PNG layer assets, validation checks, and rendered video outputs.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
