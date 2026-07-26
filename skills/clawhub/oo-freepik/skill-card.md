## Description: <br>
Magnific (Freepik) connector that lets an agent search stock images and templates, retrieve resource metadata, and create download URLs through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to operate Magnific (Freepik) from an agent, including searching Freepik resources, retrieving details by resource ID, and creating download URLs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Freepik/Magnific requests route through OOMOL and may use a connected account to create download URLs. <br>
Mitigation: Install and connect the OOMOL CLI only if the user trusts OOMOL and needs this integration; confirm download URL creation requests before running them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-freepik) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>
- [Magnific (Freepik) homepage](https://www.magnific.com/freepik) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
