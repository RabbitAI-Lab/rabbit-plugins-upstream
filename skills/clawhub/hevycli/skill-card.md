## Description: <br>
Access and analyze Hevy fitness tracking data including workouts, routines, and exercise templates via the command line. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nsampre](https://clawhub.ai/user/nsampre) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and Hevy users use this skill to inspect workout history, routines, exercise templates, and progress data through hevycli commands. It helps produce read-only command-line workflows and JSON exports for personal fitness analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide users to export workout history, which may contain personal fitness data. <br>
Mitigation: Export Hevy data only to intended locations and review files before sharing or storing them. <br>
Risk: The workflow depends on installing and running the third-party hevycli command-line tool. <br>
Mitigation: Confirm that you trust the hevycli source used by the go install command before installation. <br>
Risk: Hevy API key configuration is required for CLI access. <br>
Mitigation: Keep API keys out of shared transcripts, logs, and exported files, and verify configuration with hevycli config show when troubleshooting. <br>


## Reference(s): <br>
- [ClawHub Hevy skill page](https://clawhub.ai/nsampre/skills/hevycli) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and optional JSON-oriented analysis] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands are read-only against Hevy data and may request table or JSON CLI output.] <br>

## Skill Version(s): <br>
0.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
