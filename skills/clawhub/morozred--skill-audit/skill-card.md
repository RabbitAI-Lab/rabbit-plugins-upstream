## Description: <br>
Audits locally installed agent skills for security and policy issues using the SkillLens CLI and produces risk-focused audit reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[morozred](https://clawhub.ai/user/morozred) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to scan local Codex or Claude skill directories, triage security and policy risks, and produce concise audit reports with evidence and recommended fixes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow relies on the external SkillLens CLI. <br>
Mitigation: Verify the SkillLens package before use and prefer a one-off or pinned invocation over a global install. <br>
Risk: Scanning broad roots or using optional auditor CLIs can expose more local skill content than intended. <br>
Mitigation: Scan specific skill folders where possible and use optional auditor CLIs only for content you are comfortable having those tools process. <br>
Risk: Audit results can miss issues when auditor CLIs are unavailable or return skipped statuses. <br>
Mitigation: Treat missing or skipped auditor results as manual review required rather than safe. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/morozred/skills/skill-audit) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with inline shell command snippets and audit report structure] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports are expected to include skill name, path, verdict, risk score, concrete evidence, and recommended fixes.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
