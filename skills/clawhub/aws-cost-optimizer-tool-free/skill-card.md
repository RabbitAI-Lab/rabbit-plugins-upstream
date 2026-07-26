## Description: <br>
Provides monthly AWS cost summaries, service and region breakdowns, idle-resource checks, and basic savings recommendations for individual developers and startup teams. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and startup teams use this skill to inspect AWS spending, identify idle resources, and generate basic cost-saving guidance for a single AWS account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests AWS billing and resource access, which may expose account cost and infrastructure information. <br>
Mitigation: Use a dedicated read-only AWS profile or IAM user and avoid production administrator credentials. <br>
Risk: The skill advertises read, write, and exec tool use, including report export behavior that can write local files. <br>
Mitigation: Review commands before execution and choose explicit report output paths. <br>


## Reference(s): <br>
- [ClawHub Skill Listing](https://clawhub.ai/thcjp/skills/aws-cost-optimizer-tool-free) <br>
- [Skill Homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline bash commands and structured cost report examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May export CSV or JSON cost reports when an explicit output path is provided.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
