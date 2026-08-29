## Description:

分析用户指定的普通方法、HTTP 接口方法或 RPC 方法，说明用途与流程、涉及的数据库表及引用它的服务。

This skill is ready for commercial/non-commercial use.

## Publisher:

[extraskittles](https://clawhub.ai/user/extraskittles)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to analyze a specified method, HTTP endpoint, or RPC method and understand its purpose, flow, database tables, and calling services. It supports a fast current-repository mode by default and broader cross-service analysis only when explicitly requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may run implicitly for code-analysis prompts and inspect repository code to answer the request.

Mitigation: Use explicit wording when invoking or avoiding the skill, and review what repository scope is appropriate before analysis.

Risk: Standard mode can broaden analysis to cross-service searches across the workspace.

Mitigation: Use quick mode for routine current-repository analysis and request standard mode only when cross-service evidence is needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/extraskittles/skills/analyze-code)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Concise Chinese Markdown report with code locations and evidence-backed conclusions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only analysis; quick mode is scoped to the current repository, while standard mode may inspect other service repositories when explicitly requested.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
