## Description:

Insites (insites.com) lets an agent read, create, and update Insites data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to let an agent operate an OOMOL-connected Insites account for website audit workflows, including listing audits, retrieving audit results, and starting new SEO and AEO audits after payload confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can start new Insites audits, which changes connected account state and may consume account resources.

Mitigation: Review the exact start_audit payload and intended effect before approving the write action.

Risk: The skill depends on a trusted one-time oo CLI installation and OOMOL account connection.

Mitigation: Perform CLI installation, sign-in, and Insites connection setup only as trusted setup actions when required by command failures.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-insites)
- [Insites homepage](https://insites.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before payload construction; write actions require user confirmation.]

## Skill Version(s):

1.0.0 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
