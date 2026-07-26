## Description: <br>
Extracts structured fields from Chinese mainland business license images, including unified social credit code, company name, legal representative, registered capital, establishment date, business scope, and address. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[scnet-sugon](https://clawhub.ai/user/scnet-sugon) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users, business operations teams, and developers use this skill to convert authorized Chinese mainland business license files into structured OCR data for review or downstream processing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Business license files and extracted business identity data are sent to SCNet's OCR service. <br>
Mitigation: Use the skill only for documents the user is authorized to process, and confirm the configured SCNET_API_BASE before sending files. <br>
Risk: The SCNET_API_KEY grants access to the OCR service and could be exposed if pasted into chat or stored with broad permissions. <br>
Mitigation: Store the key in the local config file or environment with restrictive permissions, and do not paste the key into conversations. <br>


## Reference(s): <br>
- [Sugon-Scnet OCR API docs](references/api-docs.md) <br>
- [Business license field summary](assets/templates/fields-summary.md) <br>
- [SCNet website](https://www.scnet.cn) <br>
- [ClawHub skill page](https://clawhub.ai/scnet-sugon/skills/business-license-ocr) <br>


## Skill Output: <br>
**Output Type(s):** [text, json] <br>
**Output Format:** [JSON printed to standard output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns the API data array after removing confidence fields from each result item.] <br>

## Skill Version(s): <br>
1.0.5 (source: SKILL.md frontmatter, skill.yaml, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
