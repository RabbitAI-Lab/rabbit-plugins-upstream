## Description: <br>
This skill helps agents search, discover, browse, view details for, and install Huawei Cloud agent skills. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[changhui123456](https://clawhub.ai/user/changhui123456) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and agent users use this skill to find Huawei Cloud skills by keyword or category, inspect matching skill details, and receive installation guidance before using a more specific Huawei Cloud skill. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Installation mutates the local skill set and the workflow reports an install count to a remote Huawei Cloud endpoint. <br>
Mitigation: Review the selected skill, install command, and remote reporting step before execution; do not proceed in environments where local skill mutation or install reporting is not acceptable. <br>
Risk: Bundled reference files appear to describe a Huawei Cloud skill creator package rather than only the finder workflow. <br>
Mitigation: Treat the primary SKILL.md and search script as the operative finder evidence; do not follow creator, credential, live cloud call, or resource mutation guidance unless it is separately reviewed for the intended task. <br>
Risk: The security verdict is suspicious because the package combines finder behavior with mismatched credential and cloud-operation guidance. <br>
Mitigation: Review the package before installation and keep execution limited to search, discovery, detail review, and explicitly approved installation steps. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/changhui123456/skills/huawei-cloud-find-skills) <br>
- [Huawei Cloud skill finder script](scripts/search-skills.py) <br>
- [GitCode skill index](https://gitcode.com/api/v5/repos/2501_91318609/skills-for-index/contents/skills-index/index.json?ref=main) <br>
- [GitCode Chinese-English keyword map](https://gitcode.com/api/v5/repos/2501_91318609/skills-for-index/contents/skills-index/cn-en-map.json?ref=main) <br>
- [Huawei Cloud skills repository](https://github.com/huaweicloud/huaweicloud-skills) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with search results, skill detail links, and install command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Network access is required to fetch the skill index and optional skill details.] <br>

## Skill Version(s): <br>
1.0.14 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
