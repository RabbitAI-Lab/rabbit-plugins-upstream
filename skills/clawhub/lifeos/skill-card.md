## Description: <br>
LifeOS teaches an agent to read, search, append to, and update a LifeOS or Obsidian PARA vault through the public @life-os/cli command-line tool. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[quanru](https://clawhub.ai/user/quanru) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and LifeOS users use this skill to let an agent inspect tasks, periodic notes, PARA theme notes, tags, and AI Wiki pages in a local vault, then make requested note or task updates through the LifeOS CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can cause an agent to read and modify a real LifeOS or Obsidian vault. <br>
Mitigation: Install it only for vaults where agent access is intended, prefer an explicit vault= path, and review proposed file changes before write commands. <br>
Risk: AI Wiki maintenance and note creation can overwrite or reshape durable vault content. <br>
Mitigation: Read the existing target note first, keep vault backups or version control, and use overwrite only after confirming the target and content. <br>
Risk: The skill install workflow runs a live npm package that can overwrite installed agent skill files. <br>
Mitigation: Run skill install only when the exact @life-os/cli package version is trusted. <br>


## Reference(s): <br>
- [LifeOS website](https://lifeos.md/) <br>
- [LifeOS ClawHub skill page](https://clawhub.ai/quanru/skills/lifeos) <br>
- [Command reference](references/commands.md) <br>
- [LifeOS AI Wiki maintenance rules](references/ai-wiki.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and optional JSON CLI output.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May direct the agent to run npm CLI commands that read or modify a local LifeOS or Obsidian vault.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
