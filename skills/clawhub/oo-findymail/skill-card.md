## Description:

Findymail support for searching and reading professional contact data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, employees, and developers use this skill to retrieve Findymail credit information, search for professional email contacts by name or domain, list company employees, and verify email addresses through an OOMOL-connected Findymail account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes remote installer commands that pipe downloaded scripts directly to a shell.

Mitigation: Do not run installer commands automatically; review installer contents first or use an official signed or version-pinned installation method.

Risk: Findymail actions may consume account credits or fail when billing, authentication, or connector state is not ready.

Mitigation: Check the live action schema and handle authentication, connection, and billing errors before retrying user-requested actions.

## Reference(s):

- [Findymail homepage](https://www.findymail.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub Findymail skill page](https://clawhub.ai/oomol/skills/oo-findymail)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before submitting action payloads.]

## Skill Version(s):

1.0.3 (source: release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
