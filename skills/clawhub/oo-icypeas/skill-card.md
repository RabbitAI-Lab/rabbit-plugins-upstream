## Description: <br>
Icypeas lets agents read, create, and update Icypeas data through the OOMOL oo CLI using a connected Icypeas account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to run Icypeas email discovery, email verification, reverse email lookup, domain scans, search-item retrieval, and subscription credit checks through an OOMOL-connected Icypeas account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Write actions can submit Icypeas searches or scans and may use account credits. <br>
Mitigation: Confirm the exact payload and intended effect with the user before running write actions, and check subscription credit status when needed. <br>
Risk: The optional CLI installation command runs an external OOMOL installer. <br>
Mitigation: Run the installer only when the oo CLI is missing and the user trusts the OOMOL installer source; prefer the published install guide. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-icypeas) <br>
- [Icypeas homepage](https://www.icypeas.com) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands use the OOMOL oo CLI and return connector JSON when executed.] <br>

## Skill Version(s): <br>
1.0.1 (source: evidence release and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
