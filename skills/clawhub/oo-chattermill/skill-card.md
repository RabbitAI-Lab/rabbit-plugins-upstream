## Description: <br>
Chattermill (chattermill.com). Use this skill for ANY Chattermill request -- reading, creating, updating, and deleting data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to work with Chattermill projects, responses, metrics, tags, themes, attributes, categories, data sources, data types, and custom segments through an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create or update Chattermill responses through an OOMOL-connected account. <br>
Mitigation: Confirm the exact payload and expected effect with the user before running any write action. <br>
Risk: The skill can permanently delete Chattermill responses. <br>
Mitigation: Require explicit approval for the specific target response before running any destructive action. <br>
Risk: Connected account access may expose Chattermill project and response data. <br>
Mitigation: Install and use the skill only when the connected OOMOL account is intended to access the relevant Chattermill workspace. <br>


## Reference(s): <br>
- [Chattermill homepage](https://chattermill.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-chattermill) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown guidance with bash commands and JSON CLI responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Live connector schema inspection is used before action execution; write and destructive actions require confirmation.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
