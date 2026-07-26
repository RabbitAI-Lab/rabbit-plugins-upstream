## Description: <br>
Search GIF providers with CLI/TUI, download results, and extract stills/sheets. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[steipete](https://clawhub.ai/user/steipete) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and external users use Gifgrep to search Tenor or Giphy, preview results, download selected GIFs, and extract still frames or contact sheets for review and sharing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Installation depends on a Homebrew tap or Go module source, and the Go install path uses @latest. <br>
Mitigation: Verify that the publisher and install source are trusted before installation; pin or review the installed version when reproducibility matters. <br>
Risk: Giphy and Tenor provider keys may be supplied through environment variables. <br>
Mitigation: Provide API keys only when needed, keep them out of shared prompts and logs, and rotate them if exposed. <br>
Risk: Download commands create files in the user's Downloads folder. <br>
Mitigation: Review selected GIFs and generated still or sheet files before sharing or committing them. <br>


## Reference(s): <br>
- [Gifgrep Homepage](https://gifgrep.com) <br>
- [ClawHub Skill Page](https://clawhub.ai/steipete/skills/gifgrep) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance] <br>
**Output Format:** [Markdown with inline shell commands, environment variables, and command-output guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference JSON output fields, downloaded GIF files, still images, and PNG contact sheets.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
