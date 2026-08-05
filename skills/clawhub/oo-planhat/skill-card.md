## Description: <br>
Planhat (planhat.com). Use this skill for ANY Planhat request - reading, creating, and updating data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to operate Planhat through an OOMOL-connected account, including reading, listing, creating, and updating companies and end users. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Write actions can change business and customer records in Planhat. <br>
Mitigation: Confirm the exact target, payload, and expected effect with the user before running create or update actions. <br>
Risk: Incorrect payload fields could create or update the wrong Planhat data. <br>
Mitigation: Fetch the live connector schema for the selected action before constructing any payload. <br>
Risk: The skill uses the user's OOMOL-connected Planhat account. <br>
Mitigation: Install and use it only when the user intends Codex to access that connected Planhat account. <br>


## Reference(s): <br>
- [Planhat homepage](https://www.planhat.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-planhat) <br>
- [Publisher profile](https://clawhub.ai/user/oomol) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses the oo CLI and live connector schemas before constructing Planhat action payloads.] <br>

## Skill Version(s): <br>
1.0.1 (source: release evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
