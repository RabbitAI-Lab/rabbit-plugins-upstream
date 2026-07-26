## Description: <br>
Baidu Baike Search lets an agent query Baidu Baike for encyclopedia entries by title or entry ID and return structured results, including support for homonym resolution. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ide-rea](https://clawhub.ai/user/ide-rea) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agents use this skill to look up Baidu Baike entries for people, places, concepts, events, and other nouns, including ambiguous terms that require selecting among homonymous entries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Lookup terms are sent to Baidu when the skill queries Baidu Baike. <br>
Mitigation: Avoid using the skill for confidential internal terms or sensitive user-provided queries. <br>
Risk: The skill requires a Baidu API key in BAIDU_API_KEY. <br>
Mitigation: Use a dedicated, revocable key and monitor quota or billing for unexpected usage. <br>
Risk: The command-line helper depends on the Python requests package and network access to Baidu. <br>
Mitigation: Confirm the runtime has the requests package installed and can reach the Baidu API before relying on the skill. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ide-rea/skills/baidu-baike-data) <br>
- [Baidu Baike](https://baike.baidu.com/) <br>
- [Baidu AppBuilder Baike API](https://appbuilder.baidu.com/v2/baike) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, API calls, Shell commands, Guidance] <br>
**Output Format:** [JSON returned by a command-line helper, with agent-facing Markdown guidance in the skill documentation] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returned entries may include lemma ID, title, description, URL, plain-text abstract, information cards, image albums, and a main image URL.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
