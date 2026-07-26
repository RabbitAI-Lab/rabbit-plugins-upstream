## Description: <br>
Operates HubSpot through an OOMOL-connected account for reading, creating, and updating CRM data with the oo CLI connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and business users use this skill to search HubSpot records, inspect CRM schemas, and create or update companies, contacts, deals, CRM objects, activities, and campaign reporting data through an OOMOL-connected HubSpot account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: HubSpot write actions can change CRM business records. <br>
Mitigation: Confirm the exact action, target records, payload, and expected effect with the user before running create, update, manage, or feedback actions. <br>
Risk: The skill depends on an OOMOL account, the oo CLI, OAuth connection state, and account billing. <br>
Mitigation: Review the one-time installer and OAuth connection steps, and use setup or billing actions only after the matching error occurs. <br>
Risk: Payloads can be wrong if they are built from stale assumptions about HubSpot connector schemas. <br>
Mitigation: Fetch the live connector schema for the selected action before constructing JSON payloads. <br>


## Reference(s): <br>
- [ClawHub HubSpot skill page](https://clawhub.ai/oomol/skills/oo-hubspot) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [HubSpot](https://www.hubspot.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with oo CLI commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands may perform HubSpot reads or user-confirmed writes through an OOMOL-connected account.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
