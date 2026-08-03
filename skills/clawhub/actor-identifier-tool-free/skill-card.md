## Description: <br>
仓库协作分析(免费版) helps personal developers analyze Git repository collaboration patterns with read-only local Git commands, producing repository-level aggregate reports on commit rhythm, churn, conventional-commit compliance, and file-level bus-factor risk. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to inspect authorized local Git repositories and summarize repository-level collaboration patterns. It is intended for workflow analysis and knowledge-transfer risk awareness, not individual performance scoring. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks an agent to run local read-only Git commands against a repository path. <br>
Mitigation: Use dry-run mode first, provide only an absolute path to an authorized repository, and review the proposed commands before execution. <br>
Risk: Repository history, commit messages, and file paths may contain sensitive project information even when summarized. <br>
Mitigation: Limit analysis to repositories the user is permitted to inspect and keep outputs at repository-level aggregation unless file-level risk disclosure is explicitly needed. <br>
Risk: The security summary notes inconsistent boilerplate around create, modify, delete, and network troubleshooting behavior. <br>
Mitigation: Treat the release as a local read-only Git analysis guide and ignore generic network or mutation language unless the publisher clarifies it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/actor-identifier-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown report with inline shell commands and structured summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs should stay at repository-level aggregation, with dry-run command review available before local execution.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
