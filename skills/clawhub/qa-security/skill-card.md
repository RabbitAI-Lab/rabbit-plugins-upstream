## Description: <br>
Code quality audit guidance, security review, vulnerability identification patterns, and dependency risk assessment delivered through clawtip verification. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jinyu12166](https://clawhub.ai/user/jinyu12166) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to request code quality and security review guidance, including vulnerability identification patterns, dependency risk assessment, security best practices, and testing strategy suggestions. The service is gated by clawtip payment verification before the review result is delivered. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a paid clawtip-gated workflow. <br>
Mitigation: Install and run it only if you are comfortable with the disclosed payment flow and required clawtip dependency. <br>
Risk: The question submitted for review is stored in a local order JSON file and no automatic cleanup is documented. <br>
Mitigation: Do not include secrets, API keys, or highly sensitive code details in the question field; remove local order files when they are no longer needed. <br>
Risk: The workflow depends on payment-related environment configuration. <br>
Mitigation: Set required clawtip environment values through normal secret-handling practices and avoid embedding them in shared prompts or files. <br>


## Reference(s): <br>
- [qa-security on ClawHub](https://clawhub.ai/jinyu12166/skills/qa-security) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with shell command snippets and payment authorization status text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The workflow creates local order metadata and then checks clawtip payment authorization before service execution.] <br>

## Skill Version(s): <br>
1.0.27 (source: server release metadata; artifact frontmatter states 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
