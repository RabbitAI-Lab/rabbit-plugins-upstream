## Description: <br>
Create on-brand social media carousels and single-image posts and schedule them to LinkedIn, Instagram, TikTok, and Threads from a single command. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[iammuneeb](https://clawhub.ai/user/iammuneeb) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, marketers, and developers use PostNitro to create, import, and schedule branded carousel or single-image social posts through a scriptable CLI workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses PostNitro credentials and publishing permissions to create or schedule social posts. <br>
Mitigation: Install it only for intended PostNitro publishing workflows, prefer an environment variable or per-command API key on shared machines, and clear saved credentials when they are no longer needed. <br>
Risk: A SCHEDULED post can publish live to selected social accounts. <br>
Mitigation: Confirm the target account and scheduled time before using SCHEDULED, and use DRAFT when the publishing details are uncertain. <br>
Risk: Delete and disconnect commands can cancel scheduled posts or affect linked social accounts. <br>
Mitigation: Use destructive commands only with explicit confirmation and review the selected schedule or social account before passing --yes. <br>
Risk: Large batches or AI image generation can consume paid PostNitro credits. <br>
Mitigation: Warn users before large batch runs or AI image generation and verify that the account has the required subscription and quota. <br>


## Reference(s): <br>
- [PostNitro CLI command reference](references/cli-reference.md) <br>
- [PostNitro skill examples](examples/EXAMPLES.md) <br>
- [PostNitro homepage](https://postnitro.ai) <br>
- [ClawHub skill page](https://clawhub.ai/iammuneeb/skills/postnitro) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, JSON, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands emit JSON output and can create drafts, schedule posts, or manage linked social accounts when executed with valid PostNitro credentials.] <br>

## Skill Version(s): <br>
1.2.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
