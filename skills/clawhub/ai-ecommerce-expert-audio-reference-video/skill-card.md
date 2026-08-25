## Description:

AI电商专家｜音频参考生成视频 helps ecommerce content teams use IMIVA MCP to create product videos whose rhythm, mood, and audio direction are guided by reference audio.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, brand content teams, video editors, and advertising teams use this skill to prepare, budget-check, submit, and track IMIVA audio-reference product video generation tasks. It is intended for commercial product-media workflows where users provide or confirm product facts, media assets, channel requirements, and budget limits before paid task creation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper can call arbitrary IMIVA MCP tools available to the token.

Mitigation: Review the current MCP tool list before use and limit execution to the documented video-generation and task-query workflow.

Risk: The helper runs an unpinned npm package with access to the local process environment.

Mitigation: Run it from a clean shell with only MCP_TOKEN and API_URL set, and avoid exposing unrelated secrets in the environment.

Risk: Formal video generation can consume paid credits.

Mitigation: Use dry-run budget checks first, require explicit user confirmation, set maxCredits, and use a unique idempotencyKey for each order.

Risk: Generated ecommerce media can misrepresent product facts or reuse unauthorized third-party creative elements.

Mitigation: Use only user-provided or confirmed product facts and assets, verify output against channel requirements, and avoid copying protected marks, likenesses, packaging, or exclusive creative expression.

## Reference(s):

- [IMIVA homepage](https://imiva.ecpro.com/)
- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-ecommerce-expert-audio-reference-video)
- [MCP configuration example](artifact/references/mcp-config.example.json)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls]

**Output Format:** [Markdown guidance with JSON arguments and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses dry-run budget checks, user confirmation, idempotency keys, task IDs, and task-query steps for IMIVA video generation.]

## Skill Version(s):

1.0.0 (source: server release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
