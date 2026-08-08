## Description: <br>
Api Doc Writer helps developers create REST API documentation, interface specifications, examples, status-code guidance, authentication notes, and change records in Markdown. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill to draft, normalize, and review REST API documentation for new interfaces, multi-module projects, webhook integrations, and interface reviews. It is not intended for reverse engineering closed APIs, generating application frameworks, running API tests, or providing mock services. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad read, write, and command authority could affect project files or run commands outside the documentation task. <br>
Mitigation: Review each proposed tool use and keep the skill limited to generating or editing API documentation from inputs you provide. <br>
Risk: External API, callback, or command behavior may expose data if allowed without review. <br>
Mitigation: Do not provide secrets or broad project access, and allow external callbacks or command execution only when explicitly requested and understood. <br>
Risk: Generated API documentation may include incorrect, stale, or overly broad security guidance. <br>
Mitigation: Have the responsible engineering team review generated endpoint details, authentication behavior, status codes, and security recommendations before publication. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, shell commands, configuration] <br>
**Output Format:** [Markdown documentation with tables, JSON examples, REST endpoint examples, and occasional shell configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include structured API documentation sections, RESTful review notes, status-code tables, security recommendations, and troubleshooting guidance.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata; artifact frontmatter reports 1.0.2) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
