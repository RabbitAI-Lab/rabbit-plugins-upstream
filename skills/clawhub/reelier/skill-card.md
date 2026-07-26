## Description: <br>
Replay recurring deterministic jobs at 0 tokens instead of re-reasoning them every run. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fixlyai](https://clawhub.ai/user/fixlyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use Reelier to record deterministic HTTP or MCP tool-call jobs once, replay them on scheduled heartbeats, and wake the LLM only when drift is detected. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Using scan or from-session can inspect local agent transcripts. <br>
Mitigation: Install only if comfortable running the reelier npm package and letting it inspect agent transcripts for replayable deterministic sequences. <br>
Risk: Replay of write steps can repeat changes when writes are explicitly enabled. <br>
Mitigation: Keep the default read-only behavior and pass --allow-writes only for jobs that are intentionally supposed to perform writes. <br>
Risk: Open-ended coding, file-editing, and non-deterministic sessions are outside the skill's replay boundary. <br>
Mitigation: Use Reelier only for deterministic HTTP or MCP tool-call workflows and treat empty scan results as expected when no replayable sequence exists. <br>


## Reference(s): <br>
- [Reelier ClawHub skill page](https://clawhub.ai/fixlyai/skills/reelier) <br>
- [Reelier homepage](https://github.com/seldonframe/reelier) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guidance focuses on deterministic replay jobs, drift checks, generated skills, and user-reviewed write permissions.] <br>

## Skill Version(s): <br>
1.0.0 (source: skill frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
