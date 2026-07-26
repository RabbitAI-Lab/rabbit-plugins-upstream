## Description: <br>
Linear Native Node helps agents use Linear's GraphQL API from native Node.js to read workspace data and run explicitly approved issue, comment, status, priority, and project mutations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jwestburg](https://clawhub.ai/user/jwestburg) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to inspect Linear teams, projects, workflow states, assigned work, urgent issues, standup summaries, and individual issues, and to create or update Linear records after explicit approval. It is intended for workspaces where the operator is comfortable granting the agent the permissions attached to the configured LINEAR_API_KEY. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The configured LINEAR_API_KEY grants access according to the permissions of the Linear user or account that created it. <br>
Mitigation: Use the least-privileged key available, keep it session-scoped, and install only where those workspace permissions are acceptable. <br>
Risk: Read command output may include workspace-sensitive Linear issue, project, user, email, description, and URL data. <br>
Mitigation: Review and redact command output before sharing logs, examples, or summaries outside the intended workspace. <br>
Risk: Write commands can create or modify Linear issues, comments, workflow state, priority, and projects. <br>
Mitigation: Run write commands only with the prefix --execute flag after confirming the exact Linear target and intended mutation. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/jwestburg/skills/linear-native-node) <br>
- [Linear API Key Settings](https://linear.app/settings/api) <br>
- [Linear GraphQL API Endpoint](https://api.linear.app/graphql) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, shell commands, guidance] <br>
**Output Format:** [Plain text or JSON command output with shell command examples in Markdown documentation.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read commands may include workspace-sensitive Linear data; write commands require the prefix --execute flag and explicit approval.] <br>

## Skill Version(s): <br>
1.0.20 (source: server release metadata and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
