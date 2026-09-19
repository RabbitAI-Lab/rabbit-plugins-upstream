## Description:

Salesflare skill for reading, creating, and updating Salesflare data through the OOMOL oo CLI instead of direct API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Salesflare CRM records through an OOMOL-connected account, including listing and retrieving data plus creating or updating accounts, contacts, opportunities, and tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote shell installer commands without verification.

Mitigation: Use an official, versioned OOMOL CLI installation method with checksum or signature verification before installing.

Risk: The skill can create or update Salesflare CRM records through write actions.

Mitigation: Fetch the live action schema and confirm the exact payload and expected effect with the user before executing any write action.

Risk: Salesflare access is mediated by OOMOL as a third-party connector.

Mitigation: Install only when the deployment is comfortable granting OOMOL connector access to the relevant Salesflare data.

## Reference(s):

- [Salesflare homepage](https://salesflare.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub Salesflare skill](https://clawhub.ai/oomol/skills/oo-salesflare)
- [ClawHub publisher profile: oomol](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution; write actions require user confirmation of payload and effect.]

## Skill Version(s):

1.0.2 (source: SKILL.md frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
