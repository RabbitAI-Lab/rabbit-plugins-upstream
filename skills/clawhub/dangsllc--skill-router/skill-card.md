## Description: <br>
Reads one or more document manifests and the rote-compliance-toolkit skill catalog to produce an Analysis Plan that recommends candidate skills for discovered documents and surfaces unmatched documents as toolkit coverage gaps. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dangsllc](https://clawhub.ai/user/dangsllc) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Compliance operators and developers use this skill after document discovery to match discovered documents to candidate rote-compliance-toolkit skills and identify toolkit coverage gaps before deciding what to run next. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads user-provided manifests and frontmatter from the target skills directory. <br>
Mitigation: Confirm the supplied manifests and skills directory are appropriate to share with the agent before installing or using the skill. <br>
Risk: Routing recommendations can be incomplete or mismatched when manifest classifications or skill frontmatter are ambiguous. <br>
Mitigation: Review the generated Analysis Plan before running downstream compliance skills and treat reported coverage gaps as operator decisions. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/dangsllc/skills/skill-router) <br>
- [Rote Compliance Skills](https://github.com/Rote-Compliance/rote-compliance-skills) <br>
- [Dang's Solutions](https://dangssolutions.com) <br>
- [Rote](https://rotecompliance.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, guidance] <br>
**Output Format:** [Markdown analysis plan plus structured JSON] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only routing plan; does not execute recommended skills.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
