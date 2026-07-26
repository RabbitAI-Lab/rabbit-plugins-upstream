## Description: <br>
Agnes Vision helps agents analyze images with the agnes-2.0-flash multimodal model for description, OCR, object recognition, and related visual understanding tasks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruokkkkk](https://clawhub.ai/user/ruokkkkk) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill when they need to route image description, OCR, comparison, or object-recognition tasks through Agnes instead of the agent's native image reader, including workflows that need output consistent with Agnes models. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Images are uploaded to Agnes's remote API for analysis, which can expose sensitive screenshots, documents, or other private content. <br>
Mitigation: Use the skill only with images you are comfortable sending to Agnes, and avoid sensitive screenshots or documents unless that exposure is acceptable. <br>
Risk: The release includes an apparent API key in config.json. <br>
Mitigation: Remove or replace the bundled config.json key before use, and prefer an environment-managed API key such as AGNES_API_KEY. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration guidance] <br>
**Output Format:** [Plain text from stdout, with operational errors on stderr.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires one or more image paths, optional prompt/model/API-key settings, and network access to Agnes's API.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
