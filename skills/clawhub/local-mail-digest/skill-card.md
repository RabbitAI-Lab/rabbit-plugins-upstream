## Description:

Local Mail Digest turns batches of email into structured summaries with priority, project grouping, todos, and deadlines for host agents or self-hosted Python use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aks-666888](https://clawhub.ai/user/aks-666888)

### License/Terms of Use:

MIT-0

## Use Case:

Email users and agent operators use this skill to convert connector-exported, IMAP-fetched, or pasted email into a structured digest of priorities, projects, todos, and deadlines. It supports host-agent workflows that need local email summaries for review, automation, reminders, or downstream task handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Mailbox data can contain sensitive personal, business, legal, or financial information.

Mitigation: Review the skill before installation and test with non-sensitive mail samples before using it on a real mailbox.

Risk: Optional LLM, webhook, and notification paths can send email-derived sender names, subjects, deadlines, or summary content outside the local computer.

Mitigation: Use --llm only with an endpoint you control, avoid --webhook unless the destination is approved for the content, and treat local-only privacy claims as applying only to the default local file-processing path.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/aks-666888/skills/local-mail-digest)
- [Server-resolved source repository](https://github.com/aks-666888/local-mail-digest)
- [Server-resolved release commit](https://github.com/aks-666888/local-mail-digest/tree/d04dc4d5bde61bf99f842792a79bd96485306db4)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown, HTML, JSON, and concise text notifications]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Structured JSON can include total, high, mid, and low counts plus per-email sender, subject, date, priority, project, todos, deadlines, summary, and body excerpt.]

## Skill Version(s):

0.1.0 (source: server release metadata; SKILL.md frontmatter declares 2.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
