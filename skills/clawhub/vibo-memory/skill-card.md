## Description:

ViBo helps agents maintain local persistent memory, compress web-search results and long conversations, and build searchable local document archives.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vnbochkarev-netizen](https://clawhub.ai/user/vnbochkarev-netizen)

### License/Terms of Use:

ViBo End User License Agreement

## Use Case:

Developers and agent operators use this skill when an agent needs licensed local memory, thread history, web-result compression, or document archive search across sessions. It is intended for normal ClawHub use with deliberate configuration of local privacy-sensitive storage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill persists local long-term memory, conversation history, document archives, web cache data, and usage logs that may contain sensitive information.

Mitigation: Review and protect the configured storage locations for memory.web, thread.web, archive.vibo, web_cache.json, and vibo_usage.jsonl before use.

Risk: Secrets or highly sensitive data could be saved into memory in a way that exposes them to later agent context.

Mitigation: Avoid saving secrets except through the documented L3 permission flow, which is intended to keep secrets out of LLM context.

Risk: The skill requires license activation and license checks before use.

Mitigation: Activate with a valid ViBo license and run the documented license check before agent workflows depend on the skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/vnbochkarev-netizen/skills/vibo-memory)
- [Publisher profile](https://clawhub.ai/user/vnbochkarev-netizen)
- [ViBo product website](https://wwwvibo.com)
- [Installation and integration guide](artifact/INSTALL.md)
- [End User License Agreement](artifact/EULA.md)
- [Skill instructions](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash and Python code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct the agent to use local memory, cache, archive, history, and usage-log files after license activation.]

## Skill Version(s):

1.0.9 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
