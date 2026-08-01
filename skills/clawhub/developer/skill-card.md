## Description: <br>
Helps an agent handle everyday software development work, from finding where a change belongs through implementation, testing, review, release, and incident follow-up. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering agents use this skill to work inside existing codebases: orienting in unfamiliar repos, fixing bugs, planning changes, testing, reviewing, shipping, and handling operational follow-up. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores local development notes under ~/Clawic/data/, including repo commands, conventions, estimates, releases, incidents, contacts, and project status. <br>
Mitigation: Review those local files periodically on shared or synced machines and keep secrets, tokens, private customer data, and sensitive incident details out of local notes. <br>
Risk: Development workflows can involve destructive changes such as data fixes, backfills, migrations, history rewrites, or deletions. <br>
Mitigation: Use the skill's disclosed guardrail of presenting blast radius and requiring explicit confirmation when risk_confirm is true. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ivangdavila/skills/developer) <br>
- [Clawic Developer skill](https://clawic.com/skills/developer) <br>
- [Skill definition](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown, code snippets, shell commands, and concise implementation guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May update disclosed local notes under ~/Clawic/data/ when durable development knowledge is produced.] <br>

## Skill Version(s): <br>
1.0.2 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
