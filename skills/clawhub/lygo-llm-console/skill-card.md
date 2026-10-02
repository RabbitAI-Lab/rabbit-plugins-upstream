## Description:

Helps operators verify and run a local GGUF-powered LLM console with a loopback agent portal and optional tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[deepseekoracle](https://clawhub.ai/user/deepseekoracle)

### License/Terms of Use:

MIT-0 (skill); LYGO Sovereign License v3.0 (bundled kit)

## Use Case:

Operators and developers use this skill to verify and set up a local LLM console, scan GGUF models, and chat through an agent portal without relying on hosted inference. The bundled runtime can optionally use local tools and fetch public web content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Untrusted web content can reach a tool-enabled agent able to execute local code as the user.

Mitigation: Avoid tool-enabled sessions with untrusted URLs; consider setting LYGO_HOST_PREFETCH=0 and run only as an unprivileged user.

Risk: The console can expose powerful local tools if made available beyond the operator's machine.

Mitigation: Keep the console bound to loopback and do not serve untrusted users.

Risk: Chats, notes, indexes, tasks, and scheduled jobs may remain on disk.

Mitigation: Review retained data and delete the kit folder when those records are no longer needed.

## Reference(s):

- [ClawHub release](https://clawhub.ai/deepseekoracle/skills/lygo-llm-console)
- [LYGO LLM Console homepage](https://chatagent.ca/lygo-llm-console.html)
- [Quickstart](examples/quickstart.md)
- [Security notes](references/SECURITY.md)
- [Bundled kit license](kit/LICENSE)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration guidance]

**Output Format:** [Conversational text and tool results, with commands or code when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local sessions, notes, indexes, tasks, and scheduled jobs can persist in the kit folder.]

## Skill Version(s):

1.6.0 (source: ClawHub release and skill frontmatter; bundled console 1.5.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
