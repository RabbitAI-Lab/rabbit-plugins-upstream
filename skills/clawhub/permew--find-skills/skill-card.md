## Description: <br>
Find Skills searches skills.sh, ClawHub, and GitHub for agent skills, summarizes registry-specific signals, scans top candidates for risk patterns, and helps recommend or install a suitable skill. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[permew](https://clawhub.ai/user/permew) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill when deciding whether an existing agent skill can satisfy a task before building or installing one. It searches multiple registries, highlights installed and cross-posted candidates, and supports human review before recommendations or installation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Recommended skills can be third-party code that is untrusted or unscanned by this skill. <br>
Mitigation: Review each candidate's SKILL.md and bundled scripts before installing or recommending it, especially GitHub-only results. <br>
Risk: The built-in security scan is heuristic and a clean result is not a full security audit. <br>
Mitigation: Treat scan badges as triage signals and perform human review before relying on a candidate skill. <br>
Risk: Installation commands can add skills that later run with broad agent permissions. <br>
Mitigation: Only approve installation commands for a specific user-chosen skill after reviewing the source and expected behavior. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/permew/skills/find-skills) <br>
- [Skill homepage](https://agentspace.so) <br>
- [skills.sh search API](https://skills.sh/api/search) <br>
- [ClawHub search API](https://clawhub.ai/api/search) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Plain-text or JSON registry search report with recommendation guidance and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires jq and curl; GitHub and ClawHub body inspection degrade gracefully when optional gh or unzip are unavailable.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
