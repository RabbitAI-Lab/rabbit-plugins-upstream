## Description: <br>
TheirStack (theirstack.com) helps agents search and read TheirStack data through the OOMOL-connected `oo` CLI instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to query TheirStack through an OOMOL-connected account for credit balance checks, company search, job search, and company technographics. It helps agents inspect live connector schemas and run read-only TheirStack actions with structured JSON payloads. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use the connected TheirStack account for broad search and credit-balance read requests. <br>
Mitigation: Review the requested connector action and payload before execution, and re-check permissions if future connector actions are marked write or destructive. <br>
Risk: Connector schemas may change over time. <br>
Mitigation: Inspect the live TheirStack connector schema before constructing each payload. <br>
Risk: Authentication, connection, credential, or billing failures can block execution. <br>
Mitigation: Use the documented first-time setup and billing guidance only after a command fails with the matching error. <br>


## Reference(s): <br>
- [TheirStack homepage](https://theirstack.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [TheirStack skill on ClawHub](https://clawhub.ai/oomol/skills/oo-theirstack) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration instructions, API Calls, JSON, Guidance] <br>
**Output Format:** [Markdown with inline bash code blocks and JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only connector actions use live schema inspection before execution; OOMOL handles TheirStack credentials server-side.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
