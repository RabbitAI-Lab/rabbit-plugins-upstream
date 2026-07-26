## Description: <br>
Stellar Trails provides an always-on six-phase workflow framework for agent tasks, with traceability IDs, entry and exit gates, scope commitment, and enforcement checks that scale by task complexity. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hoshiyomix](https://clawhub.ai/user/hoshiyomix) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to impose structured planning, implementation, verification, and delivery discipline across coding, document, data, visualization, and multi-step analysis tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may start a local HTTP server as part of its workflow setup. <br>
Mitigation: Review server binding behavior before installation and disable the local server setup in sensitive or restricted workspaces. <br>
Risk: The skill may change files under `.zscripts` and `/home/user_skills` and persist task history to local worklogs. <br>
Mitigation: Install only in workspaces where those paths are expected to be modified, and review file changes after activation. <br>
Risk: The skill may use a GitHub PAT for git or CI workflows. <br>
Mitigation: Use a scoped token, avoid exposing credentials in shared workspaces, and remove credential setup if it is not required. <br>
Risk: The skill includes auto-update behavior. <br>
Mitigation: Review or remove auto-update steps when deterministic execution or change control is required. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/hoshiyomix/skills/stellar-trails) <br>
- [AskUserQuestion Gate Template](artifact/references/askuserquestion-gate.md) <br>
- [SADC Subagent Delegation Template](artifact/references/sadc-subagent-delegation.md) <br>
- [Workflow Phases](artifact/procedure/phases.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown instructions with workflow checklists, inline shell commands, and task reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May direct the agent to run setup commands, manage local workflow files, and produce structured phase reports.] <br>

## Skill Version(s): <br>
9.9.1 (source: server release metadata and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
