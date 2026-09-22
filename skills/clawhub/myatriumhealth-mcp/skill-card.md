## Description:

Read MyAtriumHealth patient portal data such as test results, medications, allergies, immunizations, health issues, visits, goals, insurance, care team, and messages from a shell by relaying requests through a signed-in Chrome tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technically proficient users use this skill to retrieve their own MyAtriumHealth data for scripting, one-shot inspection, and JSON projection without running the myatriumhealth-mcp server. It is intended for authenticated access to the signed-in user's own patient portal data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can relay broad authenticated requests from a signed-in MyAtriumHealth browser session and expose highly sensitive health information.

Mitigation: Use it only with the documented read-only recipes, only for the signed-in user's own account, and revoke the fpx/Transporter pairing when ongoing access is no longer needed.

Risk: Command output may contain protected health information that could be retained in shell history, terminal logs, files, or shared debugging artifacts.

Mitigation: Project responses with jq to the minimum fields needed, avoid saving raw responses, and keep outputs out of shared logs or files.

Risk: Expired sessions, MFA prompts, or a missing relay tab can produce misleading empty or login-page responses.

Mitigation: Check session state with mah_signed_in before interpreting empty results, and sign in again when the helper reports a missing bridge or auth wall.

## Reference(s):

- [MyAtriumHealth endpoint recipes](references/endpoints.md)
- [MyAtriumHealth shell helpers](references/mah.sh)
- [MyAtriumHealth portal](https://my.atriumhealth.org/myatriumhealth)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/myatriumhealth-mcp)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code, JSON]

**Output Format:** [Markdown guidance with shell commands and jq-oriented JSON output recipes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs can contain protected health information and should be minimized, projected, and handled as sensitive data.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
