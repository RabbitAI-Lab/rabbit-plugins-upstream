## Description:

Helps agents draft Chinese government and enterprise official documents across 38 document types using guided templates, server-provided writing frameworks, and GB/T 9704 formatting guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yourtsao](https://clawhub.ai/user/yourtsao)

### License/Terms of Use:

MIT-0

## Use Case:

Office staff, administrative teams, and agents use this skill to draft, revise structure, and format official Chinese administrative documents such as requests, reports, notices, meeting minutes, speeches, summaries, and plans. The skill gathers missing inputs, retrieves document-specific templates and writing frameworks from its service, and marks unknown facts rather than fabricating them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores a user email and service token locally in config.json after registration.

Mitigation: Use a dedicated email where appropriate, avoid sharing the machine with untrusted users, and verify that the agent platform can protect or clear stored config.json credentials.

Risk: Draft requests and document context are sent to the third-party service at gongwen-api.xyz.

Mitigation: Do not send confidential or sensitive drafts unless the user trusts the service and its handling of submitted content.

Risk: Broad trigger behavior and paid-service flows can consume quota or prompt payment during normal document-drafting interactions.

Mitigation: Review quota prompts before continuing, confirm payment intent explicitly, and monitor remaining free or paid usage.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yourtsao/skills/gongwen-writting)
- [Publisher profile](https://clawhub.ai/user/yourtsao)
- [Word export guide](artifact/references/word-export.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown or plain text official-document drafts, with optional Word/docx formatting guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May store user email and service token in local config.json after registration; generated drafts can include placeholder markers for missing facts.]

## Skill Version(s):

1.0.42 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
