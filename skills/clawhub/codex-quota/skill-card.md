## Description: <br>
Checks OpenAI Codex CLI daily and weekly rate limit status from local Codex session logs, with optional live refresh and all-account checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[odrobnik](https://clawhub.ai/user/odrobnik) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to inspect Codex CLI quota usage before starting heavy work, diagnosing possible rate limits, or checking multiple saved accounts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The all-account mode temporarily rewrites ~/.codex/auth.json while switching saved Codex accounts. <br>
Mitigation: Back up ~/.codex/auth.json before using --all --yes and avoid running it while other Codex processes are active. <br>
Risk: The skill reads local Codex session logs and may write account quota metadata to /tmp/codex-quota-all.json. <br>
Mitigation: Treat session-derived quota output and /tmp/codex-quota-all.json as sensitive local account-usage metadata. <br>


## Reference(s): <br>
- [Codex Quota on ClawHub](https://clawhub.ai/odrobnik/skills/codex-quota) <br>
- [Codex CLI](https://codex.openai.com) <br>
- [Setup Instructions](SETUP.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, guidance] <br>
**Output Format:** [Terminal text or JSON describing primary and secondary Codex quota windows, reset times, and source update time.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write all-account quota results to /tmp/codex-quota-all.json when run with --all --yes.] <br>

## Skill Version(s): <br>
1.2.2 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
