## Description: <br>
This skill lets agents search and read Fivetran resources through the OOMOL oo CLI using an OOMOL-connected Fivetran account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to inspect Fivetran hybrid deployment agents, external log services, and transformation projects through configured OOMOL and Fivetran access. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill relies on OOMOL's oo CLI and a connected Fivetran account. <br>
Mitigation: Install and use it only when comfortable routing Fivetran access through the connected OOMOL account. <br>
Risk: Future connector versions could expose write or destructive actions. <br>
Mitigation: Keep normal use to listed get and list actions, and require explicit user confirmation before any write or destructive action. <br>
Risk: Payloads can become incorrect if connector schemas change. <br>
Mitigation: Inspect the live action schema with oo connector schema before constructing each payload. <br>


## Reference(s): <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [Fivetran homepage](https://fivetran.com) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, JSON, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only get and list actions return data with a meta.executionId when run through the oo CLI.] <br>

## Skill Version(s): <br>
1.0.0 (source: metadata and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
