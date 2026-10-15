## Description:

Helps manage personal to-dos from natural-language requests, with local task storage, duplicate checks, dependencies, and optional web and clipboard capture interfaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[awamwang](https://clawhub.ai/user/awamwang)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals and their assistants use this skill to capture, organize, review, and update personal tasks through conversation or a local interface.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local web interface may expose task data or permit unwanted changes while browsing untrusted sites.

Mitigation: Avoid running the web UI while browsing untrusted sites; require authentication and strict Origin checks, and remove wildcard CORS before trusting its API.

Risk: Clipboard capture can read passwords, private messages, or other sensitive copied text.

Mitigation: Disable clipboard capture whenever sensitive material may be copied.

Risk: Unexpected date or path handling may affect tasks written through the web interface.

Mitigation: Validate date and path handling before relying on web write operations.

## Reference(s):

- [Optimization roadmap](docs/OPTIMIZATION.md)
- [Agent prompt references](docs/agent-prompts.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, JSON]

**Output Format:** [Conversational task summaries and commands; JSON triage suggestions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uncertain triage decisions require confirmation before changing tasks.]

## Skill Version(s):

0.7.1 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
