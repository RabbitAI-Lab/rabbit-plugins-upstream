## Description: <br>
Provides review-workflow scaffolding for context, evidence, and output so agents can produce consistent, comparable findings. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and reviewers use this skill at the start of detailed audits to establish context, inventory scope, capture evidence, and structure review deliverables. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Suggested shell commands can collect local repository context during a review. <br>
Mitigation: Run commands only in repositories intended for review and inspect proposed commands before execution. <br>
Risk: Review scaffolding can make findings look complete even when a domain-specific checklist has not been applied. <br>
Mitigation: Pair this workflow with the relevant domain review skill or checklist before finalizing conclusions. <br>


## Reference(s): <br>
- [review-core ClawHub listing](https://clawhub.ai/athola/skills/nm-imbue-review-core) <br>
- [claude-night-market imbue homepage](https://github.com/athola/claude-night-market/tree/master/plugins/imbue) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Text] <br>
**Output Format:** [Markdown guidance with checklist items and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [None] <br>

## Skill Version(s): <br>
1.9.17 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
