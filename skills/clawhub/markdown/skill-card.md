## Description: <br>
Markdown helps agents write, fix, lint, convert, and safely render Markdown across GitHub, MDX, Pandoc, documentation sites, and chat platforms. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, documentation maintainers, and agents use this skill to repair Markdown rendering bugs, produce README and docs content, convert Markdown to or from other formats, and choose syntax that matches the target renderer. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill automatically saves and reuses documentation, project, and contact details in shared local files without per-use permission. <br>
Mitigation: Install only if local long-term memory is acceptable, and review or disable writes to ~/Clawic/data/markdown/, ~/Clawic/data/projects/, and ~/Clawic/data/contacts/ when project names, contacts, repository paths, or build decisions are sensitive. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/ivangdavila/skills/markdown) <br>
- [Skill homepage](https://clawic.com/skills/markdown) <br>
- [Skill definition](artifact/SKILL.md) <br>
- [Markdown security guidance](artifact/security.md) <br>
- [Markdown conversion guidance](artifact/conversion.md) <br>
- [Markdown flavor guidance](artifact/flavors.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or plain text responses with snippets, diffs, commands, and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Target-renderer-specific; may include local memory updates for durable documentation preferences, recipes, and project context.] <br>

## Skill Version(s): <br>
1.0.2 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
