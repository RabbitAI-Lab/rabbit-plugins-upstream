## Description: <br>
Real-time database integration with InstantDB for admin operations such as querying, creating, updating, deleting, linking entities, and subscribing to real-time data changes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ubyjerome](https://clawhub.ai/user/ubyjerome) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to administer InstantDB applications, run entity and relationship operations, execute transactions, and monitor real-time updates for workflows visible to humans. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can change or delete live InstantDB data when used with an admin token. <br>
Mitigation: Use a non-production or least-privilege token where possible, require explicit confirmation before writes or deletes, and verify backups before destructive workflows. <br>
Risk: The InstantDB admin token could be exposed through logs, shell history, or copied command output. <br>
Mitigation: Keep the admin token out of logs and shell history, and provide it through controlled environment management. <br>
Risk: The release evidence recommends updating or pinning the ws dependency to a patched version. <br>
Mitigation: Pin or update ws before deployment and keep dependency updates under normal security maintenance. <br>


## Reference(s): <br>
- [InstantDB documentation](https://www.instantdb.com/docs) <br>
- [InstantDB Admin SDK](https://www.instantdb.com/docs/admin) <br>
- [InstantDB Query Syntax Reference](references/query_syntax.md) <br>
- [InstantDB Transaction Patterns](references/transactions.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with JavaScript examples, shell commands, configuration notes, and JSON-oriented CLI usage.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an InstantDB app ID and admin token; CLI operations may emit JSON results or subscription update events.] <br>

## Skill Version(s): <br>
1.0.0 (source: package.json and server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
