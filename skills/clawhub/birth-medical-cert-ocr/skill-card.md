## Description: <br>
This skill invokes Scnet's remote OCR service to extract structured data from birth medical certificates when the user explicitly requests that document type, and it is not intended for general OCR. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[scnet-sugon](https://clawhub.ai/user/scnet-sugon) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent users use this skill to send an authorized birth medical certificate image or PDF to Scnet OCR and receive structured identity, birth, parent, medical institution, and certificate fields. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Birth-certificate images and extracted family, identity, and medical data are sent to Scnet's remote OCR service. <br>
Mitigation: Use the skill only with legal authority or guardian consent, confirm that remote processing is acceptable, and delete local images and cached results after use. <br>
Risk: The release needs review because its metadata and code may allow broader OCR use than the narrow birth-certificate description claims. <br>
Mitigation: Keep agent triggers limited to explicit birth-medical-certificate requests and prefer a version that hardcodes or validates BIRTH_CERTIFICATE before upload. <br>
Risk: The Scnet API key can expose account access if pasted into chat or stored loosely. <br>
Mitigation: Store SCNET_API_KEY in a protected local environment file or environment variable and avoid sharing it in prompts, logs, or transcripts. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/scnet-sugon/skills/birth-medical-cert-ocr) <br>
- [Sugon-Scnet OCR API documentation summary](references/api-docs.md) <br>
- [Birth certificate field summary](assets/templates/fields-summary.md) <br>
- [Scnet website](https://www.scnet.cn) <br>


## Skill Output: <br>
**Output Type(s):** [json, text, guidance] <br>
**Output Format:** [JSON on stdout with plain-text setup and error messages] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires SCNET_API_KEY; sends input files to Scnet's OCR API; documented rate limit is 10 QPS.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
