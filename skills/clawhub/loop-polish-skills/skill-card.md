## Description: <br>
Loop Polish automates full-stack project polishing by starting services, verifying APIs, frontend behavior, and database state, scoring results, applying bounded fixes, retesting, and generating a report. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lqclf](https://clawhub.ai/user/lqclf) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill for explicit pre-release QA or delivery acceptance workflows that verify a runnable project, fix bounded issues, and produce a quality report. It is not intended for routine quick reviews or production environment validation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill actively runs, tests, and modifies development or staging projects. <br>
Mitigation: Review configuration before use, start with preflight or conservative mode, and avoid production systems or valuable live data. <br>
Risk: Full mode can terminate processes on common development ports. <br>
Mitigation: Only terminate processes confirmed as project-owned; ask the user before killing unrelated processes. <br>
Risk: Database verification may read credentials from project configuration files. <br>
Mitigation: Ask before reading database credentials, set db_verify to false when credential access is unnecessary, and never write credentials or connection strings to reports. <br>
Risk: Diagnostic collection can encounter sensitive headers, cookies, request bodies, responses, passwords, tokens, or secrets. <br>
Mitigation: Redact sensitive fields before saving diagnostics, reports, or state files, and exclude raw request and response bodies from reports. <br>
Risk: Auto-fixes may introduce incorrect code changes when findings are ambiguous or high risk. <br>
Mitigation: Use isolated Git branches, limit fix scope by strategy, request confirmation for schema, auth, or large-deletion changes, and roll back failed fixes from saved originals. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/lqclf/skills/loop-polish-skills) <br>
- [Skill Instructions](artifact/SKILL.md) <br>
- [README](artifact/README.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports, status text, code diffs, shell command guidance, and optional JSON configuration] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create polish reports, temporary state, and source-code edits in full mode; preflight mode is read-only.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
