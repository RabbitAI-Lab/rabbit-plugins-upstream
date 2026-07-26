## Description: <br>
Tinybird (tinybird.co). Use this skill for Tinybird requests involving searching, reading data, running published Pipe endpoints, or executing synchronous SQL queries through OOMOL. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to query Tinybird data sources, inspect data-source metadata, and run published Pipe endpoints through an OOMOL-connected Tinybird account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tinybird queries and endpoint payloads may expose business data visible to the connected OOMOL account. <br>
Mitigation: Review SQL queries and endpoint payloads before execution, and use an OOMOL connection scoped to the minimum Tinybird access needed. <br>
Risk: First-time setup may run an external oo CLI installer. <br>
Mitigation: Run the installer only when the oo CLI is missing and after confirming that the user trusts OOMOL's installer. <br>


## Reference(s): <br>
- [Tinybird homepage](https://www.tinybird.co) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [Tinybird connection setup](https://console.oomol.com/app-connections?provider=tinybird) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-tinybird) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, JSON, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Connector responses include data and meta.executionId when actions run successfully.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
