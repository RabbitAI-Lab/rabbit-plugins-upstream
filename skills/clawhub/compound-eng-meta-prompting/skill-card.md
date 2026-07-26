## Description: <br>
Structured reasoning modifiers (/think, /verify, /adversarial, /edge, /confidence, /assumptions, etc.) to stress-test decisions, surface assumptions, or enumerate edge cases. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[iliaal](https://clawhub.ai/user/iliaal) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, architects, reviewers, and other agent users use this skill to request structured reasoning patterns before committing to important designs, architecture decisions, security-sensitive reviews, or ambiguous plans. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad activation language may change the agent's response style or reasoning structure when the user did not explicitly request a modifier. <br>
Mitigation: Use or enable the skill only when automatic structured reasoning is desired; otherwise disable it or invoke comparable reasoning patterns explicitly. <br>
Risk: Structured reasoning outputs can still contain incorrect assumptions, incomplete verification, or misleading confidence labels. <br>
Mitigation: Review outputs before relying on them for critical design, architecture, security, or production decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-meta-prompting) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, guidance] <br>
**Output Format:** [Markdown or JSON depending on the requested reasoning pattern] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include marked answer sections such as VERIFIED ANSWER, REVISED ANSWER, confidence tiers, assumptions, comparisons, edge cases, or counterarguments.] <br>

## Skill Version(s): <br>
4.2.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
