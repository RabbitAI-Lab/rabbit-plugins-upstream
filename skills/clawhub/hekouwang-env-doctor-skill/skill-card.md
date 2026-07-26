## Description: <br>
env-doctor audits developer-tool disk usage on macOS and Linux, identifies likely leftover tools and caches, and guides user-confirmed cleanup while distinguishing data that should not be deleted. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huiyonghkw](https://clawhub.ai/user/huiyonghkw) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and engineers use this skill in Claude Code to understand which local development tools, package caches, containers, simulators, and model caches are consuming disk space. It helps them review evidence-based classifications and choose whether to run user-confirmed cleanup actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Cleanup can remove version-manager directories or caches that the user may later need. <br>
Mitigation: Start with the dry-run cleanup selector, review each listed command and cost, and select only entries the user recognizes. <br>
Risk: Deleting version-manager directories without updating shell initialization files can cause future terminal startup errors. <br>
Mitigation: After removing a version manager, manually review shell configuration for the corresponding initialization lines. <br>
Risk: Developer caches, package stores, model weights, and container data can be expensive or unsafe to delete indiscriminately. <br>
Mitigation: Keep data-class items locked out of cleanup and prefer official cache commands for cache-class entries. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/huiyonghkw/skills/hekouwang-env-doctor-skill) <br>
- [Publisher profile](https://clawhub.ai/user/huiyonghkw) <br>
- [Rule library](references/rules.md) <br>
- [Report format and conversation flow](references/report.md) <br>
- [Safety boundaries](references/safety.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown reports with inline bash command blocks and plain-text scan summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill classifies findings as leftover, cache, data, or uncertain and emphasizes user review before cleanup.] <br>

## Skill Version(s): <br>
1.1.0 (source: release evidence and changelog, released 2026-07-18) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
