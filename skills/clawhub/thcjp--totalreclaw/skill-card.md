## Description: <br>
TotalReclaw provides end-to-end encrypted, decentralized memory for OpenClaw-compatible agents, with native recall, automatic background capture, and explicit CLI capture when requested. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to install, pair, and operate TotalReclaw as an encrypted memory provider for OpenClaw-compatible agents. It guides native memory recall, explicit memory capture, setup, reinstall recovery, and safe handling of recovery phrases and credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Persistent automatic memory capture can store user facts without a separate per-fact prompt. <br>
Mitigation: Deploy only where persistent memory is desired, make users aware of automatic capture, and use explicit recall or curation workflows when reviewing stored information. <br>
Risk: Reinstall recovery includes a destructive cleanup command for leftover package directories. <br>
Mitigation: Review the exact target path before running cleanup and confirm it is limited to TotalReclaw package artifacts, not credentials or unrelated files. <br>
Risk: Pairing and setup involve recovery phrases, credential files, and encryption key material. <br>
Mitigation: Use the browser-based pairing flow and never ask the agent to read, display, or inspect recovery phrases, credentials, keys, or related secrets. <br>
Risk: Autonomous restart or detached pairing fallback actions can reduce operator control. <br>
Mitigation: Run restart and detached background actions only with operator awareness and verify the need for those actions before execution. <br>


## Reference(s): <br>
- [Totalreclaw ClawHub release page](https://clawhub.ai/thcjp/skills/totalreclaw) <br>
- [TotalReclaw Skill Platform setup guide](https://github.com/p-diogo/totalreclaw/blob/main/docs/guides/skill-platform-setup.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown instructions with inline shell commands and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May emit setup URLs, PINs, and CLI command guidance; recovery phrases and credential files should not be exposed to the agent context.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact frontmatter reports 3.3.13) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
