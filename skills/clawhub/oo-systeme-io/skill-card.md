## Description:

Operates Systeme.io through OOMOL's oo CLI connector to read, create, update, and delete contacts, tags, webhooks, courses, enrollments, subscriptions, and contact fields.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Operators and agents use this skill to work with a connected Systeme.io account for contact, tag, webhook, course, enrollment, and subscription workflows through the OOMOL connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can connect to a Systeme.io account with read/write authority through OOMOL.

Mitigation: Install and use it only when the publisher is trusted and the connected account permissions match the intended workflow.

Risk: Installer commands can run remote scripts.

Mitigation: Do not let an agent run remote installer commands automatically; install the oo CLI through a verified method first.

Risk: Contact tag actions can change Systeme.io state without the same confirmation language used for other writes.

Mitigation: Treat attach_contact_tag and detach_contact_tag as write actions and require explicit confirmation of the contact, tag, and expected effect before execution.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-systeme-io)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Systeme.io](https://systeme.io)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, API Calls, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
