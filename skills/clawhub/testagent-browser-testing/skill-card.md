## Description: <br>
Helps agents perform functional browser testing for web products using Playwright MCP, browser-use CLI, and the OpenClaw built-in browser, from test planning through bug evidence and reporting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wangyin717](https://clawhub.ai/user/wangyin717) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, QA engineers, and product teams use this skill to plan and run functional browser tests against authorized web products, capture bug evidence, produce a test report, and optionally file confirmed defects. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can delegate browser sessions, network access, and local testing configuration to an agent. <br>
Mitigation: Use it only on systems and targets you control or are authorized to test, with test accounts and isolated browser profiles. <br>
Risk: SSRF allowlist edits, tunnels, proxies, CAPTCHA bypass, sandbox changes, and gateway restarts can broaden access beyond the intended test scope. <br>
Mitigation: Treat those changes as administrator-level actions, restrict them to approved domains, review them before use, and roll them back after testing. <br>
Risk: Screenshots and bug reports can capture sensitive product, account, or customer data. <br>
Mitigation: Prefer test data, review captured evidence before sharing or filing, and file defects only after explicit user confirmation. <br>


## Reference(s): <br>
- [Browser Testing Reference](REFERENCE.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown reports with inline shell commands, configuration snippets, screenshot file references, and defect-filing guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce screenshot file paths and proposed defect metadata for user-confirmed issue filing.] <br>

## Skill Version(s): <br>
1.0.6 (source: ClawHub release metadata; artifact frontmatter reports 1.4.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
