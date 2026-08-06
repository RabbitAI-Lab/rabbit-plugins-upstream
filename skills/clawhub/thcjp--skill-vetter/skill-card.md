## Description: <br>
Skill Vetter guides agents through source checks, mandatory code review, permission scoping, risk classification, and structured report generation before installing a skill. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to vet agent skills before installation by checking source trust, reviewing files for red flags, assessing requested permissions, and producing an install recommendation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can inspect files, write reports, run shell commands, and contact external APIs while reviewing other skills. <br>
Mitigation: Review before installing and run it in a sandbox or limited workspace with only the files, commands, and network/API access required for the review. <br>
Risk: The skill may involve API keys or tokens for external lookups. <br>
Mitigation: Do not provide keys or tokens unless the destination and purpose are clear; use scoped environment variables and avoid sensitive credentials. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/skill-vetter) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown or plain-text review report with occasional shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include source metadata, red flags, permission summaries, risk levels, and install recommendations.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata; artifact frontmatter lists 1.0.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
