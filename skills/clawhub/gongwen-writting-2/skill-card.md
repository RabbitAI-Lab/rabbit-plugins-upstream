## Description:

This skill helps Chinese office, state-owned enterprise, and government-affairs users draft and revise formal official documents with audience-specific style, online writing templates, GB/T 9704 formatting guidance, and missing-detail placeholders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yourtsao](https://clawhub.ai/user/yourtsao)

### License/Terms of Use:

MIT-0

## Use Case:

Office, secretarial, administrative, and government-affairs users use this skill to turn document requirements, meeting notes, policy context, or drafts into Chinese official-document prose. It supports common document classes such as requests, reports, summaries, meeting minutes, notices, letters, speeches, plans, research reports, briefings, and related formal materials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to register with an email and send document prompts to the publisher's online gateway.

Mitigation: Use it only for content appropriate to share with that publisher-operated service, and avoid sensitive or regulated material unless the organization has approved the data flow.

Risk: The skill uses a paid quota/payment flow and may store a local service token after registration.

Mitigation: Review account, quota, payment, and token-storage behavior before deployment, and avoid sharing the configured skill directory with others.

Risk: The skill includes instructions for broad cleanup of prior conversation history, caches, memory, clipboard contents, or local knowledge files.

Mitigation: Require explicit user or administrator confirmation before any cleanup action, or disable those cleanup instructions in managed deployments.

## Reference(s):

- [Word 版式导出指引（GB/T 9704-2012）](artifact/references/word-export.md)
- [ClawHub skill page](https://clawhub.ai/yourtsao/skills/gongwen-writting-2)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Chinese official-document drafts, Markdown guidance, optional Python snippets, and Word/export instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require online quota, email registration, and publisher gateway calls before document generation.]

## Skill Version(s):

1.0.58 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
