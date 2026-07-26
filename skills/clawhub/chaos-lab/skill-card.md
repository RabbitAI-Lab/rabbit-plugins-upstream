## Description: <br>
Chaos Lab is a multi-agent framework for exploring AI alignment through Gemini agents with conflicting optimization targets. <br>

This skill is for research and development only. <br>

## Publisher: <br>
[jbbottoms](https://clawhub.ai/user/jbbottoms) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, educators, and AI safety researchers use Chaos Lab to run Gemini-based multi-agent experiments that surface conflicting optimization goals, security over-alerting, and preservation tradeoffs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sandbox file contents are sent to Google's Gemini API. <br>
Mitigation: Use only dummy data or deliberately selected files in /tmp/chaos-sandbox, and keep secrets and private projects outside the sandbox. <br>
Risk: The Gemini API key can be exposed or misused if handled loosely. <br>
Mitigation: Store the key with restrictive permissions, limit access to the key, and rotate it if exposure is suspected. <br>
Risk: The optional tool-access path could allow file writes or deletions if implemented without controls. <br>
Mitigation: Keep tool access disabled unless sandbox path checks, approvals, action logs, rollback, and a kill switch are in place. <br>


## Reference(s): <br>
- [Chaos Lab on ClawHub](https://clawhub.ai/jbbottoms/skills/chaos-lab) <br>
- [Tool Access Guidance](docs/tool-access.md) <br>
- [Flash Experiment Results](examples/flash-results.md) <br>
- [Pro Experiment Results](examples/pro-results.md) <br>
- [Trio Experiment Results](examples/trio-results.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown logs, terminal output, Python scripts, and setup commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Experiments write Markdown transcripts under /tmp/chaos-sandbox and call the Gemini API with a configured API key.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
