## Description: <br>
Architects, debugs, secures, and cost-optimizes AWS infrastructure across EC2, Lambda, RDS, VPC, IAM, ECS, CloudFront, AWS accounts, billing, reliability, and CLI workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and cloud engineers use this skill to plan, review, debug, secure, and cost-optimize AWS infrastructure and AWS CLI workflows. It is suited for service selection, account audits, IAM and network troubleshooting, incident diagnosis, infrastructure-as-code guidance, and production readiness checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can persist AWS inventory, account IDs, resource names, cost history, runbooks, and policy notes under ~/Clawic/data/. <br>
Mitigation: Keep the local Clawic data directory protected and treat infrastructure metadata as sensitive operational information. <br>
Risk: Real AWS secret keys, session tokens, passwords, private keys, or webhook tokens could be accidentally added to local notes. <br>
Mitigation: Store only credential pointers such as profile names, SSM paths, keychain references, or environment-variable names, and remove raw secret values from any saved text. <br>
Risk: AWS CLI guidance can include commands that inspect or modify live cloud resources. <br>
Mitigation: Review commands before execution, use the intended AWS profile and region, and require explicit confirmation for destructive or state-changing actions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ivangdavila/skills/aws) <br>
- [Clawic AWS skill homepage](https://clawic.com/skills/aws) <br>
- [AWS CLI requirement](https://formulae.brew.sh/formula/awscli) <br>
- [AWS skill definition](artifact/SKILL.md) <br>
- [AWS CLI toolkit](artifact/commands.md) <br>
- [AWS security guide](artifact/security.md) <br>
- [AWS cost control guide](artifact/costs.md) <br>
- [AWS production guide](artifact/production.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline commands, configuration examples, checklists, and infrastructure recommendations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference local Clawic memory files under ~/Clawic/data/ for user-declared AWS preferences, inventory notes, cost history, runbooks, and policy notes.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
