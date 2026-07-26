## Description: <br>
Detects fail-open insecure defaults such as hardcoded secrets, weak authentication, and permissive security settings that can let applications run insecurely in production. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[atlas-secint](https://clawhub.ai/user/atlas-secint) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, security reviewers, and platform teams use this skill during audits, code reviews, configuration reviews, and pre-deployment checks to find production-reachable insecure defaults. It helps distinguish fail-open patterns from fail-secure behavior that crashes or requires explicit secure configuration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may inspect sensitive application code and configuration while searching for insecure defaults. <br>
Mitigation: Run it only in repositories intended for audit and avoid pointing the agent at unrelated private directories. <br>
Risk: Search matches can be misleading when examples, tests, templates, or fail-secure code resemble vulnerable defaults. <br>
Mitigation: Verify runtime behavior and production reachability before treating a match as a finding. <br>


## Reference(s): <br>
- [Insecure Defaults Examples and Counter-Examples](examples.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown findings and review guidance with suggested search commands and evidence snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Findings should include location, pattern, behavioral verification, production impact, and exploitation rationale when supported by evidence.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
