## Description: <br>
Create professional terminal recordings with VHS tape files - guides through syntax, timing, settings, and best practices. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[killerapp](https://clawhub.ai/user/killerapp) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and documentation authors use this skill to draft VHS tape files, terminal recording command sequences, timing guidance, and output settings for CLI demos, README animations, documentation videos, and screenshots. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Example tapes include destructive or overly broad shell commands, including directory deletion and stopping all running Docker containers. <br>
Mitigation: Review generated .tape files before running them, use a disposable workspace, and replace broad cleanup commands with narrowly scoped demo resources. <br>
Risk: Users may copy production-like deletion examples into real environments. <br>
Mitigation: Treat VHS tapes like scripts and remove or constrain destructive commands before execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/killerapp/skills/vhs-recorder) <br>
- [VHS Tape File Syntax Reference](artifact/references/vhs-syntax.md) <br>
- [VHS Timing Control Reference](artifact/references/timing-control.md) <br>
- [VHS Settings Reference](artifact/references/settings.md) <br>
- [VHS Recording Examples](artifact/references/examples.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown with VHS tape snippets and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces authoring guidance and examples for VHS tape files; users must run generated tapes with local VHS, ttyd, and ffmpeg tooling.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
