## Description: <br>
Baidu Baike Search queries Baidu Baike for standardized encyclopedia explanations of nouns such as objects, people, places, concepts, and events. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[baiduqianfangroup](https://clawhub.ai/user/baiduqianfangroup) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to look up Baidu Baike lemma lists and lemma content for objective nouns through Baidu's API when encyclopedia context is needed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Lookup terms are sent to Baidu's service and may expose secrets, confidential project names, private identifiers, or sensitive personal data. <br>
Mitigation: Use the skill only when disclosure of the lookup terms to Baidu is acceptable, and avoid submitting sensitive or confidential terms. <br>
Risk: The skill requires a Baidu API key in the runtime environment. <br>
Mitigation: Store BAIDU_API_KEY as a secret, scope and rotate it according to local policy, and avoid writing it into prompts, logs, or committed files. <br>


## Reference(s): <br>
- [Baidu Baike](https://baike.baidu.com/) <br>
- [ClawHub Skill Page](https://clawhub.ai/baiduqianfangroup/skills/baidu-baike) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Guidance] <br>
**Output Format:** [JSON API responses with markdown usage guidance and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl and a BAIDU_API_KEY environment variable.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
