## Description: <br>
Automates Twitter/X account operations including posting, scheduling, engagement, search, monitoring, analytics, follower management, media handling, and exports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[millymilton](https://clawhub.ai/user/millymilton) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Social media operators, community managers, and developers use this skill to manage Twitter/X workflows, monitor trends and mentions, analyze engagement, and prepare account actions through an agent. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill covers powerful Twitter/X account actions without clearly bounded approvals. <br>
Mitigation: Require manual approval for posting, replies, direct messages, follows, blocks, moderation, and bulk actions before an agent executes them. <br>
Risk: OAuth credentials and local logs, caches, archives, or exports could expose account or user data. <br>
Mitigation: Use least-privilege OAuth credentials, avoid high-value or personal accounts, protect stored files, and periodically clear retained data. <br>
Risk: Webhook-based alerts or integrations could send account activity to an unintended destination. <br>
Mitigation: Verify webhook destinations before use and restrict them to trusted endpoints. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or text with inline CLI commands, configuration values, and optional CSV/JSON export descriptions.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may propose account actions, analytics exports, webhook usage, and local credential or archive paths.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
