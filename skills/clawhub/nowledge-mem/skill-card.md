## Description:

Enables OpenClaw to use shared Nowledge Mem memory locally or remotely for persistent multi-tool AI context storage and retrieval.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wey-gu](https://clawhub.ai/user/wey-gu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OpenClaw users use this plugin to connect OpenClaw agents to Nowledge Mem for searchable conversation memory, structured memory capture, startup context, graph exploration, and local or remote memory workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: OpenClaw conversations can become persistent searchable memory.

Mitigation: Install only when persistent memory is intended, review sessionDigest before use, and set sessionDigest=false for manual-only memory.

Risk: Remote memory mode may send conversation memory to a configured server.

Mitigation: Review apiUrl and apiKey before use, keep local mode when remote sharing is not intended, and use only the minimum remote credentials required.

Risk: Sensitive or regulated sessions may need stricter capture boundaries.

Mitigation: Use captureExclude and #nmem-skip for sessions that should not be captured, and prefer minimal mode with sessionDigest=false for sensitive work.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wey-gu/skills/nowledge-mem)
- [Nowledge Mem](https://mem.nowledge.co)
- [OpenClaw](https://openclaw.ai)
- [Nowledge Mem remote access guide](https://mem.nowledge.co/docs/remote-access)
- [Nowledge Mem search and relevance](https://mem.nowledge.co/docs/search-relevance)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell command and JSON configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces agent-facing setup, verification, recall, save, search, and troubleshooting guidance for OpenClaw and Nowledge Mem.]

## Skill Version(s):

0.8.34 (source: server release evidence, package.json, CHANGELOG, released 2026-08-31)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
