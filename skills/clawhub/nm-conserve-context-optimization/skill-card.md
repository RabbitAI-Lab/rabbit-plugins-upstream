## Description: <br>
Optimizes context window via MECW principles and memory tiering. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to monitor context pressure, choose conservation strategies, route complex work to subagents or dedicated sessions, and keep long-running workflows within effective context limits. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Checkpoint, memory, or coordination files can retain secrets, credentials, proprietary snippets, or full transcripts if users store too much session detail. <br>
Mitigation: Store minimal summaries, avoid sensitive content in these files, and delete temporary files when the workflow is done. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-conserve-context-optimization) <br>
- [OpenClaw homepage](https://github.com/athola/claude-night-market/tree/master/plugins/conserve) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with inline code examples and command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only guidance that may propose checkpoint, memory, or coordination file patterns.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release metadata; artifact frontmatter lists 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
