## Description: <br>
Share code snippets and files securely via snipit.sh with AES-256 encryption. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[homecity](https://clawhub.ai/user/homecity) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to share selected code, configuration snippets, logs, diffs, build output, or files through the snipit CLI or curl API, with options such as password protection, burn-after-read, and expiration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may upload credentials, personal data, or production secrets to an external sharing service. <br>
Mitigation: Review the exact content before sharing, redact sensitive values where possible, and use password protection, burn-after-read, and short expirations for sensitive material. <br>
Risk: Using the CLI depends on trusting snipit.sh and the snipit-sh npm package. <br>
Mitigation: Install only when the publisher and package source are trusted in the user's environment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/homecity/skills/snipit) <br>
- [snipit.sh snippets API](https://snipit.sh/api/snippets) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, API calls, configuration] <br>
**Output Format:** [Markdown with bash command examples and curl request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands may upload user-selected content to snipit.sh and can use password, expiration, burn-after-read, language, title, and copy-url options.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
