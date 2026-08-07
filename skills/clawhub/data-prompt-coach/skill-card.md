## Description: <br>
Guides users through data-analysis prompt design and tutorial distillation with eight scenario routes, 26 methods, CRISP-DM workflow support, and review gates for self-updates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edwardwason](https://clawhub.ai/user/edwardwason) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, analysts, and developers use this skill to convert data-analysis needs into structured prompts, templates, validation checklists, and reports. It can also distill tutorials into reusable methods with review gates before modifying the skill library. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill includes web scraping, session/key simulation, external cloud write, and elevated scheduled automation guidance that may be sensitive in some environments. <br>
Mitigation: Install it only for data-analysis coaching needs, review crawler/key-simulation and Feishu templates before use, avoid private or login-protected targets, and remove or downgrade elevated scheduled-task examples. <br>
Risk: Generated examples may involve cookies, tokens, .env files, or external API calls. <br>
Mitigation: Do not paste real cookies or tokens into chat, keep .env files out of source control, and review generated code for credential handling before running it. <br>
Risk: The distillation workflow can propose changes to the skill's own method library. <br>
Mitigation: Require the documented pre-write review, inspect diffs after distillation, and keep self-updates limited to the skill directory. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/edwardwason/skills/data-prompt-coach) <br>
- [Publisher profile](https://clawhub.ai/user/edwardwason) <br>
- [Homepage](https://github.com/EdwardWason/data-prompt-coach) <br>
- [Method index](assets/INDEX.md) <br>
- [Skill digest](assets/DIGEST.md) <br>
- [Security compliance notes](references/audit/security-compliance.md) <br>
- [Examples](references/examples.md) <br>
- [Troubleshooting](references/troubleshooting.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown prompts, checklists, templates, and optional code or configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May generate files or skill-library updates only when the user explicitly approves the relevant workflow.] <br>

## Skill Version(s): <br>
3.4.4 (source: frontmatter and ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
