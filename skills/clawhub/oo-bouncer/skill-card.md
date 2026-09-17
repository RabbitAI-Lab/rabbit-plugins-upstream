## Description:

Bouncer helps agents operate the Bouncer connector through the OOMOL-connected oo CLI for email, domain, batch verification, toxicity list, and credit-balance requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to verify email addresses and domains, manage Bouncer batch and toxicity-list jobs, retrieve verification results, and check account credits through an OOMOL-connected Bouncer account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup can run remote installer scripts directly.

Mitigation: Review official oo CLI installation documentation or use a pinned, verifiable installer before allowing installation commands to run.

Risk: Write and destructive Bouncer actions can change stored jobs or results and may consume account credits.

Mitigation: Confirm the exact action, target, and payload with the user before running write, delete, finish, or batch verification operations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-bouncer)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Bouncer homepage](https://www.usebouncer.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
