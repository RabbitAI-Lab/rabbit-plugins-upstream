## Description: <br>
aws-infra helps agents run read-only AWS CLI infrastructure checks across resource inventory, health, security, cost, and change-tracking workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operations teams, and cloud administrators use this skill to inspect AWS resources, review security posture and costs, and troubleshoot infrastructure state through read-only AWS CLI queries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can cause an agent to run AWS CLI commands and write local report files. <br>
Mitigation: Install only if this execution and file-writing behavior is acceptable for the target environment, and review exported AWS results before committing or sharing them. <br>
Risk: AWS credential and profile handling is under-disclosed for a skill that performs broad AWS infrastructure inspection. <br>
Mitigation: Use AWS SSO or short-lived role credentials, avoid pasting secrets into commands or shared terminals, and pass explicit --profile and --region flags where possible. <br>


## Reference(s): <br>
- [ClawHub aws-infra Skill Page](https://clawhub.ai/thcjp/skills/aws-infra) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline AWS CLI commands and optional table, JSON, text, or file outputs.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write local report files and depends on caller-provided AWS credentials or profiles, target regions, and AWS read-only permissions.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
