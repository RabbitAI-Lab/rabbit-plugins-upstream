## Description:

Systeme.io lets an agent read, create, update, and delete Systeme.io contacts, tags, webhooks, courses, enrollments, subscriptions, and contact fields through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, operators, and developers use this skill to manage Systeme.io customer, tag, webhook, course, enrollment, and subscription workflows from an agent through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup recommends executing remote installer scripts for the oo CLI.

Mitigation: Review the installer path before installing and prefer a verified, versioned source or manual inspection of the downloaded installer.

Risk: The skill can create, update, cancel, and delete business data in Systeme.io.

Mitigation: Connect only the intended Systeme.io account, inspect live action schemas, confirm write payloads with the user, and require explicit approval for destructive actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-systeme-io)
- [Systeme.io Homepage](https://systeme.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before running actions; command responses are JSON objects that include data and execution metadata.]

## Skill Version(s):

1.0.3 (source: artifact frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
