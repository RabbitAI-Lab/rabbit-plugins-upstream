## Description: <br>
TRPG Abbreviation Wrap normalizes English abbreviations in Chinese TRPG rules, scenarios, and character sheets into Chinese full-term-plus-abbreviation form for player and game master readability. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ice26985850](https://clawhub.ai/user/ice26985850) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, writers, and game masters use this skill before release to normalize TRPG terminology in Markdown, text, and Excel character sheet content. It is intended for project-specific abbreviation cleanup where the agent confirms the target files and mapping before making changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may change local .md, .txt, and .xlsx content using an incorrect project-specific abbreviation mapping. <br>
Mitigation: Confirm the target files and abbreviation-to-full-term mapping before applying edits. <br>
Risk: Repeated or poorly scoped replacements could introduce double-wrapped abbreviations or leave bare abbreviations behind. <br>
Mitigation: Use the skill's idempotency checks, rerun validation after changes, and verify that a repeat dry run reports no further changes. <br>
Risk: Skipped old, backup, v1, draft, or internal briefing files may still contain unnormalized abbreviations. <br>
Mitigation: Report skipped files to the user and process them only when explicitly requested. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ice26985850/skills/trpg-abbr-wrap) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with regex rules, Python validation snippets, and delivery checklist items] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide an agent to edit local .md, .txt, and .xlsx files after confirming the abbreviation mapping and target files.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
