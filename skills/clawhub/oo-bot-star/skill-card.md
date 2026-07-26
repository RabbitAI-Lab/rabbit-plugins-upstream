## Description: <br>
BotStar helps an agent read, create, update, publish, and delete BotStar bots, bot attributes, CMS content, and audience user attributes through the OOMOL BotStar connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and BotStar operators use this skill to inspect and manage BotStar bots, CMS entities, CMS items, bot attributes, and audience user attributes from an agent workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can change live BotStar bots, CMS content, bot attributes, and audience user attributes. <br>
Mitigation: Review the exact payload and expected effect with the user before approving write, publish, update, or delete actions. <br>
Risk: The skill relies on OOMOL to broker the BotStar account connection. <br>
Mitigation: Install and use it only when the publisher and connected BotStar account are trusted for the intended workspace. <br>


## Reference(s): <br>
- [BotStar homepage](https://botstar.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires live schema inspection before action payloads; write and destructive actions require user confirmation.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
