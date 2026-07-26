## Description: <br>
Operates Get 笔记 (biji.com) through the OOMOL getnote connector for reading, creating, updating, sharing, and deleting notes and related knowledge-base data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to manage Get 笔记 notes, tags, sharing, and knowledge bases from an agent through the OOMOL oo CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Write or destructive actions can change or delete Get 笔记 data. <br>
Mitigation: Confirm the target note, knowledge base, tags, payload, and expected effect before approving write or destructive actions. <br>
Risk: Installing or authenticating the OOMOL oo CLI affects access to the user's connected account. <br>
Mitigation: Install or authenticate the OOMOL oo CLI only from the documented source and only when an auth or connection error requires it. <br>


## Reference(s): <br>
- [Get 笔记 homepage](https://www.biji.com/) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-getnote) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call the OOMOL oo CLI and return connector JSON responses when actions are executed.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
