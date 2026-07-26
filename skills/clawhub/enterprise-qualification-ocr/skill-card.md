## Description: <br>
Enterprise Qualification OCR extracts structured text from business licenses and related organization qualification certificates by sending user-selected images, PDFs, or archives to the Sugon-Scnet OCR API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[scnet-sugon](https://clawhub.ai/user/scnet-sugon) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Employees, external users, and developers use this skill to extract machine-readable JSON fields from enterprise qualification documents such as business licenses, social organization registrations, trade union certificates, religious activity registrations, private non-enterprise registrations, institution legal person certificates, and unified social credit code certificates. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uploads selected business certificate images or PDFs to SCNet's OCR service for recognition. <br>
Mitigation: Use it only for documents you are authorized to process, avoid sensitive or unauthorized records, and confirm that external processing is acceptable for the organization. <br>
Risk: Business qualification documents may contain sensitive company identifiers, names, addresses, legal representatives, registration capital, validity dates, and issuing authorities. <br>
Mitigation: Limit retained local copies and caches after processing, and handle returned JSON as sensitive business data. <br>
Risk: The SCNET_API_KEY can grant access to the OCR service if exposed. <br>
Mitigation: Store the key in the local config file with restricted permissions and do not paste it into chat or shared logs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/scnet-sugon/skills/enterprise-qualification-ocr) <br>
- [Sugon-Scnet OCR API documentation summary](references/api-docs.md) <br>
- [Recognition field summary](assets/templates/fields-summary.md) <br>
- [Scnet website](https://www.scnet.cn) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, JSON, Shell commands, Configuration] <br>
**Output Format:** [JSON emitted to standard output, with command-line guidance and friendly error text when configuration or API calls fail] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires SCNET_API_KEY in a local config file and accepts an OCR type plus a local document path.] <br>

## Skill Version(s): <br>
1.0.5 (source: frontmatter, skill.yaml, and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
