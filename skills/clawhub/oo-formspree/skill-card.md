## Description: <br>
Formspree (formspree.io) support for searching and reading Formspree data through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to inspect the live Formspree connector schema and list submissions for a Formspree form through an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Formspree submissions can contain personal or business-sensitive information. <br>
Mitigation: Use the skill only with an intended OOMOL-connected Formspree account and review returned submission data before sharing it outside the authorized workflow. <br>
Risk: The connector depends on local oo CLI installation, sign-in, Formspree connection state, scopes, credentials, and billing status. <br>
Mitigation: Run the requested read action first, then follow the documented setup or recovery step only when the matching command failure occurs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-formspree) <br>
- [Formspree homepage](https://formspree.io) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, JSON, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only Formspree submission access through the oo CLI connector.] <br>

## Skill Version(s): <br>
1.0.0 (source: server evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
