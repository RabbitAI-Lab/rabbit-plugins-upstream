## Description: <br>
Publish WordPress posts with API and public URL receipts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[leostehlik](https://clawhub.ai/user/leostehlik) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and operators use this skill to publish WordPress posts from agent, scheduled, or OpenClaw workflows and verify that the public artifact exists. It is useful when completion must be backed by both WordPress API state and an HTTP 200 response from the public URL. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can support operational publishing workflows that change public WordPress content. <br>
Mitigation: Use least-privilege WordPress credentials, keep user confirmation gates for publishing decisions, and review deployment targets before execution. <br>
Risk: A scheduler may report success even when no public WordPress post exists. <br>
Mitigation: Verify publication using the WordPress API response and a public URL HTTP 200 receipt after the scheduled publishing window. <br>
Risk: Credential exposure could occur if application passwords, tokens, cookies, or authorization headers are logged or committed. <br>
Mitigation: Store secrets in an env file outside the skill folder, avoid printing secrets, and do not commit real environment files. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/leostehlik/skills/wordpress-receipts) <br>
- [Project homepage](https://github.com/LeoStehlik/wordpress-receipts) <br>
- [README.md](README.md) <br>
- [SKILL.md](SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON receipt examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports include title, URL, WordPress post ID, API status, public HTTP status, and duplicate-skip status when applicable.] <br>

## Skill Version(s): <br>
0.1.2 (source: release evidence and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
