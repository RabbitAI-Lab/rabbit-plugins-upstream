## Description:

Cue 搭子 helps business experts author, validate, test, tune, and pin reusable Cue research buddy templates for recurring public-data finance and business research workflows through natural conversation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wangxiaoxu](https://clawhub.ai/user/wangxiaoxu)

### License/Terms of Use:

MIT-0

## Use Case:

External Cue users and domain experts in finance, banking, asset management, compliance, and industry research use this skill to turn recurring public-data research scenarios into reusable Cue buddy templates. It guides template drafting, validation, creation, testing, tuning, and pinning through an agent conversation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes a self-update path and silent update check outside the core template-authoring workflow.

Mitigation: Treat +upgrade as an admin action; review the source and update target before running it, and monitor the documented update checker behavior.

Risk: The skill needs network access to Cue and access to the user's CUE_API_KEY.

Mitigation: Use only trusted Cue endpoints, protect CUE_API_KEY outside chat history, and avoid setting CUE_API_BASE unless it points to a trusted Cue service.

Risk: Private materials or unlisted upload helpers could create data exposure risk if used outside the documented workflow.

Mitigation: Keep user-provided materials local to the agent context and do not use unlisted upload helpers for private materials.

Risk: Testing and tuning can consume Cue credits and may involve long-running research streams.

Mitigation: Require explicit user confirmation before paid +test or +tune runs; use the documented replay fallback when long streams disconnect.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wangxiaoxu/skills/cue-buddy)
- [Cue platform](https://cuecue.cn)
- [Cue API key page](https://cuecue.cn/api-key)
- [Materials intake rules](references/materials-intake.md)
- [Template field specification](references/template-fields-spec.md)
- [Hard rules](references/hard-rules.md)
- [Gemini CLI cross-agent verification report](docs/verification-reports/2026-05-20-gemini-cli.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Conversational guidance plus Markdown template drafts, JSON payloads, shell commands, and local report files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call Cue APIs using the user's configured CUE_API_KEY; write operations and paid test or tune runs require user confirmation.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter metadata.version is 0.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
