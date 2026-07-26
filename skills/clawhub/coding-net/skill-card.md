## Description: <br>
Query and operate on Tencent Coding DevOps platform (e.coding.net) data, including iterations, issues, team members, requirements, and defects. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wangyin717](https://clawhub.ai/user/wangyin717) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and project teams use this skill to query Tencent Coding DevOps work items, inspect project iterations and team members, and create requirements or defects when explicitly requested. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a Tencent Coding bearer token that grants access to workspace data. <br>
Mitigation: Set CODING_TOKEN in the environment, avoid pasting tokens into chat, and use the least-privileged token available. <br>
Risk: The skill can create requirements or defects in the configured Coding project. <br>
Mitigation: Review the target project, issue type, assignee, iteration, dates, labels, and custom fields before allowing create_issue to run. <br>
Risk: Queries may return project, issue, and team member data from a private Coding workspace. <br>
Mitigation: Confirm the project identifier with the user and share returned data only in the intended workspace context. <br>


## Reference(s): <br>
- [Tencent Coding Open API endpoint](https://e.coding.net/open-api/) <br>
- [ClawHub skill page](https://clawhub.ai/wangyin717/skills/coding-net) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with Python and shell code blocks, plus structured API result summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Coding.net issue, iteration, and member identifiers returned by the API.] <br>

## Skill Version(s): <br>
1.0.6 (source: ClawHub release evidence; artifact frontmatter says 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
