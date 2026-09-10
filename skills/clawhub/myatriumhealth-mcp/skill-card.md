## Description:

Read MyAtriumHealth data such as test results, medications, allergies, immunizations, health issues, visits, goals, and messages from a signed-in Chrome session using the fpx CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technically proficient MyAtriumHealth users can use this skill to script one-shot reads of their own patient portal data through an already authenticated browser session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Shell commands can access highly sensitive patient portal data while the browser session is authenticated.

Mitigation: Install and run the skill only when this access is intentional, and review each endpoint command before execution.

Risk: Command output may contain protected health information.

Mitigation: Avoid logging, storing, or sharing raw output; project only the fields needed for the task.

Risk: A stale or missing browser session can produce empty or misleading responses.

Mitigation: Use the provided session checks before data reads and sign in again when the helper reports an unavailable or expired session.

Risk: Long-lived pairing grants can keep broad portal access available from the shell.

Mitigation: Revoke the fpx or browser extension pairing when this access is no longer needed.

## Reference(s):

- [MyAtriumHealth endpoints](artifact/references/endpoints.md)
- [MyAtriumHealth shell helpers](artifact/references/mah.sh)
- [MyAtriumHealth portal](https://my.atriumhealth.org/myatriumhealth)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/myatriumhealth-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell commands and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The generated guidance is intended to produce local shell commands that may emit protected health information from the signed-in user's own MyAtriumHealth account.]

## Skill Version(s):

0.3.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
