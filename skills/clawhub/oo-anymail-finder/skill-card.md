## Description:

Anymail Finder helps an agent use an OOMOL-connected Anymail Finder account to find verified company, decision-maker, and person work email addresses, verify email deliverability, and check account credits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to perform Anymail Finder lookups through the oo CLI with a connected OOMOL account. It supports contact discovery, deliverability checks, and account-credit lookup while requiring schema inspection before connector calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup can install the oo CLI and create persistent OOMOL authentication or connector state.

Mitigation: Run setup steps only after an auth, connection, or missing-command failure and confirm the user intends to connect Anymail Finder through OOMOL.

Risk: Connector calls may consume account credits or submit personal and business contact data.

Mitigation: Inspect the action schema first and review payloads with the user before searches involving contact data or billable lookups.

## Reference(s):

- [Anymail Finder homepage](https://anymailfinder.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-anymail-finder)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are returned as JSON containing data and meta.executionId when actions run successfully.]

## Skill Version(s):

1.0.0 (source: server evidence release.version and artifact metadata.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
