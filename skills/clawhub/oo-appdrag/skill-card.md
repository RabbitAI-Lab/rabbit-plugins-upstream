## Description:

AppDrag helps agents inspect connector schemas and run AppDrag Cloud Backend API functions through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate AppDrag through an OOMOL-connected account, including inspecting live action schemas and invoking AppDrag Cloud Backend API functions with JSON payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill describes AppDrag search and read workflows, but its only action can invoke AppDrag backend functions that may mutate state depending on the function, method, and payload.

Mitigation: Inspect the live action schema and confirm the exact function, HTTP method, payload, and expected effect before executing potentially mutating calls.

Risk: Setup guidance includes remote installer commands that pipe downloaded scripts into a shell.

Mitigation: Prefer a verified CLI installation path or inspect the installer separately before running it.

Risk: Commands operate through the user's connected AppDrag account with server-side credential injection.

Mitigation: Use the minimum necessary connected-account permissions and only perform authentication or connection remediation after a matching command failure.

## Reference(s):

- [ClawHub AppDrag Skill](https://clawhub.ai/oomol/skills/oo-appdrag)
- [AppDrag Homepage](https://appdrag.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector commands may return JSON data with execution metadata.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
