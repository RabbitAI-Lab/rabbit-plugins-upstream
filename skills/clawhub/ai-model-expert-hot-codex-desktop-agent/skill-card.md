## Description:

Helps agents plan and validate traceable desktop workflows that combine Codex local work with AI-HIVE model lookup, routing, execution records, and delivery folders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, product managers, operations teams, and independent founders use this skill to turn business goals involving code, files, web pages, and AI content production into auditable agent workflows. It emphasizes non-paid planning first, runtime model and price checks, explicit approval gates, and reproducible handoff records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses an AI-HIVE API key and runtime network model lookup.

Mitigation: Keep AI_HIVE_API_KEY in a secure environment variable or credential store, and confirm the user intends to use AI-HIVE before model queries.

Risk: Execution plans may lead to paid, batch, publishing, deletion, or account-affecting actions.

Mitigation: Review the generated plan and require explicit confirmation before those actions.

Risk: Desktop workflows can accidentally exceed the user's intended file, terminal, or account permissions.

Mitigation: Record an explicit permission scope and approval gate before accessing files, terminals, accounts, or external publishing channels.

## Reference(s):

- [AI-HIVE homepage](https://ai-hive.iclip.cn/chat)
- [OpenAI: ChatGPT Work and Codex](https://help.openai.com/zh-hans-cn/articles/20001275-chatgpt-work-and-codex)
- [AI-HIVE API base](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON execution plans and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local execution-plan JSON files and validation results; paid, batch, publishing, deletion, or account-affecting actions require review before execution.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
