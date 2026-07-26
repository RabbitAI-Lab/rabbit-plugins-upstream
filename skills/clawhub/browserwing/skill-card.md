## Description: <br>
Control browser automation through HTTP API, including page navigation, element interaction, data extraction, accessibility snapshot analysis, screenshots, JavaScript execution, and batch operations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chenhg5](https://clawhub.ai/user/chenhg5) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and automation engineers use this skill to control a BrowserWing Executor through HTTP APIs for navigation, element interaction, form filling, browser inspection, and structured data extraction. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can drive sensitive browser actions, including logins, uploads, purchases, posts, account changes, screenshots, page dumps, network inspection, and JavaScript execution. <br>
Mitigation: Connect only to a trusted local or secured BrowserWing Executor, and require explicit user approval before sensitive browser actions. <br>
Risk: Broad browser automation can expose page content, credentials, or authenticated sessions if the executor is misconfigured or connected to an untrusted endpoint. <br>
Mitigation: Use scoped sessions and credentials, limit executor access to trusted networks, and review planned operations before deployment. <br>


## Reference(s): <br>
- [BrowserWing GitHub repository](https://github.com/browserwing/browserwing) <br>
- [ClawHub skill page](https://clawhub.ai/chenhg5/skills/browserwing) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline bash and JSON code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a BrowserWing Executor endpoint configured with BROWSERWING_EXECUTOR_URL; outputs HTTP API workflows, curl examples, and response handling guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
