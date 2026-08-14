## Description:

Use when the agent needs persistent memory (L1/L2/L3), web-search savings (compress articles up to 96%), or thread memory (compress long conversations, restore details). Requires a valid ViBo license.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vnbochkarev-netizen](https://clawhub.ai/user/vnbochkarev-netizen)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external AI-agent operators use this skill to add persistent memory, compressed web-search caching, and thread-memory summaries to Python-capable agents while tracking token savings. Before deployment, operators should decide what may be stored and how local memory, cache, secret, export, deletion, and retention controls will be handled.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create persistent local records of user facts, conversation history, web queries, compressed pages, and usage logs.

Mitigation: Define what categories may be stored before use, review where files are written, and verify delete, export, and retention controls in the runtime package.

Risk: The security summary warns that secrets may be stored with too little user control.

Mitigation: Avoid saving secrets unless explicitly intended, require user permission for secret storage, and verify that secret values are encrypted or withheld from model context before deployment.

Risk: Cached web searches and compressed pages may retain sensitive queries or source material.

Mitigation: Limit sensitive browsing through the skill, review cache contents and retention settings, and clear cached data according to the operator's data-handling policy.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/vnbochkarev-netizen/skills/vibo-memory)
- [Installation and integration guide](artifact/INSTALL.md)
- [Skill instructions](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline Python and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runtime behavior may persist local memory, cached web-search data, compressed conversation history, and usage logs.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
