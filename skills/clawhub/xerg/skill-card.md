## Description: <br>
Audit and reduce AI agent spend in dollars, or audit provider-generated FOCUS 1.4 billing data. Use for AI costs, agent spend, token waste, billing reconciliation, commitments, or FinOps. Works with OpenClaw, Hermes, Claude Code, Cursor, generic event ingest, and FOCUS CSV/Parquet. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xerg](https://clawhub.ai/user/xerg) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, engineering leads, and FinOps practitioners use Xerg to audit local AI-agent runtime spend, identify waste separately from savings opportunities, reconcile FOCUS billing data, and compare compatible fixes in dollar terms. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may inspect sensitive local AI usage logs, transcripts, billing exports, and optional remote sources. <br>
Mitigation: Run local audits only in workspaces where that data access is acceptable, and review the local sources reported by doctor before starting an audit. <br>
Risk: Cloud upload can disclose audit totals, rollups, findings, recommendations, comparison deltas, and source metadata. <br>
Mitigation: Keep audits local by default and run connect, push, activate, or push-latest flows only after explicit user approval. <br>
Risk: Credential exposure can occur if XERG_API_KEY or workspace keys are pasted into commands, logs, source files, URLs, or chat. <br>
Mitigation: Use browser activation or a CI secret manager, and do not place credentials directly in shell commands or conversations. <br>


## Reference(s): <br>
- [Xerg homepage](https://xerg.ai) <br>
- [Xerg documentation](https://xerg.ai/docs) <br>
- [Xerg skill source](https://xerg.ai/skill.md) <br>
- [@xerg/cli npm package](https://www.npmjs.com/package/@xerg/cli) <br>
- [Xerg service status](https://status.xerg.ai) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or plain text with inline shell commands and optional JSON audit summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Local audit results should be summarized in dollars, distinguish identified waste from savings opportunities, and avoid upload flows unless the user explicitly approves them.] <br>

## Skill Version(s): <br>
0.17.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
