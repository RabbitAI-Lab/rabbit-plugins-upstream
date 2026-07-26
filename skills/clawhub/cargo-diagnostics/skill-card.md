## Description: <br>
Diagnose and explain Cargo workflow behavior after the fact: trace why a single run produced the wrong output, sweep a batch or play for errors and group them by root cause, and profile where a play's credits go and how to cut the cost. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cargo-ai](https://clawhub.ai/user/cargo-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to diagnose Cargo workflow runs, group batch failures, and analyze credit spend before deciding whether to fix, re-run, report, or optimize a play. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Cargo CLI diagnostics can inspect workspace workflow runs, errors, and credit usage. <br>
Mitigation: Install and run the skill only for Cargo workspaces where this inspection is intended. <br>
Risk: Billing commands may require an admin token and can expose account usage data. <br>
Mitigation: Use admin access only for the billing attribution steps that require it, and review those commands before execution. <br>
Risk: Re-running records or paid nodes can spend Cargo credits. <br>
Mitigation: Review re-run recommendations, pilot on a small record set, and confirm expected credit spend before broader execution. <br>


## Reference(s): <br>
- [Cargo Diagnostics on ClawHub](https://clawhub.ai/cargo-ai/skills/cargo-diagnostics) <br>
- [Cargo Skills Homepage](https://github.com/getcargohq/cargo-skills) <br>
- [Run Trace](references/run-trace.md) <br>
- [Batch Error Sweep](references/batch-error-sweep.md) <br>
- [Play Cost Profile](references/play-optimize-credits.md) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Guidance, Shell commands, Markdown] <br>
**Output Format:** [Markdown with inline shell commands and compact diagnostic tables] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Cargo CLI commands, SQL queries, root-cause summaries, cost estimates, and recommended next actions.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
