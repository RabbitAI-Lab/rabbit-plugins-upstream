## Description: <br>
Searches, discovers, browses, and guides installation of Huawei Cloud agent skills by keyword or category. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud operators use this skill to find Huawei Cloud agent skills for services such as ECS, OBS, RDS, and VPC, inspect matching skill documentation, and receive supported install commands. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can send an install-count request and install additional skills, not only search. <br>
Mitigation: Review and approve network calls and each downstream skill before execution. <br>
Risk: Search and detail lookup require outbound requests to GitCode and GitHub endpoints. <br>
Mitigation: Run the skill only where those network requests are acceptable and inspect results before following install commands. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/erickeyhu-hug/skills/huawei-cloud-find-skills) <br>
- [Huawei Cloud Skills Repository](https://github.com/huaweicloud/huaweicloud-skills) <br>
- [GitCode Skill Index API](https://gitcode.com/api/v5/repos/2501_91318609/skills-for-index/contents/skills-index/index.json?ref=main) <br>
- [GitCode Chinese-English Keyword Map API](https://gitcode.com/api/v5/repos/2501_91318609/skills-for-index/contents/skills-index/cn-en-map.json?ref=main) <br>
- [Search Script](artifact/scripts/search-skills.py) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with command snippets and script-produced text results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses keyword and optional category inputs; network access is required for remote index and detail lookup.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
