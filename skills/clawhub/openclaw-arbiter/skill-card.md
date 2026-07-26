## Description: <br>
Audits installed agent skills and reports their use of network access, subprocess execution, file I/O, environment variables, unsafe serialization, and related permission patterns. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[atlaspa](https://clawhub.ai/user/atlaspa) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and workspace administrators use this skill to audit installed agent skills, generate permission reports, and review elevated permission use before trusting or deploying skills. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill includes commands that can disable, quarantine, or remove installed skills. <br>
Mitigation: Use audit, report, and status for read-only review; back up the skills workspace and use quarantine, protect, and revoke only after manual review. <br>
Risk: Permission findings are produced by local pattern-based analysis and can require human interpretation. <br>
Mitigation: Review line-level findings before taking enforcement actions, especially when a skill is flagged for elevated or critical permissions. <br>


## Reference(s): <br>
- [OpenClaw Arbiter on ClawHub](https://clawhub.ai/atlaspa/skills/openclaw-arbiter) <br>
- [OpenClaw](https://github.com/openclaw/openclaw) <br>
- [Claude Code documentation](https://docs.anthropic.com/en/docs/claude-code) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Terminal text and Markdown tables with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runs locally with Python 3 and no external dependencies; reports may include line-level findings and exit codes for clean, elevated, or critical permission results.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
