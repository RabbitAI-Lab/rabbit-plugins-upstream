## Description: <br>
Dispatches paid tasks to physical robots through the Robot Task Protocol on the Spraay x402 gateway, with escrow-protected payment and operator registration workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[plagtech](https://clawhub.ai/user/plagtech) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, robot buyers, and robot operators use this skill to discover RTP-capable robots, dispatch paid tasks through the Spraay x402 gateway, poll task status, and register or manage robots on the network. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Dispatched tasks can cause physical robots to move, actuate, or perform work in the real world. <br>
Mitigation: Before dispatch, verify the robot, task parameters, physical environment, and safety expectations with the user. <br>
Risk: Buyer workflows can trigger x402 micropayments and task fees. <br>
Mitigation: Confirm the total fee and wallet payment behavior before any paid request or dispatch. <br>
Risk: All requests and payment flows depend on the configured Spraay gateway URL. <br>
Mitigation: Use a trusted SPRAAY_GATEWAY_URL and avoid dispatching tasks through an untrusted gateway. <br>


## Reference(s): <br>
- [Robot Task Protocol on ClawHub](https://clawhub.ai/plagtech/skills/robot-task-protocol) <br>
- [Spraay gateway](https://gateway.spraay.app) <br>
- [Spraay app](https://spraay.app) <br>
- [Spraay docs](https://docs.spraay.app) <br>
- [RTP spec](https://github.com/plagtech/rtp-spec) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with curl command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires SPRAAY_GATEWAY_URL plus curl and jq; paid buyer endpoints use an x402 wallet payment flow.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
