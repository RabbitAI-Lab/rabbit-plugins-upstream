## Description: <br>
Viggle helps agents operate Viggle through an OOMOL-connected account by reading account data, creating characters and render jobs, importing templates, checking render status, and managing Viggle resources. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to route Viggle tasks through the OOMOL oo CLI, including listing resources, creating reusable characters or scenes, starting render jobs, and retrieving completed video URLs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use a connected OOMOL/Viggle account to create render jobs, create reusable characters or scenes, check credits, and soft-delete Viggle resources. <br>
Mitigation: Approve write or delete actions only after reviewing the exact payload, target resource, and expected effect. <br>
Risk: Installing or relying on the optional oo CLI adds a separate trust decision outside the skill content. <br>
Mitigation: Review the CLI installation source and account connection flow before installing or authenticating. <br>


## Reference(s): <br>
- [ClawHub Viggle Skill](https://clawhub.ai/oomol/skills/oo-viggle) <br>
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol) <br>
- [Viggle Homepage](https://viggle.ai) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands should inspect the live connector schema before constructing action payloads.] <br>

## Skill Version(s): <br>
1.0.0 (source: server evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
