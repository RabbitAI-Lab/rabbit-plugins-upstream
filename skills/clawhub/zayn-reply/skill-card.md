## Description:

Generates channel- and language-appropriate customer replies from the customer's message, confirmed facts, communication goal, and commitment boundaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zaynpeng](https://clawhub.ai/user/zaynpeng)

### License/Terms of Use:

MIT-0

## Use Case:

Business users and sales or support teams use this skill to decide whether a customer message can be answered safely and to draft replies for Email, WhatsApp, WeChat, LinkedIn, or similar channels. It emphasizes confirmed facts, unanswered questions, commitment limits, and reply risk before producing customer-facing text.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Drafted customer replies may include incorrect commitments if the user provides unconfirmed facts or unclear business boundaries.

Mitigation: Provide only confirmed facts, mark unresolved items explicitly, set commitment boundaries, and review the generated reply before sending.

Risk: Customer or business-sensitive context may be included in prompts unnecessarily.

Mitigation: Provide only the specific customer message, confirmed facts, and business boundaries needed for the reply.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zaynpeng/skills/zayn-reply)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown with structured analysis, risk notes, and draft reply text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the customer message, confirmed facts, reply goal, commitment boundaries, channel, and output language before producing a stable final reply.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
