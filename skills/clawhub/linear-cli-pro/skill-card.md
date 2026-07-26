## Description: <br>
Guides developers and agent workflows in using the Linear CLI with stable JSON handling, dry-run previews, safe Markdown input, batch operations, and authentication recovery. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill to have an agent operate Linear through the CLI for issue creation, status changes, backlog cleanup, label synchronization, and source-adjacent intake from Slack, email, PRs, or git workflows. It emphasizes read-preview-write-verify loops before authenticated writes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide an agent through authenticated Linear writes that create, update, or transition issues. <br>
Mitigation: Review dry-run previews before writes, use the least-privileged Linear token available, and verify command receipts and error details after execution. <br>
Risk: Batch updates or hook-based automation can affect many Linear issues quickly or trigger rate limits. <br>
Mitigation: Keep concurrency low, start with dry-run or read-before-write checks, and add backoff when Linear returns rate-limit responses. <br>
Risk: Linear credentials may be exposed if tokens or credential files are copied into project files. <br>
Mitigation: Use interactive login or environment variables for automation, keep tokens out of repositories, and refresh or re-login when authentication fails. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/thcjp/skills/linear-cli-pro) <br>
- [Linear GraphQL API endpoint](https://api.linear.app/graphql) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration instructions] <br>
**Output Format:** [Markdown with bash command examples and JSON-oriented workflow guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs guide authenticated Linear CLI operations and prefer dry-run previews, machine-readable JSON, receipt checks, and file or stdin input for Markdown content.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
