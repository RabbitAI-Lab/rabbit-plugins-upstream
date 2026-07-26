## Description: <br>
Runscope lets an agent inspect and read Runscope API Monitoring account, bucket, test, environment, and result data through the OOMOL oo CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operations teams use this skill to query Runscope API Monitoring data from an OOMOL-connected Runscope account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read Runscope account and monitoring data through an OOMOL-connected Runscope account. <br>
Mitigation: Install and use it only where the agent is allowed to access that Runscope data, and keep actions scoped to the requested get and list operations. <br>
Risk: First-time setup may require running a remote oo CLI installer if the oo CLI is not already installed. <br>
Mitigation: Review the remote installer before running it, or install the oo CLI through an approved internal process. <br>


## Reference(s): <br>
- [ClawHub Runscope skill page](https://clawhub.ai/oomol/skills/oo-runscope) <br>
- [Runscope API Monitoring](https://www.blazemeter.com/api-monitoring) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON connector responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live oo connector schema inspection before constructing action payloads.] <br>

## Skill Version(s): <br>
1.0.0 (source: server evidence and artifact metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
