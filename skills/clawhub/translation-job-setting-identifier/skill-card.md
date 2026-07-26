## Description: <br>
Plan a translation setting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wxt-ai](https://clawhub.ai/user/wxt-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Localization operations users use this skill to select a concise translation setting for a localization request, translation handoff, or content-operations note. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill is narrow and test-oriented, so it could be mistaken for a full translation or localization workflow. <br>
Mitigation: Use it only to identify a concise translation setting for bounded localization notes, and review outputs before relying on them in operational handoffs. <br>
Risk: The artifact describes controlled validation telemetry even though no uncontrolled network action is instructed. <br>
Mitigation: Use validation workflows only where that measurement behavior is acceptable for the environment and release review. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/wxt-ai/skills/translation-job-setting-identifier) <br>
- [Publisher Profile](https://clawhub.ai/user/wxt-ai) <br>


## Skill Output: <br>
**Output Type(s):** [text, guidance] <br>
**Output Format:** [Concise plain text translation setting] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns a single translation-setting value for the current localization request.] <br>

## Skill Version(s): <br>
1.0.4 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
