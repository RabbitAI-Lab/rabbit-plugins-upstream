## Description:

Use when the agent needs persistent memory (L1/L2/L3), a living document archive (.vibo: pack documents, search by meaning, answer questions), web-search savings (compress articles up to 96%), thread memory (compress long conversations, restore details), live handoff (resume/save-state), or a privacy layer (mask secrets before they reach any LLM). Requires a valid ViBo license.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vnbochkarev-netizen](https://clawhub.ai/user/vnbochkarev-netizen)

### License/Terms of Use:

Proprietary

## Use Case:

Developers and agent operators use ViBo Memory to add consent-gated persistent memory, thread recall, document archive search, web-summary caching, live handoff, and optional secret-masking proxy behavior to AI agents that can run shell commands. The skill is intended for normal ClawHub commercial releases and requires activation with a valid ViBo license.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can persist local memory facts, document archives, conversation history, and web-summary cache data.

Mitigation: Enable modules only after explicit user consent, explain what each module stores, and use the documented forget, wipe, and file deletion paths when data should be removed.

Risk: The optional hosted proxy creates an external trust boundary for prompts, masked content, and metadata.

Mitigation: Use the self-hosted proxy for confidential work, enable hosted mode only with explicit trust in the provider, and keep a direct LLM provider route available.

Risk: Secrets or regulated data may be stored or copied into memory, archives, snapshots, web cache, or proxy data directories.

Mitigation: Use L3 secret storage or proxy masking for secrets, avoid storing secrets in live handoff snapshots, and keep generated memory, archive, cache, and proxy data files in user-controlled locations.

## Reference(s):

- [ViBo Memory ClawHub listing](https://clawhub.ai/vnbochkarev-netizen/skills/vibo-memory)
- [ViBo product site](https://wwwvibo.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs can include CLI commands for memory, archive, web compression, thread memory, live handoff, license checks, and optional proxy setup.]

## Skill Version(s):

2.1.2 (source: frontmatter, VERSION, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
