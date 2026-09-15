## Description:

DocsAutomator (docsautomator.co) helps agents read, create, and update DocsAutomator data through the OOMOL-connected oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate DocsAutomator from an authorized OOMOL account, including listing automations, inspecting template placeholders, creating documents, checking async job status, and reviewing queue statistics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer commands that execute downloaded shell or PowerShell scripts.

Mitigation: Do not let the agent run those installers automatically; install the oo CLI only through a trusted and verified method.

Risk: DocsAutomator connector actions operate through an account-authorized OOMOL connection, and write actions can create documents or queue generation jobs.

Mitigation: Inspect the live action schema and confirm the exact payload and expected effect with the user before running write actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-docsautomator)
- [DocsAutomator homepage](https://www.docsautomator.co)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Guidance, Configuration]

**Output Format:** [Markdown guidance with oo CLI shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include DocsAutomator action results such as document URLs, signing metadata, job handles, job status, automation details, placeholders, or queue statistics.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
