## Description:

EmailListVerify lets an agent operate EmailListVerify through an OOMOL-connected account for email verification, credit checks, and batch email-list workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to verify individual email addresses, check disposable domains, manage batch email-list verification jobs, download results, delete completed lists, and check EmailListVerify credits through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence flags an unsafe remote CLI installer in the setup guidance.

Mitigation: Prefer a verified, version-pinned installation path for the oo CLI before using the skill.

Risk: The security evidence flags broader OOMOL CLI command access than the EmailListVerify workflow needs.

Mitigation: Use the skill only in a signed-in OOMOL context you trust, and review commands before execution.

Risk: The skill includes upload and delete actions that can change or remove EmailListVerify data.

Mitigation: Confirm the exact payload, target list, and intended effect with the user before running write or destructive actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-emaillistverify)
- [EmailListVerify Homepage](https://emaillistverify.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, text]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON when commands are run with --json.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
