## Description: <br>
Enables an agent to operate Accredible Certificates through an OOMOL-connected account for reading, creating, searching, listing, and deleting credentials and groups. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to manage Accredible certificate credentials and credential groups from an agent workflow through the OOMOL connector. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create Accredible credentials and delete certificate data. <br>
Mitigation: Review the exact payload and expected effect before approving creation, and require explicit approval for deletion targets. <br>
Risk: The skill depends on OOMOL-mediated access to the user's Accredible account. <br>
Mitigation: Install only when OOMOL should mediate account access, and confirm the account connection and scopes before use. <br>
Risk: Installing the oo CLI from a remote installer may introduce supply-chain risk. <br>
Mitigation: Verify the oo CLI installer source before installation, or use an already installed trusted CLI. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-accredible-certificates) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [Accredible Certificates homepage](https://www.accredible.com/) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API Calls, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires live connector schema inspection before payload construction; write and destructive actions require user confirmation.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
