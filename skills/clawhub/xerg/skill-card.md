## Description: <br>
Audit and reduce AI agent runtime spend in dollars. Use for AI costs, agent spend, token waste, runtime attribution, detector coverage, and FinOps. Works with OpenClaw, Hermes, Claude Code, Cursor, and generic event ingest. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xerg](https://clawhub.ai/user/xerg) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, engineering leads, and FinOps teams use Xerg to run local-first audits of AI agent runtime spend, identify waste, report detector coverage, and compare compatible changes. The skill guides agents through installation checks, non-interactive audits, local summaries, and optional hosted sync only after explicit user action. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The third-party CLI reads AI agent logs, transcripts, local databases, Cursor exports, generic event payloads, or selected remote sources to calculate spend. <br>
Mitigation: Run local audits first, review outputs before pushing, and use hosted sync or API keys only when cloud features or CI automation are intentionally approved. <br>
Risk: Running through npx fetches and executes the published third-party npm package before the audit runs. <br>
Mitigation: Use the documented @xerg/cli package path according to local package and network policy, or install the CLI globally when repeated fetches are not desired. <br>
Risk: Runtime costs may be observed, locally estimated, or unpriced and are not authoritative provider invoices. <br>
Mitigation: Use Xerg output for runtime waste analysis and comparison, not for invoice reconciliation or provider billing authority. <br>
Risk: Credentialed cloud or CI usage can expose workspace access if keys are pasted into chat, commands, logs, or source files. <br>
Mitigation: Use browser pairing for normal activation and store XERG_API_KEY only in the CI provider's secret manager for non-interactive automation. <br>


## Reference(s): <br>
- [Xerg homepage](https://xerg.ai) <br>
- [Xerg documentation](https://xerg.ai/docs) <br>
- [Xerg skill source](https://xerg.ai/skill.md) <br>
- [Xerg service status](https://status.xerg.ai) <br>
- [@xerg/cli npm package](https://www.npmjs.com/package/@xerg/cli) <br>
- [ClawHub skill page](https://clawhub.ai/xerg/skills/xerg) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON audit summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Summaries should report dollar spend, identified waste, detector coverage, top findings, and per-agent spend when present.] <br>

## Skill Version(s): <br>
0.18.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
