## Description: <br>
Detects aggressive interactions in livestock and poultry from continuous barn videos, including fighting, biting, chasing, and butting, and outputs behavior type, intensity level, and alert level. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and farm operations teams use this skill to submit barn image or video inputs for livestock and poultry aggression screening, including fight, bite, chase, and butting detection. It returns structured behavior observations, event timing, involved locations, intensity levels, warning levels, and report links. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Barn images or videos and identity-linked report requests are sent to lifeemergence.com services for cloud analysis. <br>
Mitigation: Use the skill only with media approved for third-party cloud processing, and avoid submitting sensitive footage unless the publisher and service terms are acceptable. <br>
Risk: The skill may silently create or reuse a local default identity and associate analysis history with that identity. <br>
Mitigation: Review identity handling before deployment and run it in a controlled workspace where generated identities and report access are expected. <br>
Risk: Service tokens may be stored in the workspace database. <br>
Mitigation: Limit workspace access, treat the local database as sensitive, and remove stored credentials when the skill is no longer needed. <br>
Risk: The remote service can return billing or recharge instructions when use is rejected for payment reasons. <br>
Mitigation: Confirm commercial and billing expectations with the publisher before operational use. <br>


## Reference(s): <br>
- [API documentation](artifact/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-aggressive-behavior-detection-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and JSON-like structured analysis text, with optional saved output files and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports local file paths or media URLs, history-list output, and basic, standard, or json detail modes; documented media limit is 10 MB.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release evidence; artifact frontmatter reports 1.0.5) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
