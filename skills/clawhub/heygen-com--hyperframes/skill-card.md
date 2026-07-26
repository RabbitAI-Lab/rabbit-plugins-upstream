## Description: <br>
HyperFrames routes video, animation, and motion-graphics requests into the right workflow, resumes existing projects, and manages project inspection, validation, preview, rendering, publishing, and batch rendering. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[heygen-com](https://clawhub.ai/user/heygen-com) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and content teams use this skill as the entry point for creating, editing, validating, rendering, and publishing HyperFrames video projects from briefs, URLs, GitHub PRs, Figma inputs, existing footage, or music. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may run npx-based HyperFrames commands and install or refresh related workflow skills. <br>
Mitigation: Review command summaries, keep projects under version control, and run HyperFrames validation after upgrades or workflow changes. <br>
Risk: Site capture, Figma or GitHub inputs, media generation, and publishing can use networked services when requested. <br>
Mitigation: Confirm external inputs and publishing intent before use, and avoid sending sensitive material to networked services unless approved. <br>
Risk: Project edits, renders, and publishing actions may create or update video project artifacts. <br>
Mitigation: Inspect diffs, previews, and validation results before treating generated output as final or public. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/hyperframes) <br>
- [Publisher profile](https://clawhub.ai/user/heygen-com) <br>
- [HyperFrames entry point](SKILL.md) <br>
- [Intent interview](references/intent-interview.md) <br>
- [Capability menu](references/capability-menu.md) <br>
- [Skill lifecycle](references/skill-lifecycle.md) <br>
- [Workflow route contracts](references/routes/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, code, configuration, and project artifact descriptions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include workflow routing decisions, project file changes, validation summaries, preview or render commands, and publishing guidance.] <br>

## Skill Version(s): <br>
1.0.19 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
