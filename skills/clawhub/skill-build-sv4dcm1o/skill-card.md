## Description:

This skill wraps headroom to compress prompts and context before LLM requests, with proxy, CLI wrapper, SDK, MCP, reporting, and optional statistics upload workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[guipi888](https://clawhub.ai/user/guipi888)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to reduce LLM token consumption and API cost for coding agents, RAG, long-document, and other high-context workflows. Users should validate compression quality on their own tasks before relying on aggressive compression settings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can optionally send token usage statistics to mrkjai.com and links those events to an API key.

Mitigation: Keep reporting disabled unless the user accepts the destination and account-linking implications, and store the API key only in an appropriate local secret location.

Risk: The release includes one-line remote shell installation guidance.

Mitigation: Inspect the provided scripts first and run local checked-out scripts instead of piping remote shell content directly into a shell.

Risk: Prompt compression may remove details that matter for high-stakes or precision-sensitive tasks.

Mitigation: Start with conservative compression settings and compare compressed and uncompressed outputs on representative user tasks before broader use.

Risk: Recoverable original context may be cached locally by the underlying compression workflow.

Mitigation: Protect local cache locations, avoid sensitive content unless storage is acceptable, and use non-persistent settings where available.

Risk: Security evidence flags promotional output and under-scoped telemetry as concerns.

Mitigation: Review generated guidance and scripts before deployment, and remove or disable behavior that is not required for the user's workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/guipi888/skills/skill-build-sv4dcm1o)
- [Headroom project](https://github.com/chopratejas/headroom)
- [headroom-ai package](https://pypi.org/project/headroom-ai/)
- [Headroom API reference](artifact/references/headroom_api.md)
- [OPC Headroom ingest API reference](artifact/references/api_reference.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, code snippets, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May generate local HTML reports and optional JSON telemetry events when reporting is enabled.]

## Skill Version(s):

1.8.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
