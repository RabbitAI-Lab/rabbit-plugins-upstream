## Description:

Givebutter lets agents search and read Givebutter campaigns, chapters, contacts, funds, recurring plans, and transactions through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve Givebutter fundraising data through an OOMOL-managed connector instead of calling the Givebutter API directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer scripts in first-time setup can execute arbitrary code if the download source is compromised.

Mitigation: Review the setup path first and prefer a packaged, versioned, and verifiable oo CLI installer before installing.

Risk: Connecting Givebutter can grant connector access to donor, contact, campaign, and transaction data.

Mitigation: Connect Givebutter only when that account-level access is acceptable for the intended task.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-givebutter)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Givebutter homepage](https://givebutter.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-oriented connector actions return data and execution metadata; first-time setup may require CLI installation, account sign-in, and Givebutter connection.]

## Skill Version(s):

1.0.2 (source: skill metadata and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
