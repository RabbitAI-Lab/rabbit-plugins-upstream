## Description: <br>
Tracks per-agent token usage and flags waste in parallel dispatch. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill after multi-agent runs to review per-agent token expenditure, identify duplicated work, and decide whether future dispatches should use fewer or more focused agents. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may lead users to inspect agent activity or file-access logs after parallel work. <br>
Mitigation: Use it only in environments where those logs are appropriate for review. <br>
Risk: The skill provides advisory judgments about token waste and duplicated work. <br>
Mitigation: Treat findings as review guidance and confirm them against the actual agent outputs before changing dispatch practices. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-conserve-agent-expenditure) <br>
- [Conserve plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/conserve) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Guidance, Markdown] <br>
**Output Format:** [Markdown guidance and review checklists] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [No code execution, credentials, MCP tools, or privileged access are included in the skill artifact.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release metadata; artifact frontmatter reports 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
