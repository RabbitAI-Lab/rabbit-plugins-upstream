## Description:

Omise (omise.co). Use this skill for ANY Omise request: reading, creating, updating, and deleting data through the OOMOL oo CLI connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate connected Omise accounts through OOMOL, including account and balance lookups, charge retrieval and listing, and customer create, read, update, list, and delete workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install the required oo CLI by running a remotely fetched shell script.

Mitigation: Review the install script or manually install the oo CLI from a trusted source before allowing the install command.

Risk: The skill can run write and destructive Omise customer actions through a connected account.

Mitigation: Require explicit user confirmation for customer updates or deletions, including the target customer and exact payload.

## Reference(s):

- [Omise homepage](https://www.omise.co)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-omise)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration, Guidance]

**Output Format:** [Markdown with inline bash, PowerShell, text, and JSON command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands return JSON responses from the oo CLI connector when run with --json.]

## Skill Version(s):

1.0.1 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
