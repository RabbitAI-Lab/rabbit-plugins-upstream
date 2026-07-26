## Description: <br>
Audit agent system architecture across 12 layers for wrapper regression, memory pollution, tool discipline failures, and hidden fix loops. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paudyyin](https://clawhub.ai/user/paudyyin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to audit agent-system architecture, diagnose regressions, and produce severity-ranked findings with an ordered fix plan. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may guide an agent to inspect logs, memory files, and configuration that can contain sensitive local evidence. <br>
Mitigation: Use it only in workspaces where local evidence review is appropriate, avoid including secrets in generated reports, and review outputs before sharing. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [analysis, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown report with optional JSON schema for structured findings and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Findings are severity-ranked and include architecture diagnosis, evidence references, confidence, and an ordered fix plan.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
