## Description: <br>
Generates terminal recordings using VHS tape scripts and produces GIF outputs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and technical writers use this skill to create terminal demo recordings from VHS tape scripts for documentation, tutorials, and CLI workflow demonstrations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: VHS tape files can execute commands and record terminal output, which may expose secrets, private paths, hostnames, or sensitive command results. <br>
Mitigation: Review tape files before execution, redact sensitive output, and avoid recording commands that reveal credentials or private data. <br>
Risk: Publishing with VHS can upload recordings publicly. <br>
Mitigation: Use publishing options only when public disclosure is intended and the generated recording has been reviewed. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/athola/skills/nm-scry-vhs-recording) <br>
- [OpenClaw Homepage](https://github.com/athola/claude-night-market/tree/master/plugins/scry) <br>
- [VHS Execution Guide](modules/execution.md) <br>
- [VHS Tape Syntax Reference](modules/tape-syntax.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, Files] <br>
**Output Format:** [Markdown with inline bash and tape code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide creation of GIF, MP4, WebM, or screenshot files through VHS tape directives.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release evidence; artifact frontmatter lists 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
