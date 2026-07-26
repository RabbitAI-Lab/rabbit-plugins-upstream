## Description: <br>
Generates short-form Chinese text from a user-supplied topic after a paid order and payment credential are completed. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[laoguihui09-cmyk](https://clawhub.ai/user/laoguihui09-cmyk) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users can ask an agent to create a short Chinese passage from a topic or writing request. The workflow is intended for paid fulfillment, requiring order creation, payment processing, and service execution before returning the generated text. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends the user's prompt and payment credential to a remote service and stores order records locally, including the original prompt. <br>
Mitigation: Do not use sensitive personal, financial, secret, or confidential content unless the publisher and remote service are trusted. <br>
Risk: The security review reports that the skill asks the agent to reveal internal reasoning during Chinese interaction. <br>
Mitigation: Remove the reasoning-disclosure instruction before normal use. <br>
Risk: The release was flagged as suspicious by the authoritative security scan because it handles paid orders and credentials with limited disclosure. <br>
Mitigation: Review the payment flow, remote service behavior, and local order storage before installing or running the skill. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/laoguihui09-cmyk/skills/scripts) <br>
- [Remote service](https://web.kihb.shop) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [Plain text response with command output handling] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns payment status values and, when successful, generated short-form text.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
