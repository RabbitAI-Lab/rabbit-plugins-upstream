## Description: <br>
Demo of x402 payment protocol by fetching a protected image. Triggers: '演示x402-payment' or 'demo x402-payment' <br>

This skill is for demonstration purposes and not for production usage. <br>

## Publisher: <br>
[wzc1206](https://clawhub.ai/user/wzc1206) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and external users can use this skill to demonstrate an x402 payment flow on the TRON network by requesting a protected image, completing the payment protocol, and displaying the retrieved image. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use a TRON private key to perform payment actions without a clear confirmation or spending boundary. <br>
Mitigation: Use a dedicated low-balance TRON wallet and require visible confirmation of network, amount, recipient, and signing details before any payment is allowed. <br>
Risk: The payment flow depends on the x402_payment_tron dependency and the destination service. <br>
Mitigation: Review the x402_payment_tron dependency and verify the destination service before installing or running the skill. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/wzc1206/skills/tron-x402-payment-demo) <br>
- [Protected x402 TRON demo resource](http://x402-tron-demo.sunagent.ai/protected) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands] <br>
**Output Format:** [Markdown with status text and retrieved image display guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses TRON_PRIVATE_KEY and should delete the temporary image file after display.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
