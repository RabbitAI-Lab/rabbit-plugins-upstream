## Description:

Read MyAtriumHealth data from a shell with the fpx CLI by relaying requests through a user's signed-in Chrome tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query their own MyAtriumHealth/MyChart records from shell workflows, including test results, medications, allergies, immunizations, health issues, visits, goals, messages, insurance, care team, and health summary data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access personal health information through a live MyAtriumHealth browser session.

Mitigation: Use it only with the signed-in user's own account and run it in a dedicated browser profile containing only the MyAtriumHealth session.

Risk: Persistent fetchproxy pairing and broad cookie access may outlive the immediate task.

Mitigation: Pin and verify the fetchproxy CLI and extension, revoke the persistent pairing when finished, and avoid use on shared machines.

Risk: Antiforgery tokens and response data could be exposed through shell history, logs, or broad output dumps.

Mitigation: Avoid logging tokens, unset MAH_TOKEN after use, and project large health portal responses with jq before storing or sharing output.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/myatriumhealth-mcp)
- [MyAtriumHealth portal](https://my.atriumhealth.org/myatriumhealth)
- [MyAtriumHealth endpoints](references/endpoints.md)
- [MyAtriumHealth helper script](references/mah.sh)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash commands, jq filters, and JSON response projections]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a signed-in MyAtriumHealth Chrome tab, fetchproxy CLI, Transporter extension, and careful projection of health portal responses.]

## Skill Version(s):

0.4.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
