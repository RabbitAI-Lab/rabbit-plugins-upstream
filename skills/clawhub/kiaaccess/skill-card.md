## Description:

kiaaccess helps an agent answer Kia Access and Kia Owners account requests for vehicle status, location, EV charging, and confirm-gated vehicle commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect an agent to their own Kia Access or Kia Owners account so it can answer vehicle-status questions and, when explicitly confirmed, run supported Kia vehicle commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to run an unpinned external MCP package with Kia credentials.

Mitigation: Pin kiaaccess-mcp to a reviewed version and store credentials in a secret manager or tightly permissioned user-level environment.

Risk: Vehicle command tools can affect a real Kia vehicle, including door lock and unlock control when all write tools are enabled.

Mitigation: Keep KIA_WRITE_MODE=none unless commands are needed, require explicit confirmation for every command, and enable all only when door lock and unlock risk is accepted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/kiaaccess)
- [npm package: kiaaccess-mcp](https://www.npmjs.com/package/kiaaccess-mcp)

## Skill Output:

**Output Type(s):** [guidance, configuration, shell commands]

**Output Format:** [Markdown with JSON and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide an agent to call MCP tools for Kia account setup, vehicle reads, and confirm-gated commands.]

## Skill Version(s):

0.8.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
