## Description: <br>
Nyne.ai helps agents operate Nyne.ai through an OOMOL-connected account for company and person search, enrichment, and usage reporting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to inspect Nyne.ai action schemas, submit company or person search and enrichment requests, poll asynchronous results, and review account usage through the OOMOL CLI connector. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Write-tagged actions submit Nyne.ai search or enrichment requests using the connected account. <br>
Mitigation: Review the live action schema and confirm the exact payload and expected effect with the user before running write-tagged actions. <br>
Risk: The skill relies on the user's OOMOL-connected Nyne.ai account and may require first-time CLI setup or sign-in. <br>
Mitigation: Install or authenticate the oo CLI only when the user intends to use the connector and a command fails for setup or connection reasons. <br>
Risk: Nyne.ai actions can consume account credits or be blocked by billing limits. <br>
Mitigation: Use the usage-reporting action when cost or quota matters, and stop retrying if the connector reports insufficient credit. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-nyne-ai) <br>
- [Nyne.ai homepage](https://nyne.ai) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, guidance, text] <br>
**Output Format:** [Markdown guidance with oo CLI commands and JSON payloads or responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Responses may include connector data and execution metadata from Nyne.ai actions.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
