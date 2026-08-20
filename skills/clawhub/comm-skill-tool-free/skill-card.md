## Description:

沟通助手基础版 helps users draft context-aware, empathetic messages from conversation history, emotional cues, relationship context, and communication channel needs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate structured drafts for difficult conversations, customer emails, feedback, requests, and channel-specific messages. It supports lightweight personal communication workflows with tone and relationship-aware guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad file, API credential, command-execution, and network capabilities that are not well scoped to message drafting.

Mitigation: Install and run it in a constrained workspace, and avoid granting shell, broad file-write, API-key, or network access unless the requested access has been independently reviewed.

Risk: Generated communication drafts can be inappropriate for sensitive, high-stakes, or relationship-specific contexts.

Mitigation: Require a human review before sending generated messages, especially for difficult conversations, customer complaints, or consequential decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/comm-skill-tool-free)
- [Publisher profile](https://clawhub.ai/user/thcjp)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Natural-language message drafts with optional JSON, text, or CSV structured output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include execution status, operation logs, tone/channel options, and human-review guidance.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
