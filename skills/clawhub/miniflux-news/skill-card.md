## Description: <br>
Fetch and triage unread RSS and news entries from a Miniflux instance via its REST API using a local API token. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hartlco](https://clawhub.ai/user/hartlco) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and Miniflux users use this skill to list unread entries, inspect full entry content, summarize selected items, and explicitly mark chosen entries or categories as read. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a Miniflux API token and can change account read state when mark-read commands are used. <br>
Mitigation: Use HTTPS, keep the token private, prefer the narrowest token Miniflux supports, and run mark-read commands only after checking the target entries or category. <br>


## Reference(s): <br>
- [Miniflux API notes](references/miniflux-api-notes.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and optional JSON from the bundled script] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can read from a local config file or MINIFLUX_URL and MINIFLUX_TOKEN environment variables; mark-read actions require explicit confirmation.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
