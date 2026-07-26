## Description: <br>
Helps pharmaceutical R&D teams screen and rank candidate drug targets for a disease using evidence strength, druggability, safety risk, and cited references. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[unisound-llm](https://clawhub.ai/user/unisound-llm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and pharmaceutical R&D teams use this skill to prepare disease and candidate target inputs, compute a local priority ranking, and request a Markdown analysis from a remote medical model. The skill is for drug-target research triage and does not provide clinical diagnosis, treatment advice, or drug efficacy conclusions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: User-provided disease, target lists, evidence notes, and references are sent to a disclosed remote medical-model endpoint. <br>
Mitigation: Install and run the skill only when that data sharing is acceptable for the intended workflow and data classification. <br>
Risk: Optional parsing of Office, PDF, and image inputs can involve local converter and OCR tools. <br>
Mitigation: Prefer JSON or trusted structured files; process untrusted documents only in an isolated runtime with patched converter tools. <br>
Risk: Generated target-screening analysis may be incomplete or unsuitable for direct research decisions. <br>
Mitigation: Require qualified scientific review and experimental validation before using the ranking or narrative to guide R&D decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/unisound-llm/skills/unisound-target-screening) <br>
- [Open Targets Database reference skill](https://agent-skills.md/skills/x-cmd/skill/opentargets-database) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, guidance] <br>
**Output Format:** [UTF-8 JSON with structured ranked-target data and a Markdown analysis in the text field] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a user-supplied appkey for the remote medical-model call; optional preprocessing can save prepared JSON for review.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
