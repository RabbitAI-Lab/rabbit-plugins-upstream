## Description: <br>
Admin CLI for Lemon Squeezy stores. View orders, subscriptions, and customers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[abakermi](https://clawhub.ai/user/abakermi) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and store operators use this skill to manage Lemon Squeezy stores from the command line, including viewing orders, subscriptions, customers, and stores. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a Lemon Squeezy API key and can expose access if the key is shared or printed in unsafe contexts. <br>
Mitigation: Use the least-privileged API key available, avoid sharing terminal output that contains secrets, and rotate the key if it is exposed. <br>
Risk: Command output can include customer emails, revenue, order, and subscription information. <br>
Mitigation: Review terminal output before sharing screenshots, logs, or transcripts and redact customer or revenue data when needed. <br>
Risk: The skill depends on the ls-admin CLI being available in the agent environment. <br>
Mitigation: Install and trust the ls-admin CLI before use, and confirm commands in a non-production context when possible. <br>


## Reference(s): <br>
- [Lemon Squeezy API settings](https://app.lemonsqueezy.com/settings/api) <br>
- [ClawHub skill page](https://clawhub.ai/abakermi/skills/lemonsqueezy-admin) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance, Text] <br>
**Output Format:** [Markdown with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the LEMONSQUEEZY_API_KEY environment variable.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata; artifact frontmatter reports 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
