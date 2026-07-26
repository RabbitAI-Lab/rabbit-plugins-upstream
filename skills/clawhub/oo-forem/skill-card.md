## Description: <br>
Forem (forem.com). Use this skill for ANY Forem request - reading, creating, and updating data. Whenever a task involves Forem, use this skill instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to read Forem content and manage authenticated Forem articles through the OOMOL-connected Forem connector. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Write actions can create or update Forem content through the connected account. <br>
Mitigation: Review the exact JSON payload and intended effect before approving article creation or updates. <br>
Risk: The skill depends on OOMOL as an intermediary for Forem account access. <br>
Mitigation: Install and use it only when the user is comfortable connecting Forem through OOMOL. <br>


## Reference(s): <br>
- [Forem homepage](https://www.forem.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-forem) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call the OOMOL Forem connector and return JSON data from Forem actions.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
