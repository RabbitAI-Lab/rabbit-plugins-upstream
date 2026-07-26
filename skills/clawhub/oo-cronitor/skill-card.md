## Description: <br>
Cronitor (cronitor.io). Use this skill for ANY Cronitor request - reading, creating, updating, and deleting data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to manage Cronitor monitors through an OOMOL-connected account, including listing, fetching, creating, updating, and deleting monitors. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Create and update actions can change Cronitor monitor state. <br>
Mitigation: Confirm the exact payload and expected effect with the user before running actions tagged as write operations. <br>
Risk: Delete actions can remove Cronitor monitor data. <br>
Mitigation: Confirm the target monitor and obtain explicit approval before running destructive actions. <br>
Risk: Connector payloads can drift if schemas change. <br>
Mitigation: Inspect the live connector schema before constructing each action payload. <br>


## Reference(s): <br>
- [Cronitor homepage](https://cronitor.io) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub Cronitor skill](https://clawhub.ai/oomol/skills/oo-cronitor) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Configuration guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Connector responses include data and metadata with an execution ID.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
