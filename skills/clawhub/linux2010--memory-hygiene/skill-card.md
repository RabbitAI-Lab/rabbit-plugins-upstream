## Description: <br>
Audit, clean, and optimize Clawdbot's vector memory (LanceDB). Use when memory is bloated with junk, token usage is high from irrelevant auto-recalls, or setting up memory maintenance automation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linux2010](https://clawhub.ai/user/linux2010) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to audit Clawdbot LanceDB memory, reduce noisy auto-recall behavior, and apply memory cleanup and reseeding practices. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill includes commands that can delete the user's LanceDB vector memory. <br>
Mitigation: Back up ~/.clawdbot/memory/lancedb/ and verify the target path before running wipe commands. <br>
Risk: The recurring maintenance cron can repeatedly delete memory if configured without recovery planning. <br>
Mitigation: Avoid recurring deletion unless a tested reseed and recovery process is in place. <br>


## Reference(s): <br>
- [Memory Hygiene homepage](https://github.com/xdylanbaker/memory-hygiene) <br>
- [ClawHub skill page](https://clawhub.ai/linux2010/skills/memory-hygiene) <br>
- [Publisher profile](https://clawhub.ai/user/linux2010) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline shell commands and JSON configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes manual memory audit, wipe, reseed, auto-capture configuration, and maintenance cron guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
