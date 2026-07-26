## Description: <br>
Performs a two-phase audit combining a fast deterministic scan and a deep LLM quality review of security, cron jobs, config, and skills. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[merlinrabens](https://clawhub.ai/user/merlinrabens) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and OpenClaw operators use this skill to audit local OpenClaw installations for security, cron, configuration, and skill-quality issues before publishing, after major changes, or during periodic health checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Audit output may reveal local file paths and locations of suspected credentials. <br>
Mitigation: Keep generated JSON and reports local, and review them before sharing outside the trusted environment. <br>
Risk: The skill inspects local OpenClaw configuration, cron prompts, skills, and workspace files. <br>
Mitigation: Run it only when local inspection is intended and use its findings as review guidance rather than automatic remediation. <br>


## Reference(s): <br>
- [Remediation Guide](references/remediation.md) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown report with JSON output from the deterministic audit script] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Phase 1 emits local JSON scores and findings; Phase 2 emits a readable audit report with recommended actions.] <br>

## Skill Version(s): <br>
2.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
