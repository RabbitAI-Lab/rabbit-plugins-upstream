## Description:

GenPage (genpage.ai). Use this skill for ANY GenPage request: reading, creating, updating, and deleting data through the OOMOL GenPage connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage GenPage workspaces, campaigns, audiences, leads, analytics, variables, and credit balance through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Some GenPage actions that link or unlink audiences and campaigns may change account state even when not tagged as write actions.

Mitigation: Review the exact action and payload before execution, and get explicit user confirmation for audience-campaign linking or unlinking and other state-changing operations.

Risk: CLI install and login steps connect the user's environment to OOMOL and GenPage services.

Mitigation: Only run install, login, or connection commands when the user intends to connect the account and trusts the OOMOL CLI.

## Reference(s):

- [GenPage homepage](https://www.genpage.ai/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub GenPage skill page](https://clawhub.ai/oomol/skills/oo-genpage)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs OOMOL oo CLI connector schema and action commands; action responses are JSON with data and meta.executionId.]

## Skill Version(s):

1.0.0 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
