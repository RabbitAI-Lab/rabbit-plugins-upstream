## Description:

Browser Use enables agents to operate Browser Use Cloud through an OOMOL-connected account using the `oo` CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to inspect Browser Use action schemas, run browser-agent tasks, check sessions and messages, view account billing information, and stop active Browser Use Cloud sessions through an authenticated OOMOL connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow includes pipe-to-shell installation commands for the `oo` CLI.

Mitigation: Do not let an agent run the installer automatically; manually review or verify the CLI installation path before installing.

Risk: The connector can access a user's Browser Use account through OOMOL and run Browser Use Cloud actions.

Mitigation: Install only when the publisher is trusted and the user is comfortable granting the connector access to the Browser Use account.

Risk: Browser tasks and session control actions can affect live browser sessions.

Mitigation: Confirm the exact task, payload, target session, and expected effect before running `run_task` or `stop_session`, especially when actions could change data.

## Reference(s):

- [Browser Use homepage](https://browser-use.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub Browser Use skill page](https://clawhub.ai/oomol/skills/oo-browser-use)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include Browser Use Cloud session data, messages, billing details, action schemas, task execution results, or confirmation guidance for write actions.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
