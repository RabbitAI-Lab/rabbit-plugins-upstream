## Description: <br>
Pre-commit and pre-ship code review with Codex by default and optional Claude or Pi review engines. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tinycen](https://clawhub.ai/user/tinycen) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and engineering teams use this skill to run structured review over local, branch, pull request, or commit changes before shipping. It helps identify concrete correctness, security, maintainability, and regression risks while keeping findings advisory and human-reviewed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Review findings can be incorrect, speculative, or out of scope for the current change. <br>
Mitigation: Verify every accepted finding against the real code path and classify scope before making changes. <br>
Risk: Automated review can miss user-visible behavior regressions even when the source review is clean. <br>
Mitigation: Pair review with focused tests or behavior validation for UI, CLI, API, and generated-artifact changes. <br>
Risk: Reviewer subprocesses and optional engines may need access to local code and tool credentials. <br>
Mitigation: Use the documented isolated review bundle, keep prompt and dataset inputs repo-relative, and avoid running unsupported engines that cannot confine project context. <br>


## Reference(s): <br>
- [Autoreview Skill](.agents/skills/autoreview/SKILL.md) <br>
- [Autoreview Maintainer Notes](.agents/skills/autoreview/AGENTS.md) <br>
- [ClawHub Security Documentation](docs/security.md) <br>
- [OpenAI Latest Model Guide](https://developers.openai.com/api/docs/guides/latest-model) <br>
- [Claude Code Model Configuration](https://code.claude.com/docs/en/model-config) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown review findings and shell command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Findings are advisory and should be verified against the actual code path before applying changes.] <br>

## Skill Version(s): <br>
1.2.0 (source: target metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
