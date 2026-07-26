## Description: <br>
PartnerStack Partner helps agents retrieve PartnerStack Partner marketplace programs, partnerships, payouts, and rewards through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill when they need to search or read PartnerStack Partner account data, including marketplace programs, partnerships, payouts, and rewards, without calling the PartnerStack API directly. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can expose connected PartnerStack Partner account data, including payouts and rewards, in the agent conversation. <br>
Mitigation: Install it only for accounts where the agent should read PartnerStack Partner data, and keep requests specific to the data retrieval task. <br>
Risk: First-time setup may require installing the OOMOL CLI and connecting the account. <br>
Mitigation: Review the CLI install source and account connection flow before first use. <br>


## Reference(s): <br>
- [PartnerStack Partner homepage](https://partnerstack.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-partner-stack-partner) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schema checks before action execution and returns JSON responses from the oo CLI.] <br>

## Skill Version(s): <br>
1.0.0 (source: release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
