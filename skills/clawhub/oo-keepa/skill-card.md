## Description: <br>
Keepa (keepa.com). Use this skill for Keepa search and read requests through the OOMOL oo CLI instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to run Keepa connector actions for Amazon product discovery, product history, product snapshots, seller snapshots, category search, best-seller lookup, and token-status checks through an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill relies on OOMOL as an intermediary for Keepa access and may require installing and signing in to the oo CLI. <br>
Mitigation: Install and sign in to the oo CLI only when the user trusts OOMOL for the Keepa connection and accepts the setup requirement. <br>
Risk: Connector calls can use incorrect payloads if the live action contract is not checked first. <br>
Mitigation: Inspect the action schema with `oo connector schema` before constructing payloads, then run the connector with JSON matching that schema. <br>
Risk: Setup, connection, or billing recovery commands can interrupt a normal request if run proactively. <br>
Mitigation: Run first-time setup, auth, connection, or billing recovery steps only after the matching command failure occurs. <br>


## Reference(s): <br>
- [Keepa homepage](https://keepa.com/) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses oo CLI connector schema and run commands; connector responses are JSON objects containing data and meta.executionId.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
