## Description: <br>
Weekday AI briefing - fetches top AI stories from Hacker News and dev.to, generates a 3-item curated briefing post in Sol's voice. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[amrree](https://clawhub.ai/user/amrree) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and content operators use this skill to generate a weekday AI news briefing from Hacker News and dev.to and publish it as a Jekyll post. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can run unattended on a weekday schedule and publish directly to a configured GitHub repository. <br>
Mitigation: Review the referenced pipeline before enabling launchd, and prefer a dry-run, staging branch, or manual approval step before publication. <br>
Risk: The workflow depends on a local MiniMax API key and local filesystem paths. <br>
Mitigation: Restrict access to the secret file, confirm the configured paths before first run, and rotate the API key if it may have been exposed. <br>
Risk: Security evidence reports incomplete permission disclosure for behavior that writes posts, commits changes, and pushes to GitHub. <br>
Mitigation: Confirm the requested permissions and repository access match the intended deployment before installation. <br>


## Reference(s): <br>
- [Sol Quick Hits on ClawHub](https://clawhub.ai/amrree/skills/sol-quick-hits) <br>
- [Referenced content pipeline](https://github.com/TheSolAI/sol-skills-bundle) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, files, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown Jekyll post files with repository commit and push actions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses MiniMax and local repository paths configured outside the submitted skill artifact.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
