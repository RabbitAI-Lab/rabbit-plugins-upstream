## Description:

Operate GetResponse campaigns, contacts, newsletters, tags, custom fields, and newsletter statistics through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to read, create, update, and delete GetResponse data through the oo CLI after connecting their GetResponse account in OOMOL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup section includes remote installer snippets for the oo CLI.

Mitigation: Do not let an agent run installer snippets automatically; install the oo CLI from a verified, versioned source with checksum or signature verification.

Risk: The skill can create, update, or delete GetResponse campaigns and contacts.

Mitigation: Confirm the exact target, payload, connected account, and expected effect with the user before running write or destructive actions.

Risk: Actions run against the user's OOMOL-connected GetResponse account.

Mitigation: Verify the intended OOMOL account and GetResponse connection before using the skill for account-changing operations.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-getresponse)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [GetResponse Homepage](https://www.getresponse.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON command payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands inspect live connector schemas and run GetResponse actions through the oo CLI.]

## Skill Version(s):

1.0.2 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
