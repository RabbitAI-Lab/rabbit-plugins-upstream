## Description: <br>
Conduct open-ended research on a topic, building a living markdown document. Supports interactive and deep research modes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[brennerspear](https://clawhub.ai/user/brennerspear) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and other agent users use this skill to investigate topics, compare options, gather sources, and preserve findings in living research documents. For deeper investigations, it can guide use of the Parallel AI CLI and save asynchronous results as markdown or PDF research artifacts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Research prompts and outputs may be persisted locally and deep research requests may be sent to Parallel AI. <br>
Mitigation: Use the skill only with research content appropriate for local storage and third-party processing. <br>
Risk: Setup instructions include shell profile changes, symlinks, remote installer execution, and optional system-wide installation. <br>
Mitigation: Verify helper scripts and installers from trusted sources, prefer user-local symlinks, avoid curl-to-shell installation where possible, and avoid sudo unless explicitly needed. <br>
Risk: The setup stores and loads a Parallel AI API key from the user's environment. <br>
Mitigation: Use a scoped or revocable API key, keep secret files permission-restricted, and avoid broadly loading secrets into shell profiles. <br>
Risk: Optional delayed research checks may cause agent activity after the initial request. <br>
Mitigation: Review scheduled jobs, ensure delivery targets are correct, and confirm scheduled times before enabling auto-check behavior. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/brennerspear/skills/parallel-ai-research) <br>
- [Research skill instructions](SKILL.md) <br>
- [Setup guide](SETUP.md) <br>
- [OpenClaw integration](OPENCLAW.md) <br>
- [OpenClaw](https://openclaw.ai) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and optional JSON scheduling snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update prompt, research, and PDF files under the user's research workspace.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
