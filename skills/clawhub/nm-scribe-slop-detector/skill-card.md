## Description: <br>
Detects AI-generated writing patterns in prose. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and documentation maintainers use this skill to audit prose, code comments, READMEs, and repository documentation for AI-writing markers, hallucinated references, identity leaks, and cleanup candidates before publishing or merging. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill performs broad repository and documentation auditing, which can produce findings beyond lightweight prose detection. <br>
Mitigation: Use report-only review by default and require a human to approve findings before changing files. <br>
Risk: Network validation, delegated remediation, auto-apply behavior, and local scan history can expand the skill's operational footprint. <br>
Mitigation: Require explicit approval before network checks, delegated remediation, or auto-apply runs, and avoid --track unless local scan history is acceptable. <br>
Risk: Over-aggressive cleanup can remove useful comments, historical text, or low-confidence patterns that are legitimate in context. <br>
Mitigation: Follow the artifact's anti-goals: do not auto-apply low-confidence findings, preserve safety and invariant comments, and surface uncertain changes for human decision. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-scribe-slop-detector) <br>
- [OpenClaw homepage metadata](https://github.com/athola/claude-night-market/tree/master/plugins/scribe) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown reports, structured finding records, and optional CI JSON or JSONL] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include line-anchored findings, scores, suggested fixes, high-confidence diffs, CI exit status, and optional local scan history when tracking is enabled.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
