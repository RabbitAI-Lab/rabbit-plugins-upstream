## Description: <br>
Expert guidance on navigating, understanding, configuring, troubleshooting, and automating Clawdbot using official documentation and config snippets. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[janhcla](https://clawhub.ai/user/janhcla) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to find the relevant Clawdbot documentation, retrieve configuration examples, troubleshoot setup issues, and summarize recent documentation changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Helper scripts may access docs.clawd.bot and store documentation data in a local cache under ~/.cache/clawddocs. <br>
Mitigation: Review network access expectations before running scripts and clear the local cache when cached documentation should not persist. <br>
Risk: Configuration snippets include placeholder token fields that could be mistaken for places to store real secrets in shared files. <br>
Mitigation: Use snippets as templates only and keep real tokens out of repositories and shared configuration examples. <br>
Risk: WhatsApp QR login connects an account to the Clawdbot workflow. <br>
Mitigation: Run QR login only with an account intended for that connection. <br>


## Reference(s): <br>
- [Clawdbot Documentation](https://docs.clawd.bot/) <br>
- [ClawHub Skill Page](https://clawhub.ai/janhcla/skills/clawdbot-documentation-expert) <br>
- [Common Clawdbot Configuration Snippets](snippets/common-configs.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline shell commands and JSON configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May cite Clawdbot documentation URLs and may suggest local helper scripts for sitemap, search, cache, index, and change-tracking workflows.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
