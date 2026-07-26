## Description: <br>
Browse, read, and manage Miniflux feed articles through a CLI with flexible output formats for headlines, summaries, full content, and JSON. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shekohex](https://clawhub.ai/user/shekohex) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to browse, search, read, and manage RSS/Atom articles in a Miniflux account. It supports feed and category browsing, article pagination, read/unread state changes, refresh actions, and machine-readable output for agent workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can store a Miniflux API key locally and uses that key to access account content. <br>
Mitigation: Prefer environment variables for credentials, protect any local config file that stores the key, and install only when account access is acceptable. <br>
Risk: Commands such as mark-read, mark-unread, and refresh can change state on the connected Miniflux server. <br>
Mitigation: Review commands before execution and treat state-changing commands as account actions rather than read-only queries. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/shekohex/skills/miniflux) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Guidance] <br>
**Output Format:** [Plain text, Markdown-style command guidance, or JSON from the Miniflux CLI] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports brief, summary, full-content, plain, JSON, pagination, filtering, search, and article status operations.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
