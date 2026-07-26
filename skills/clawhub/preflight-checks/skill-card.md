## Description: <br>
Preflight Checks helps agents create and run behavioral checklists that compare expected actions against actual responses after memory loads or updates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivanmmm](https://clawhub.ai/user/ivanmmm) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent operators use this skill to set up scenario-based behavioral checks for agents with persistent memory, then compare agent responses with expected answers to detect drift after restarts, updates, or memory changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The initialization script creates or overwrites PRE-FLIGHT-CHECKS.md and PRE-FLIGHT-ANSWERS.md in the selected workspace. <br>
Mitigation: Run setup only from the intended workspace and review the generated files before using them as agent instructions. <br>
Risk: Bundled examples include Prometheus-specific identity, communication, and memory behavior that may not match another agent. <br>
Mitigation: Customize the templates for the target agent and remove or ignore example-specific behavior before operational use. <br>
Risk: Behavioral checks can encourage persistent memory writes or external communication if the user's expected answers allow them. <br>
Mitigation: Require explicit approval for sensitive memory writes, public posts, third-party messages, credentials, personal data, and ambiguous retained content. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ivanmmm/skills/preflight-checks) <br>
- [README](README.md) <br>
- [Skill Documentation](SKILL.md) <br>
- [Changelog](CHANGELOG.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown files and text guidance with shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces workspace checklist and answer templates that users customize for their agent behavior rules.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata, package.json, CHANGELOG; released 2026-02-06) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
