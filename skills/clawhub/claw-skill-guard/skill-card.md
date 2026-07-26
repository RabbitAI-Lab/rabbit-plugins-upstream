## Description: <br>
Security scanner for OpenClaw skills. Detects malicious patterns, suspicious URLs, and install traps before you install a skill. Use before installing ANY skill from ClawHub or external sources. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vincentchan](https://clawhub.ai/user/vincentchan) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and engineers use this skill to scan local or remote OpenClaw skills before installation, review suspicious commands and URLs, and add optional workflow controls such as an AGENTS.md policy or pre-commit hook. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Scanner output may miss sophisticated obfuscation or produce false positives because detection is based on patterns and allowlists. <br>
Mitigation: Treat results as advisory and manually review flagged commands, URLs, dependency installs, and credential access before installing a skill. <br>
Risk: Remote ClawHub or direct URL scans fetch archives or text over the network and process downloaded content. <br>
Mitigation: Prefer trusted ClawHub or local sources, and avoid scanning malformed, untrusted, or oversized remote archives in sensitive environments. <br>
Risk: AGENTS.md policy and pre-commit hook examples add ongoing workflow controls that can block or warn on skill changes. <br>
Mitigation: Enable those controls only when they match the workspace workflow and keep a human approval path for reviewed exceptions. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/vincentchan/skills/claw-skill-guard) <br>
- [1Password analysis of malicious OpenClaw skills](https://1password.com/blog/from-magic-to-malware-how-openclaws-agent-skills-become-an-attack-surface) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Console reports, Markdown policy snippets, shell commands, JSON pattern configuration, and Python scanner code] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Scanner reports classify findings as critical, high, medium, low, or safe and return nonzero exit codes for high or critical findings.] <br>

## Skill Version(s): <br>
1.1.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
