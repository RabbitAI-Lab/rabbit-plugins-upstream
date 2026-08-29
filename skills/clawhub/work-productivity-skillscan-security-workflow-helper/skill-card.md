## Description:

Helps agent users and skill maintainers create practical SkillScan-style workflows for bug fixing, hardening, reliability review, and adjacent skill development.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyro-ma](https://clawhub.ai/user/kyro-ma)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, AI-agent users, skill authors, maintainers, and teams use this skill to turn SkillScan-style security and reliability needs into actionable plans, checklists, analysis, code changes, or workflow artifacts. It is intended for local-hardware-friendly productivity and review support.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad trigger wording may cause the skill to activate for generic productivity, security, or bug-fix requests.

Mitigation: Installers can narrow activation to explicit SkillScan or security-workflow requests.

Risk: Generated workflow or code guidance could be incomplete for a specific repository or operational environment.

Mitigation: Review outputs against the stated success criteria and run the relevant local checks before deployment.

## Reference(s):

- [Requirement Plan](references/requirement-plan.md)
- [Skill Vetter demand signal](https://clawhub.ai/skills/skill-vetter)
- [SkillScan demand signal](https://clawhub.ai/skills/skillscan)
- [AdMapix demand signal](https://clawhub.ai/skills/admapix)
- [PollyReach demand signal](https://clawhub.ai/skills/pollyreach)
- [Ask HN: Do you still do pair programming in this agentic age?](https://news.ycombinator.com/item?id=49461326)
- [Encoding Myself into the System](https://news.ycombinator.com/item?id=49457457)
- [Ask HN: How does manual QA fit into your process?](https://news.ycombinator.com/item?id=49462397)
- [Ask HN: Should we disclose AI use in our work?](https://news.ycombinator.com/item?id=49469914)
- [Another Webpage Screenshot and OG Image Generation API](https://news.ycombinator.com/item?id=49464305)
- [Fixing Status Updates - Our Manifesto](https://news.ycombinator.com/item?id=49462264)
- [[BETA] refactor(deep-capture): expose a library-first session API and thin the CLI](https://github.com/h8rt3rmin8r/fragcap/issues/252)
- [Run and diagnose the first local-model synthetic golden path](https://github.com/BeaudanBrown/pi-harness/issues/35)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown, code snippets, shell commands, checklists, and concise workflow guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include assumptions, validation notes, remaining risks, and next steps when useful.]

## Skill Version(s):

0.20260828.40337 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
