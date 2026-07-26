## Description: <br>
A collection of OpenClaw and third-party agent skills for code review, ClawHub operations, Convex development, observability, documentation, design, and release workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and operators use these skills to guide agent work across review, release, ClawHub maintenance, Convex application development, observability workflows, documentation, and interface design. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Skills may propose shell commands, configuration changes, code edits, or API operations that affect local files or connected services. <br>
Mitigation: Review proposed actions before execution, run in a constrained workspace, and require explicit approval for sensitive service changes. <br>
Risk: Some workflows reference credentials or service tokens for tools such as OpenAI, Axiom, Sentry, Slack, or Grafana. <br>
Mitigation: Use least-privilege credentials, keep secret values out of prompts and logs, and rotate tokens if exposure is suspected. <br>
Risk: The release includes third-party imported skills with separate provenance and license signals. <br>
Mitigation: Review the included provenance snapshots and original publisher materials before deploying those skills in sensitive environments. <br>


## Reference(s): <br>
- [ClawHub repository](https://github.com/openclaw/clawhub) <br>
- [ClawHub README](README.md) <br>
- [ClawHub skill format](docs/skill-format.md) <br>
- [ClawHub security audits](docs/security-audits.md) <br>
- [Axiom skills provenance](.agents/skills/axiomhq-skills.provenance.json) <br>
- [Sentry for AI skill provenance](.agents/skills/getsentry-sentry-for-ai.provenance.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline code, shell commands, configuration snippets, and file-change instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Some skills can call local scripts, CLIs, or external service APIs when the agent and environment permit those actions.] <br>

## Skill Version(s): <br>
1.0.1 (source: target metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
