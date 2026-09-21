## Description:

Intercom helps agents read, create, update, and delete Intercom data through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Support, operations, and developer teams use this skill to inspect Intercom contacts, conversations, tickets, companies, articles, admins, tags, events, counts, and job status, and to perform confirmed contact and conversation updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can install the OOMOL CLI by piping a remote install script into a shell.

Mitigation: Review the OOMOL CLI installation path before use and prefer verified official documentation or a package manager.

Risk: The skill can operate on sensitive customer-support data in Intercom.

Mitigation: Connect only an Intercom workspace where the agent is allowed to read contacts, conversations, tickets, and related records.

Risk: Write and destructive actions can change Intercom records or close conversations.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running write or destructive actions.

## Reference(s):

- [ClawHub Intercom skill page](https://clawhub.ai/oomol/skills/oo-intercom)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Intercom](https://www.intercom.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce oo CLI commands that return JSON responses from Intercom actions.]

## Skill Version(s):

1.0.5 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
