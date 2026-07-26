## Description: <br>
Smart Auto-Updater checks OpenClaw and ClawHub skill updates, analyzes changelogs and diffs with an LLM, and either auto-updates low-risk changes or produces risk reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiwang20010702](https://clawhub.ai/user/ruiwang20010702) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to keep OpenClaw and installed ClawHub skills current while applying configurable risk thresholds, dry-run checks, and reporting before changes are applied. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Automatic update decisions can change OpenClaw or installed skills without enough human review. <br>
Mitigation: Start in dry-run or report-only mode, keep scheduled auto-apply disabled in production, and enable automatic updates only with a rollback plan and approval policy. <br>
Risk: LLM-based risk classification can miss breaking, compatibility, performance, or security-sensitive changes. <br>
Mitigation: Use conservative thresholds, manually review medium and high risk reports, and test updates in a staging environment before production use. <br>
Risk: Update reports and webhook deliveries may expose operational details to the wrong destination. <br>
Mitigation: Review configured webhook destinations, report contents, and delivery channels before enabling notifications. <br>


## Reference(s): <br>
- [Risk Assessment Methodology](references/risk-assessment.md) <br>
- [Report Templates](references/report-templates.md) <br>
- [Integration Guide](references/integration.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports with inline shell commands and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Risk-classified update decisions with configurable report detail levels.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
