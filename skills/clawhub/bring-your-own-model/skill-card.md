## Description: <br>
Upload and use an existing LoRA or checkpoint on Runware by assigning an AIR, validating modelUpload fields, and generating with the imported model. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[runware](https://clawhub.ai/user/runware) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and creators use this skill to import their own hosted safetensors LoRA, LyCORIS, VAE, embedding, or checkpoint into Runware, assign a stable AIR, and run inference with the uploaded model. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Uploaded model weights may contain proprietary or sensitive intellectual property. <br>
Mitigation: Use a signed, time-limited download URL, keep the Runware model private unless publication is intended, and record the AIR and uniqueIdentifier for later update or deletion. <br>
Risk: Choosing the wrong model category or architecture can make the imported model fail or produce poor inference results. <br>
Mitigation: Resolve the live modelUpload schema before upload and match architecture to the base family used to train the weights. <br>
Risk: Upload task polling can remain in processing even after the model is usable. <br>
Mitigation: Confirm readiness by reissuing the idempotent upload, checking model availability, or running a small imageInference against the assigned AIR. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/runware/skills/bring-your-own-model) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown guidance with Runware API task fields and workflow checks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides schema validation, AIR assignment, readiness checks, and lifecycle management for imported models.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
