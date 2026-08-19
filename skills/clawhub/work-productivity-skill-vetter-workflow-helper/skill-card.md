## Description:

Helps agent users, skill authors, maintainers, and teams create practical workflow aids for vetting skills, fixing bugs, hardening setup and safety, improving reliability, or building adjacent skills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyro-ma](https://clawhub.ai/user/kyro-ma)

### License/Terms of Use:

MIT-0

## Use Case:

Agent users, skill authors, maintainers, and teams use this skill to turn skill-vetting and reliability needs into concise plans, checklists, analyses, implementation support, and verification notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad activation wording may route unrelated security, GitHub, bug-fix, or workflow requests to this helper.

Mitigation: Prefer explicit invocation or tighten trigger wording before deployment where predictable routing matters.

Risk: Generated workflow, code, shell command, or configuration guidance may be incorrect or incomplete for a user's environment.

Mitigation: Review proposed changes, run local validation, and apply the skill's verification step before deploying changes.

## Reference(s):

- [Requirement Plan](artifact/references/requirement-plan.md)
- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/work-productivity-skill-vetter-workflow-helper)
- [Popular ClawHub skill demand: self-improving-agent](https://clawhub.ai/skills/self-improving-agent)
- [Popular ClawHub skill demand: Skill Vetter](https://clawhub.ai/skills/skill-vetter)
- [Popular ClawHub skill demand: Github](https://clawhub.ai/skills/github)
- [Popular ClawHub skill demand: SkillScan](https://clawhub.ai/skills/skillscan)
- [Ask HN: How would you market this service?](https://news.ycombinator.com/item?id=49316403)
- [OpenAI updates its Privacy Policy to include ads](https://news.ycombinator.com/item?id=49308738)
- [Why is the GitHub trending page weirdly excluding DeepSeek projects?](https://news.ycombinator.com/item?id=49323677)
- [Ask HN: Anyone got a deauthentication attack script?](https://news.ycombinator.com/item?id=49314649)
- [I've build a source of real fake data](https://news.ycombinator.com/item?id=49321676)
- [GitHub issue: ci: add an OpenSSF Scorecard workflow](https://github.com/Riptide-Labs/deltav-proto-contracts/issues/49)
- [GitHub issue: [security] Update Chromium pin](https://github.com/JackZeng/LongView-Chromium/issues/11)
- [GitHub issue: Session start welcome text](https://github.com/operum-ai/operum/issues/419)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown text, with code, shell commands, configuration snippets, or checklists when the request calls for them]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are tailored to the user's immediate context and include assumptions, limits, validation notes, and next steps when helpful.]

## Skill Version(s):

0.20260817.40422 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
