## Description: <br>
Run a user-controlled Reddit account within subreddit rules, with karma phase gates, quotas, posting and reply guidance, and removal recovery. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alexbloch-ia](https://clawhub.ai/user/alexbloch-ia) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Account owners and operators use this skill to guide an agent or cron-driven workflow for Reddit posting, replies, quota checks, blocker handling, and local run recaps while staying within subreddit rules. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide an agent to publish public posts or replies from a Reddit account controlled by the user. <br>
Mitigation: Use it only with an account you control, review top-level posts before publishing, and stop for human approval when the skill marks an action as blocked or requiring approval. <br>
Risk: Local run history can retain Reddit post URLs, reply URLs, karma counts, subreddit state, ideas, and learnings in plain markdown. <br>
Mitigation: Delete the local memory directory when run history should not be retained, and follow the documented pruning practice for older entries. <br>
Risk: Optional webhook alerts can send recap data, public action links, karma, and blocker text to third-party services. <br>
Mitigation: Leave the webhook empty unless third-party delivery and storage of recap data is acceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/alexbloch-ia/skills/reddit-account-operations) <br>
- [OpenClaw homepage](https://openclaw.ai) <br>
- [Skill metadata repository](https://github.com/AlexBloch-IA/reddit-account-operations) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown with configuration snippets, shell commands, templates, and operational checklists] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces guidance for browser-based Reddit account operations, local markdown memory files, and optional recap webhook content.] <br>

## Skill Version(s): <br>
2.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
