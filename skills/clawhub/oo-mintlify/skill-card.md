## Description:

Operates Mintlify documentation deployments through an OOMOL-connected account, including deployment status checks and production or branch preview deployment triggers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and documentation operators use this skill to check Mintlify deployment status and trigger production or branch preview deployments. It routes Mintlify actions through OOMOL and requires confirmation before write actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The one-line remote installer commands can run unverified code on a user's machine.

Mitigation: Review and verify the OOMOL CLI installer source before running remote install commands, or install the CLI through a trusted package path.

Risk: Write actions can trigger Mintlify production or branch preview deployments.

Mitigation: Confirm the exact action, project, branch, and payload with the user before executing any deployment-triggering command.

## Reference(s):

- [Mintlify homepage](https://www.mintlify.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-mintlify)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Write actions require user confirmation before execution.]

## Skill Version(s):

1.0.3 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
