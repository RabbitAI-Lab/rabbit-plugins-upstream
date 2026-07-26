## Description: <br>
Download Instagram profile media including reels, photos, and carousel images via a sessionid cookie, Apify dataset fallback, or an interactive setup wizard. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cripterhack](https://clawhub.ai/user/cripterhack) <br>

### License/Terms of Use: <br>
GPL-2.0-only <br>


## Use Case: <br>
External users and developers use this skill to have an agent configure or run the Instagram downloader CLI for profiles they can access. The skill helps choose sessionid, setup-wizard, or Apify fallback modes and emits the commands and guidance needed to download media into local files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The tool asks for sensitive Instagram session access. <br>
Mitigation: Treat the sessionid like a password, avoid passing it on command lines or in shared logs, and consider using a separate low-privilege Instagram account. <br>
Risk: The setup flow can read browser cookies to obtain an Instagram session. <br>
Mitigation: Prefer manual token entry over Chrome cookie extraction when possible and review the setup path before running it. <br>
Risk: Installers and downloader commands execute local scripts that access network services and write files. <br>
Mitigation: Review installer targets and downloader options before execution, then run only in an environment where local media output and configuration writes are acceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cripterhack/skills/igd) <br>
- [Publisher profile](https://clawhub.ai/user/cripterhack) <br>
- [instagrapi](https://github.com/subzeroid/instagrapi) <br>
- [skills.sh listing](https://skills.sh/cripterhack/ig-downloader-skill) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, CLI flags, and file paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The guided CLI workflow may create downloaded media files and a local Instagram session configuration file.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact version signals differ: SKILL.md reports 2.2.0 and pyproject.toml/CHANGELOG.md report 2.3.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
