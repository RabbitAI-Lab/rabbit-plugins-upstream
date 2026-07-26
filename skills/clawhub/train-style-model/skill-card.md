## Description: <br>
Fine-tune a reusable brand, style, or character model (a LoRA) from a small set of reference images, then generate on-brand imagery from any prompt. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[runware](https://clawhub.ai/user/runware) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and creative teams use this skill to train a private, versioned style LoRA from a curated image ZIP and then generate consistent brand, character, or illustration assets from prompts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Training image ZIPs may contain content the user is not allowed to upload or reuse for model training. <br>
Mitigation: Confirm rights to the images before upload and use only datasets the user is authorized to process. <br>
Risk: A public dataset URL or trained model can expose private brand or character material. <br>
Mitigation: Prefer private, time-limited, least-privilege dataset URLs and keep the trained model private while testing. <br>
Risk: Retraining can produce regressions or make rollback difficult if versions are overwritten. <br>
Mitigation: Version retrains and test on prompts outside the training set before using the model for production assets. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/runware/skills/train-style-model) <br>
- [Worked recipes](references/examples.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, JSON, configuration] <br>
**Output Format:** [Markdown guidance with JSON API request and response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides asynchronous training submission, polling, model registration, and generation with the trained AIR.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
