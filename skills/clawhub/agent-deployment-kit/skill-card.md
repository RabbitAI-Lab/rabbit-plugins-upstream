## Description: <br>
Replicate one agent across N clients without drift -- one context source, a generator that refuses unknowns. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alexbloch-ia](https://clawhub.ai/user/alexbloch-ia) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to design repeatable agent deployment kits for multiple clients, keeping client context centralized while requiring generator guards for placeholders, sentinels, paths, permissions, backups, and retention. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users could treat the release as a ready-made deployment tool and skip implementing or testing required guards. <br>
Mitigation: Before using the pattern with real clients, verify that the generator enforces the described path, marker, sentinel, permission, backup, and retention checks. <br>
Risk: Rendered agents may process personal data or expose secrets if credentials, backups, or retention jobs are mishandled. <br>
Mitigation: Keep real credentials out of the repo, transfer secrets out of band, account for backups as sensitive data, and require an executable retention job before deployment. <br>


## Reference(s): <br>
- [OpenClaw](https://openclaw.ai) <br>
- [ClawHub Skill Page](https://clawhub.ai/alexbloch-ia/skills/agent-deployment-kit) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with JSON examples, shell snippets, and code snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces a method and validation checklist for building local deployment tooling; it does not ship an executable generator.] <br>

## Skill Version(s): <br>
1.1.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
