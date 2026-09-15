## Description:

Mails (mails.so). Use this skill for Mails requests involving email validation through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to validate individual email addresses, create Mails batch validation jobs, and retrieve validation batch results from a connected OOMOL/Mails account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup may direct users to run unverified remote installer scripts on their machine.

Mitigation: Review the installer path first and prefer a verified, pinned, or package-manager-based oo CLI installation method.

Risk: Creating a validation batch changes service state and submits a list of email addresses to the connected service.

Mitigation: Confirm the exact payload and intended effect with the user before running batch creation.

Risk: Email addresses submitted for validation are shared with the connected OOMOL/Mails service.

Mitigation: Use the skill only for email addresses the user is authorized to process through that service.

## Reference(s):

- [Mails homepage](https://mails.so)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-mails-so)
- [OOMOL CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [Mails icon](https://static.oomol.com/logo/third-party/Mails.so.svg)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance, Markdown]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are returned as JSON when commands are run with --json.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
