## Description: <br>
Weekend deep dive - long-form 600-800 word researched piece on one AI topic, with HN and dev.to sourcing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[amrree](https://clawhub.ai/user/amrree) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and content publishers use this skill to generate and publish a researched weekly AI article for a Jekyll site. It is intended for automated long-form blog content that draws on Hacker News and dev.to discussion sources. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill schedules unattended public publishing and pushes changes to GitHub without clear review controls. <br>
Mitigation: Use it only for a Jekyll site you own, review the external script before enabling automation, and prefer a dedicated branch or pull request workflow. <br>
Risk: The skill depends on repository access and a MiniMax API key for automated content generation. <br>
Mitigation: Restrict GitHub credentials to the intended repository and keep the MiniMax key in a protected secret file. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/amrree/skills/sol-weekend-deep-dive) <br>
- [sol-skills-bundle source reference](https://github.com/TheSolAI/sol-skills-bundle) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown article content with Jekyll post output and operational setup guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Targets a 600-800 word article and writes a dated Jekyll post when configured.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
