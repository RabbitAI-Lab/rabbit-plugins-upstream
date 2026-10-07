## Description:

Guides agents in querying Canvas LMS for courses, grades, assignments, messages, and files through authenticated shell commands without a running MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, parents, and other authorized Canvas users can use the skill to retrieve their own or a linked observee's learning information with direct Canvas API requests when the MCP server is unavailable or unnecessary.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An agent with shell access to Canvas tokens can expose credentials or sensitive education records.

Mitigation: Limit access to authorized users, keep tokens and client secrets out of shell history and logs, and unset credentials when finished.

Risk: The suggested unpinned npx command executes dynamically generated shell assignments.

Mitigation: Avoid the command unless the helper package has been verified and pinned; inspect its output before using it.

Risk: File download commands can fetch an unexpected URL or write to an unintended destination.

Mitigation: Validate the download URL and destination before running the command, and avoid overwriting existing files.

## Reference(s):

- [Canvas API endpoint examples](references/canvas-endpoints.md)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/canvas-parent-api)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Canvas API responses can contain sensitive education records; access requires a valid bearer token.]

## Skill Version(s):

2.1.8 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
