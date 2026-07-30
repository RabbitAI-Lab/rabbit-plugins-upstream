## Description: <br>
Generates terminal recordings using VHS tape scripts and produces GIF outputs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and technical writers use this skill to create terminal demo recordings for documentation, tutorials, and CLI workflow walkthroughs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tape files can execute terminal commands and may hide setup actions during recording. <br>
Mitigation: Review tape files before running them and avoid hiding important or sensitive actions. <br>
Risk: Published recordings can expose commands, output, paths, or environment details. <br>
Mitigation: Sanitize terminal content and use public publishing only when the captured details are safe to disclose. <br>


## Reference(s): <br>
- [VHS Execution Guide](modules/execution.md) <br>
- [VHS Tape Syntax Reference](modules/tape-syntax.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/athola/skills/nm-scry-vhs-recording) <br>
- [Clawdis Homepage](https://github.com/athola/claude-night-market/tree/master/plugins/scry) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash and VHS tape code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides agents through validating tape files, checking VHS dependencies, running recordings, and verifying generated GIF outputs.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
