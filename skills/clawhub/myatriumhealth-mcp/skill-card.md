## Description:

Helps agents read a signed-in user's MyAtriumHealth records through a Chrome tab using shell commands, without running the MyAtriumHealth MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People with a signed-in MyAtriumHealth account and their authorized agents can retrieve their own test results, medications, allergies, visits, and other health records for review or scripting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent browser-bridge pairing can relay requests from a signed-in healthcare session.

Mitigation: Use a dedicated shell and browser profile; remove the fpx profile or revoke the bridge pairing when finished.

Risk: Patient records and the MAH_TOKEN session token can be exposed through logs or shared environments.

Mitigation: Avoid sharing logs or environments containing MAH_TOKEN, and limit record output to necessary fields.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/myatriumhealth-mcp)
- [Endpoint recipes](references/endpoints.md)
- [Shell helpers](references/mah.sh)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Shell commands, JSON]

**Output Format:** [Markdown guidance and shell commands; JSON health records from portal requests]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Contains sensitive personal health information; filter responses to the fields needed.]

## Skill Version(s):

1.3.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
