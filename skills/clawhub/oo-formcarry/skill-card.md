## Description:

Enables agents to manage Formcarry forms and submissions through OOMOL's oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect Formcarry action schemas, create and delete forms, and list submissions through an OOMOL-connected Formcarry account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that execute downloaded scripts in a shell.

Mitigation: Use a verified installation method from the publisher before first use; do not let an agent run curl|bash or irm|iex installer commands without independent review.

Risk: The skill can create and delete Formcarry forms, including destructive deletion.

Mitigation: Confirm exact payloads and target form IDs with the user before write or destructive actions.

Risk: Operations depend on OOMOL as an intermediary for Formcarry credentials and requests.

Mitigation: Install only if the user accepts OOMOL-mediated Formcarry operations and has connected the intended account.

## Reference(s):

- [Formcarry homepage](https://formcarry.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-formcarry)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
