## Description: <br>
Opphub connects an OppHub account to OpenClaw so agents can add company knowledge, search business opportunities, and receive push updates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mtty-ai](https://clawhub.ai/user/mtty-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
OpenClaw users and operators use this skill to authenticate to OppHub, manage company knowledge records, run opportunity matching, and configure push or scheduled status workflows from chat or OpenClaw commands. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can rely on persistent account tokens and local credential lookups for OppHub access. <br>
Mitigation: Install only from a trusted publisher, keep the OpenClaw runtime patched, and remove the Keychain token or other local token storage when uninstalling. <br>
Risk: Endpoint override environment variables can redirect OppHub API or OAuth token traffic. <br>
Mitigation: Before use, verify that OPPHUB_API_BASE and OPPHUB_OAUTH_TOKEN_URL are unset or point to the expected OppHub service. <br>
Risk: Scheduled tasks may run skill commands without direct user interaction. <br>
Mitigation: Confirm any cron job the skill creates and remove scheduled jobs during uninstall or when no longer needed. <br>
Risk: The current artifact is reported to contain syntax-broken routed scripts. <br>
Mitigation: Require the publisher to fix and republish the affected scripts before relying on the skill in routine workflows. <br>


## Reference(s): <br>
- [ClawHub Opphub skill page](https://clawhub.ai/mtty-ai/skills/opphub) <br>
- [Publisher profile](https://clawhub.ai/user/mtty-ai) <br>
- [OppHub skill homepage](https://github.com/mtty-ai/opphub-skill) <br>
- [OppHub API base](https://api.opphub.ruiplus.cn) <br>
- [OppHub activation page](https://api.opphub.ruiplus.cn/activate?signup=1) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance and JSON responses from CLI commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js >=18, OpenClaw, the OppHub plugin, network access to the OppHub API, and local credential storage.] <br>

## Skill Version(s): <br>
4.0.7 (source: SKILL.md frontmatter, package.json, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
