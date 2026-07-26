## Description: <br>
Chart Free helps agents generate local PNG bar and line charts from inline labels and values using Python and matplotlib. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and other agent users can use this skill to create simple local PNG charts for reports, slides, and decision documents from inline data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks users to configure a generic API key even though the charting workflow is described as local and offline. <br>
Mitigation: Avoid placing sensitive API keys in the environment for this skill unless the publisher clarifies why they are needed and what service will use them. <br>
Risk: The release has a suspicious security verdict from ClawHub's scan because of the credential guidance ambiguity. <br>
Mitigation: Review the skill before installing, confirm that chart generation stays local, and run only the commands needed for the chart workflow. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/chart-free) <br>
- [SkillHub homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance, Files] <br>
**Output Format:** [Markdown guidance with bash snippets; generated chart artifacts are PNG files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports bar and line charts from inline labels and values; output images are written locally.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence; artifact frontmatter lists 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
