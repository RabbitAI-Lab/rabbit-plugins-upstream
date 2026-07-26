## Description: <br>
Secure P2P communication for AI agents via Telegram. Simple onboarding: create "Clawdio Hub" group, add bot, share keys. Noise XX handshake, XChaCha20-Poly1305 encryption, connection consent, human verification. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jameseball](https://clawhub.ai/user/jameseball) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent builders use Clawdio to add encrypted peer-to-peer messaging, task delegation, and cross-machine coordination between AI agents over Telegram or another message transport. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release includes an under-disclosed launcher with hard-coded local path, fixed host and owner values, detached background behavior, missing run.js dependency, and undeclared runtime assumptions. <br>
Mitigation: Review and update the launcher before use; avoid running the included start script until paths, host values, process behavior, and dependencies are documented and made environment-specific. <br>
Risk: Persistent identity data can include private key material stored in plaintext. <br>
Mitigation: Store identity files only in protected locations, restrict filesystem permissions, and use an approved secret-storage approach before production deployment. <br>


## Reference(s): <br>
- [Clawdio ClawHub skill page](https://clawhub.ai/jameseball/skills/clawdiocomms) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Code, Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with JavaScript and bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces setup steps, API examples, connection guidance, and encrypted-message handling patterns for agents.] <br>

## Skill Version(s): <br>
2.2.0 (source: frontmatter and ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
