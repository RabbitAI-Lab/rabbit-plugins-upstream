## Description: <br>
Packages an existing talking-head, interview, or podcast video with timed graphic overlay cards synced to the transcript while leaving the underlying clip intact. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[heygen-com](https://clawhub.ai/user/heygen-com) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and content teams use this skill to turn an existing talking-head clip into a polished recut with titles, lower-thirds, quote cards, data callouts, side panels, or picture-in-picture overlays. It is suited for agent-assisted video packaging workflows that can run local media tools and review generated files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review says the skill instructs agents to run a silent skill-package update before use, which can change trusted code without clear user approval. <br>
Mitigation: Run updates only explicitly, review the installed skill content before execution, and avoid automatic update steps in controlled workflows. <br>
Risk: The workflow runs local media tooling and npx hyperframes, then writes generated files under videos/<project>/. <br>
Mitigation: Run it in a workspace where generated media files are acceptable, review commands before execution, and inspect generated HTML and MP4 outputs before relying on them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/talking-head-recut) <br>
- [Design reference index](artifact/references/DESIGN_INDEX.md) <br>
- [Attribution notice](artifact/NOTICE.md) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, JSON planning artifacts, and HTML/CSS card fragments] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces media workflow instructions and generated project files under videos/<project>/, including metadata, transcript, storyboard, card HTML, composition HTML, and output MP4.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
