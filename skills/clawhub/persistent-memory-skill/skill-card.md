## Description: <br>
Use when a user wants cross-session personal context shared by compatible AI agents, or asks to load, save, inspect, archive, recover, clean up, or upgrade local memory files. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rainypilgrimage-beep](https://clawhub.ai/user/rainypilgrimage-beep) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to let compatible agents share reviewed local context through plain Markdown files, while keeping saves, lifecycle changes, and recovery actions user-confirmed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local memory files are plain-text Markdown and may expose secrets or sensitive personal data to compatible agents on the same machine or filesystem. <br>
Mitigation: Keep ~/.persistent-memory/ free of passwords, API keys, secrets, and highly sensitive personal data; periodically inspect the folder contents. <br>
Risk: Shared context can become stale or incorrect if agents save or update memory without careful review. <br>
Mitigation: Use explicit memory commands when possible and require user confirmation for proposed content, destination, summary, index, archive, delete, and recovery changes. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/rainypilgrimage-beep/skills/persistent-memory-skill) <br>
- [README](README.md) <br>
- [Changelog](CHANGELOG.md) <br>
- [v0.8 Summary-First Prototype Protocol](docs/experiments/v08-summary-first-prototype.md) <br>
- [v0.8 Summary-First Prototype Results](docs/experiments/v08-summary-first-results.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance, Configuration, Shell commands] <br>
**Output Format:** [Markdown guidance with file paths, proposed memory content, and confirmation prompts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose local Markdown file reads, writes, moves, archive actions, recovery actions, and index updates after explicit user confirmation.] <br>

## Skill Version(s): <br>
0.8.0 (source: release metadata and changelog, released 2026-07-15) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
