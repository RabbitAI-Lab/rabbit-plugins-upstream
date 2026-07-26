## Description: <br>
Freshsales helps agents operate Freshsales CRM contacts through the OOMOL connector and oo CLI, including reading, creating, updating, and deleting contact records. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, operators, and agents working with Freshsales use this skill to inspect connector schemas and run Freshsales contact workflows through an OOMOL-connected account. It supports contact lookup, listing, creation, updates, deletion, and contact filter discovery. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Approved write or delete actions can modify or remove Freshsales CRM contact data. <br>
Mitigation: Confirm the exact payload, target contact, and expected effect with the user before running write or destructive actions. <br>
Risk: Requests built from stale assumptions can fail or affect unintended fields. <br>
Mitigation: Inspect the live Freshsales action schema immediately before constructing each connector payload. <br>


## Reference(s): <br>
- [Freshsales ClawHub Listing](https://clawhub.ai/oomol/skills/oo-freshsales) <br>
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol) <br>
- [Freshsales Homepage](https://www.freshworks.com/crm/sales/) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live Freshsales connector schemas to shape command payloads.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
