## Description: <br>
Use at the start of any OpenCLI session as the top-level map of what opencli can do, how to discover adapters, which flags and output formats are universal, and which specialized skill to load next. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chaoyang78](https://clawhub.ai/user/chaoyang78) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Agents and developers use this skill to orient an OpenCLI session, discover available site adapters and universal flags, and decide which specialized OpenCLI skill to load next. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill grants agents broad OpenCLI command guidance, including workflows that can interact with local tools and authenticated browser sessions. <br>
Mitigation: Install only when agents are intended to use OpenCLI, and review proposed commands before execution. <br>
Risk: Commands that bind to logged-in browser tabs or capture authenticated requests can affect active web sessions. <br>
Mitigation: Use deliberate, scoped browser sessions and confirm the target tab or site before binding or capture workflows. <br>
Risk: Plugin installation from git and external CLI registration can change the local command environment. <br>
Mitigation: Use trusted plugin repositories and binaries, and verify installed tools before allowing agents to invoke them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chaoyang78/skills/opencli-usage) <br>
- [OpenCLI Chrome Web Store extension](https://chromewebstore.google.com/detail/opencli/ildkmabpimmkaediidaifkhjpohdnifk) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Orients the agent to the OpenCLI command surface and points to specialized follow-on skills.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
