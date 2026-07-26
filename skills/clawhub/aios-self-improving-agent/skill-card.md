## Description: <br>
Aios Self Improving Agent helps an AIOS/OpenClaw agent record sanitized errors, corrections, knowledge gaps, feature requests, and reusable practices in the current agent workspace. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kadbbz](https://clawhub.ai/user/kadbbz) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Use this skill when an agent should preserve local learning notes about command failures, user corrections, recurring issues, outdated assumptions, or reusable practices while keeping records limited to the current agent workspace and current senderId-accessible files. <br>

### Deployment Geography for Use: <br>
User-controlled local agent workspace; no geographic restriction is specified in the release evidence. <br>

## Known Risks and Mitigations: <br>
Risk: Review before execution as proposals could introduce incorrect or misleading guidance into skills. <br>
Mitigation: Review and scan skill before deployment. <br>

## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kadbbz/skills/aios-self-improving-agent) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, shell commands, guidance] <br>
**Output Format:** [Markdown learning, error, and feature-request entries written under .learnings/, plus optional shell commands for local initialization, search, and deduplication.] <br>
**Output Parameters:** [Current workspace path, sanitized summaries, priority, status, area, related relative paths, tags, recurrence metadata, and optional QMD search terms.] <br>
**Other Properties Related to Output:** [Security evidence reports a clean verdict and says the skill is designed to persist sanitized local summaries. Review .learnings/ periodically in sensitive projects, avoid secrets and full logs, and keep records scoped to the current agent workspace and current senderId-accessible files.] <br>

## Skill Version(s): <br>
1.0.1 <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
