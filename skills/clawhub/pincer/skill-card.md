## Description: <br>
Pincer is a security-first wrapper for installing agent skills that scans for malware, prompt injection, and suspicious patterns before installation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[panzacoder](https://clawhub.ai/user/panzacoder) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent users use Pincer to scan ClawHub skills before installation, audit installed skills, and manage trusted or blocked publishers. It is intended as a safety layer around normal skill installation workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The server security summary says Pincer's safety gate can run install actions before scanning in a fallback path. <br>
Mitigation: Use scan-only workflows for higher-risk skills, review the skill source before install, and avoid installing high-risk third-party skills until the fallback install-before-scan behavior is removed. <br>
Risk: The server security summary says Pincer relies on an unpinned external scanner. <br>
Mitigation: Run Pincer in a controlled environment, review scanner behavior before relying on it, and prefer a pinned scanner version when available. <br>
Risk: Automatic approval can reduce human review of clean scan results. <br>
Mitigation: Set autoApprove to never and review ~/.config/pincer/config.json before using Pincer for sensitive environments. <br>


## Reference(s): <br>
- [Pincer ClawHub Skill Page](https://clawhub.ai/panzacoder/skills/pincer) <br>
- [Invariant Labs mcp-scan](https://github.com/invariantlabs-ai/mcp-scan) <br>
- [1Password Security Research: Agent Skills Attack Surface](https://1password.com/blog/from-magic-to-malware-how-openclaws-agent-skills-become-an-attack-surface) <br>
- [Snyk ToxicSkills Report](https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub/) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Analysis, JSON] <br>
**Output Format:** [Markdown documentation with inline shell commands and optional JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can report scan results, installation decisions, audit summaries, trust settings, and history entries.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
