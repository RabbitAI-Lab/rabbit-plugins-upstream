## Description: <br>
Helps agent users, skill authors, maintainers, and teams create SkillScan-style security, reliability, and workflow artifacts such as plans, checklists, analyses, and implementation guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External agent users, skill authors, maintainers, and teams use this skill to turn security, reliability, bug-fix, setup-hardening, or adjacent-skill requests into practical local workflows, artifacts, checklists, analysis, code changes, or decision support. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill allows implicit invocation and uses broad trigger terms, so ordinary security, productivity, or bug-fix requests may be routed through it unintentionally. <br>
Mitigation: Review activation behavior before installation and prefer explicit invocation or narrower trigger phrases. <br>
Risk: Generated workflow or implementation guidance may be incomplete or misleading for the user's environment. <br>
Mitigation: Check outputs against the stated success criteria, review proposed code or commands before use, and keep assumptions and required inputs visible. <br>


## Reference(s): <br>
- [Requirement Plan](references/requirement-plan.md) <br>
- [ClawHub skill page](https://clawhub.ai/kyro-ma/skills/work-productivity-skillscan-security-workflow-helper-230850) <br>
- [Popular ClawHub skill demand: self-improving agent](https://clawhub.ai/skills/self-improving-agent) <br>
- [Popular ClawHub skill demand: Skill Vetter](https://clawhub.ai/skills/skill-vetter) <br>
- [Popular ClawHub skill demand: SkillScan](https://clawhub.ai/skills/skillscan) <br>
- [Popular ClawHub skill demand: AdMapix](https://clawhub.ai/skills/admapix) <br>
- [Popular ClawHub skill demand: PollyReach](https://clawhub.ai/skills/pollyreach) <br>
- [Ask HN: Can anyone explain this Gsearch rabbit-hole?](https://news.ycombinator.com/item?id=48878919) <br>
- [Tell HN: Staged NPM publishing is awful](https://news.ycombinator.com/item?id=48893354) <br>
- [A/B Test results: Trying different homepage heroes got us 2.6x sign-ups](https://news.ycombinator.com/item?id=48894437) <br>
- [Autonomous: Daily PR Audit Reporter](https://github.com/extropolis/claudia/issues/109) <br>
- [Add speculative execution barrier for Spectre mitigation](https://github.com/m-novotny/memguard-rs/issues/7) <br>
- [HGC QC: cap the module at computation](https://github.com/bigbio/hvantk/issues/205) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with optional code, shell-command, checklist, and configuration blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include assumptions, validation notes, remaining risks, and follow-up work when useful.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
