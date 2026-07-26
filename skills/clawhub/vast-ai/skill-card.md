## Description: <br>
Provision and manage on-demand GPUs on VAST.ai, including search by GPU and price, renting containers, retrieving SSH connection details, and checking account balance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sschepis](https://clawhub.ai/user/sschepis) <br>

### License/Terms of Use: <br>
ISC <br>


## Use Case: <br>
Developers and agent operators use Vast Ai to search for rentable VAST.ai GPU offers, rent containers, retrieve SSH connection details, and monitor balance and hourly burn rate before and after rentals. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Rent actions create real paid VAST.ai resources that may continue billing until stopped or destroyed. <br>
Mitigation: Before approving a rent action, confirm the offer ID, hourly price, image, expected runtime, and the plan for stopping or destroying the instance. <br>
Risk: The VAST_API_KEY grants access to the user's VAST.ai account. <br>
Mitigation: Store the key in a secure secret or environment mechanism, do not expose it in prompts or logs, and avoid DEBUG logging around failures. <br>
Risk: Production use with unpinned or stale dependencies can increase supply-chain and maintenance risk. <br>
Mitigation: Use pinned, updated dependencies for production deployments and review dependency changes before release. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/sschepis/skills/vast-ai) <br>
- [Publisher profile](https://clawhub.ai/user/sschepis) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON CLI results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires VAST_API_KEY and can trigger authenticated VAST.ai API actions, including paid GPU rentals.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
