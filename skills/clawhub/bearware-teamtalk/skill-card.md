## Description: <br>
Complete knowledge base for BearWare.dk's TeamTalk 5 Conferencing System. Use when working with TeamTalk audio/video conferencing, the TeamTalk 5 SDK (C-API, .NET, Java, Python, Rust), TeamTalk server administration, TeamTalk client development, building TeamTalk from source, or any TeamTalk-related task including cloning, building, detecting installed SDK, API usage, and configuring servers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[romeohorvath](https://clawhub.ai/user/romeohorvath) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to work with BearWare TeamTalk 5 client and server development, SDK setup, source builds, API usage, language bindings, and server configuration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The setup path can fetch source code and run privileged system-modifying build commands. <br>
Mitigation: Review the shell scripts before running them, verify the repository and branch, prefer Docker or manual dependency installation, and avoid sudo unless the user accepts that level of authority. <br>
Risk: Automated builds may modify local dependencies and build artifacts as part of SDK setup. <br>
Mitigation: Run setup in an isolated workspace or container when possible, and inspect the selected build target before execution. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/romeohorvath/skills/bearware-teamtalk) <br>
- [TeamTalk 5 SDK API Reference](references/api_reference.md) <br>
- [TeamTalk 5 SDK ChangeLog](references/changelog.md) <br>
- [TeamTalk 5 Download & Build Links](references/download_links.md) <br>
- [TeamTalk5 GitHub Repository](https://github.com/BearWare/TeamTalk5) <br>
- [TeamTalk5 Releases](https://github.com/BearWare/TeamTalk5/releases) <br>
- [TeamTalk 5 C-API Docs](https://bearware.dk/teamtalksdk/v5.22a/docs/C-API/) <br>
- [TeamTalk 5 .NET Docs](https://bearware.dk/teamtalksdk/v5.22a/docs/NET/) <br>
- [TeamTalk 5 Java Docs](https://bearware.dk/teamtalksdk/v5.22a/docs/Java/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline code and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes optional helper scripts for SDK detection, setup, and source builds.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
