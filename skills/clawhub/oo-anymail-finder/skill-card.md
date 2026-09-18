## Description:

Anymail Finder helps an agent search for verified company, decision-maker, and individual work emails, check account credits, and verify email deliverability through an OOMOL-connected Anymail Finder account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to find and verify professional email addresses with Anymail Finder from an agent workflow. It is suited for account-aware email discovery tasks where the user has already connected Anymail Finder through OOMOL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote shell installer commands that could execute unverified code if run automatically.

Mitigation: Treat CLI installation as a manual user decision, inspect official OOMOL installation documentation, and prefer a pinned or otherwise verifiable installer before execution.

Risk: Email discovery and verification can return professional contact data from a connected Anymail Finder account.

Mitigation: Use the skill only for user-authorized searches and review requested lookup targets before spending account credits or using returned contact data.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/oomol/skills/oo-anymail-finder)
- [Anymail Finder homepage](https://anymailfinder.com/)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, JSON, configuration guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the oo CLI, an authenticated OOMOL account, and a connected Anymail Finder account; connector responses include data and meta.executionId.]

## Skill Version(s):

1.0.2 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
