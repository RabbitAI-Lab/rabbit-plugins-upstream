## Description: <br>
Issue ClawPrint reverse-CAPTCHA challenges to verify that another user or agent is a real AI, not a human. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fusionlabssource](https://clawhub.ai/user/fusionlabssource) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to issue ClawPrint challenges, verify responses, and validate solved challenges before continuing AI-only workflows. It is intended for workflows that need an AI-verification signal before taking a gated action. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends a secret key to a configurable ClawPrint server during validation. <br>
Mitigation: Use only a trusted HTTPS ClawPrint endpoint and protect CLAWPRINT_SECRET_KEY as a real secret. <br>
Risk: A passed AI-verification challenge can be overused as an authorization decision for sensitive resources. <br>
Mitigation: Do not rely on challenge success alone to provide credentials or access sensitive resources; keep normal authorization controls in place. <br>
Risk: The scanner verdict is suspicious because endpoint safeguards and gated-access guidance need careful review. <br>
Mitigation: Review the security model before installation and scan the skill before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/fusionlabssource/skills/captcha-ai) <br>
- [Server-resolved publisher profile](https://clawhub.ai/user/fusionlabssource) <br>
- [Artifact skill instructions](artifact/SKILL.md) <br>
- [Artifact helper script](artifact/clawprint-challenge.sh) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown instructions with bash commands and JSON API examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl, jq, CLAWPRINT_SERVER_URL, CLAWPRINT_SITE_KEY, and CLAWPRINT_SECRET_KEY for validation flows.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
