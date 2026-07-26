## Description: <br>
Bannerbear (bannerbear.com) helps agents operate Bannerbear through an OOMOL-connected account for reading templates and images, verifying auth, and creating images from templates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to work with Bannerbear projects through the OOMOL connector, including template discovery, image lookup, auth checks, and synchronous image creation. It is intended for users who have the oo CLI installed, are signed in to OOMOL, and have connected Bannerbear. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Image creation can change Bannerbear state and may consume connected account resources. <br>
Mitigation: Confirm the exact create_image_sync payload and expected effect with the user before running the write action. <br>
Risk: The skill may ask to install or invoke the oo CLI when it is unavailable. <br>
Mitigation: Review the oo CLI install command before execution and install only when the user intends to operate Bannerbear through OOMOL. <br>
Risk: Authentication, connection, scope, credential, or billing failures can block connector actions. <br>
Mitigation: Use first-time setup, connection repair, or billing steps only after a matching command failure instead of proactively opening auth or connection flows. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-bannerbear) <br>
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [Bannerbear Homepage](https://www.bannerbear.com/) <br>
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, JSON] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON connector payloads or responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before building payloads; write actions require user confirmation of the exact payload and effect.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
