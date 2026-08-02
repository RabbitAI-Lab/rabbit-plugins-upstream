## Description: <br>
Beebole helps agents inspect schemas and execute JSON-friendly Beebole GraphQL queries or mutations through the OOMOL oo CLI connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to operate a connected Beebole account from an agent, first checking the live connector schema and then running Beebole GraphQL actions through oo CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The generic GraphQL action can run mutations against connected Beebole account data. <br>
Mitigation: Require explicit user confirmation for every GraphQL mutation and verify the exact payload and affected records before execution. <br>
Risk: A user expecting a read-only helper may underestimate the effect of an execute_graphql request. <br>
Mitigation: Treat GraphQL mutations as write operations, inspect the live action schema before building payloads, and explain the intended effect before running them. <br>


## Reference(s): <br>
- [Beebole homepage](https://beebole.com) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-beebole) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill guides schema inspection and oo CLI connector execution; connector responses are JSON objects containing data and meta.executionId.] <br>

## Skill Version(s): <br>
1.0.0 (source: evidence release and frontmatter metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
