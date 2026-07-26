## Description: <br>
Writes user-supplied text, links, and images into an Obsidian daily note with timestamped, newest-first formatting and first-use vault setup. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hongquanxu1993](https://clawhub.ai/user/hongquanxu1993) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Individuals and teams use this skill when they explicitly ask an agent to save research notes, task summaries, ideas, meeting takeaways, URLs, or images into an Obsidian daily note. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Saved notes, attachments, and fetched URL titles can persist locally and may sync through the user's Obsidian or backup setup. <br>
Mitigation: Only invoke the skill for content the user wants saved; avoid secrets, regulated data, private screenshots, and sensitive URLs unless local persistence and sync behavior are acceptable. <br>
Risk: A mistaken vault path or daily notes subdirectory can write entries to an unintended local location. <br>
Mitigation: Confirm the vault path and daily notes subdirectory during first-use setup before saving entries. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Configuration, Guidance] <br>
**Output Format:** [Markdown note entries plus brief text confirmation] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes to local Obsidian daily note files and may save image attachments when explicitly requested.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
