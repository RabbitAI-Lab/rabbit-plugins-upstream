## Description:

Use this skill for Veremark requests, including reading, creating, and updating Veremark data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to operate Veremark through an OOMOL-connected account for creating background-check requests, retrieving request status and results, and listing criteria or requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may run a remote installer script directly in the shell.

Mitigation: Review the oo CLI installation path and prefer a verifiable package or official installer before installing.

Risk: The create_request action changes Veremark state and may create a candidate background-check request.

Mitigation: Confirm candidate details, request criteria, and the intended effect with the user before running write actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-veremark)
- [Veremark homepage](https://www.veremark.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides an agent to inspect live connector schemas before sending action payloads and returns JSON responses from the oo CLI.]

## Skill Version(s):

1.0.1 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
