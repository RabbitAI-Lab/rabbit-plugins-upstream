## Description: <br>
Local approval system for managing agent permissions. Use CLI to approve/deny requests, view history, and manage auto-approved categories. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shaiss](https://clawhub.ai/user/shaiss) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to manage local human-in-the-loop approval requests for agents, review decisions, and maintain auto-approved categories. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Persistent category-based auto-approval can let future agent requests skip human review too broadly. <br>
Mitigation: Use learned categories only for narrow, low-risk actions and regularly review category, pending, and history files. <br>
Risk: Agents governed by the approval process could approve or learn their own requests if command access is not controlled. <br>
Mitigation: Install only where approval commands are controlled by a trusted user or trusted wrapper, and do not allow governed agents to run approve or approve --learn. <br>
Risk: Mistakes or suspicious behavior can persist through learned approvals. <br>
Mitigation: Reset approvals after mistakes or suspicious behavior and keep approval history under regular review. <br>


## Reference(s): <br>
- [Local Approvals ClawHub listing](https://clawhub.ai/shaiss/skills/local-approvals) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance, Text] <br>
**Output Format:** [Markdown with inline shell commands and plain-text operational guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Maintains local JSON state for pending requests, approval history, and auto-approved categories.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
