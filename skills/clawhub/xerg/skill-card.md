## Description: <br>
Audit and reduce AI agent spend in dollars or audit provider-generated FOCUS 1.4 billing data for AI costs, token waste, billing reconciliation, commitments, and FinOps across OpenClaw, Hermes, Claude Code, Cursor, generic event ingest, and FOCUS CSV/Parquet. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xerg](https://clawhub.ai/user/xerg) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, engineering teams, and FinOps practitioners use Xerg to run local AI-spend and FOCUS billing audits, identify confirmed waste and savings opportunities, and summarize dollar-level findings for remediation or comparison. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The CLI reads local agent logs, transcripts, state databases, and billing exports to calculate spend. <br>
Mitigation: Run audits only on intended data sources and review the paths reported by doctor before proceeding. <br>
Risk: Audit data can leave the local machine if hosted sync, push, remote, Railway, or cloud-connection steps are approved. <br>
Mitigation: Keep audits local by default and require explicit user approval before activation, push, remote access, or cloud setup. <br>
Risk: Persistent setup can write local credentials or configuration for later use. <br>
Mitigation: Approve persistent installation or hosted activation only after reviewing the destination, workspace, and credential handling. <br>


## Reference(s): <br>
- [Xerg homepage](https://xerg.ai) <br>
- [Xerg documentation](https://xerg.ai/docs) <br>
- [Xerg skill source](https://xerg.ai/skill.md) <br>
- [Xerg service status](https://status.xerg.ai) <br>
- [@xerg/cli npm package](https://www.npmjs.com/package/@xerg/cli) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON audit summaries from the CLI] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Local audit outputs may include dollar totals, confirmed waste, findings, recommendations, and comparison deltas; hosted sync is optional and user-approved.] <br>

## Skill Version(s): <br>
0.15.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
