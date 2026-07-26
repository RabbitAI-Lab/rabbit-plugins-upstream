## Description: <br>
Search, install, and create OpenClaw skills from built-in, local, or GitHub sources with intelligent matching and ranking. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[legionspace-hackathon](https://clawhub.ai/user/legionspace-hackathon) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to find relevant skills, inspect known and local skill options, install matching GitHub-hosted skills, or scaffold a new skill when no good match exists. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selecting a GitHub result can install third-party skill code into the local skills directory. <br>
Mitigation: Prefer trusted repositories, inspect the repository and target path before installation, and keep a removal path for installed skills. <br>
Risk: The release security summary reports too little review or warning before persistent installation of third-party code. <br>
Mitigation: Review matched GitHub results and their source before confirming installation, especially in shared or production workspaces. <br>


## Reference(s): <br>
- [ClawHub Skillstore Release Page](https://clawhub.ai/legionspace-hackathon/skills/skillstore) <br>
- [SKILL.md](artifact/SKILL.md) <br>
- [README.md](artifact/README.md) <br>
- [Skill Development Guidelines](artifact/guidelines.md) <br>
- [GitHub Repository Search API](https://api.github.com/search/repositories) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Terminal text with ranked results, Markdown skill templates, JavaScript code, JSON configuration, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May persist installed or generated skill files in the local skills directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
