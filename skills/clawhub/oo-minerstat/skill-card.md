## Description: <br>
Minerstat (minerstat.com). Use this skill for searching and reading Minerstat data through the OOMOL connector instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and mining operations teams use this skill to query Minerstat coin profitability, hardware benchmark, and mining pool data through an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill depends on the external OOMOL CLI and a connected Minerstat account, so first use can fail if the CLI is missing, authentication is expired, or the Minerstat connection is unavailable. <br>
Mitigation: Review the OOMOL CLI installation and account connection steps before first use, and only run setup steps when an action fails with the matching setup or authentication error. <br>
Risk: Connector payloads may become inaccurate if the live Minerstat action schema changes. <br>
Mitigation: Fetch the live connector schema before each action and build payloads from that schema. <br>
Risk: Account credentials are handled through the OOMOL-connected account rather than directly by the agent. <br>
Mitigation: Keep credentials server-side through OOMOL and avoid asking users to paste raw Minerstat tokens into the conversation. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-minerstat) <br>
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol) <br>
- [Minerstat Homepage](https://minerstat.com/) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Responses are returned from the OOMOL connector as JSON with data and execution metadata.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
