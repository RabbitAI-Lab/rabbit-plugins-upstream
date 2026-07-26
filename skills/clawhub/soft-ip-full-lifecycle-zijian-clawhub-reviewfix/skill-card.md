## Description: <br>
Software intellectual property full lifecycle self-assessment for Chinese software copyright applications, covering material completeness review, compliance verification, and registration readiness audit while using a third-party clawtip flow for order creation and payment verification. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jinyu12166](https://clawhub.ai/user/jinyu12166) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to assess whether Chinese software copyright application materials are complete, consistent, and ready for registration review. It provides local review guidance and uses a paid verification workflow before service fulfillment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The consultation question, order number, and encrypted payment credential are sent to api.ideaidea.com.cn for paid verification and fulfillment. <br>
Mitigation: Use the skill only when that third-party verification flow is acceptable, and avoid entering confidential source code, contract text, or sensitive company details in the question field. <br>
Risk: Order metadata is cached in a local order JSON file after the payment flow. <br>
Mitigation: Delete the local order JSON after payment and service completion when continued local retention is not needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jinyu12166/skills/soft-ip-full-lifecycle-zijian-clawhub-reviewfix) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/jinyu12166) <br>
- [Third-party verification service](https://api.ideaidea.com.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command snippets and JSON-like status output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Chinese-language interaction; service access depends on clawtip payment verification.] <br>

## Skill Version(s): <br>
3.1.33 (source: evidence release, SKILL.md frontmatter, and version history) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
