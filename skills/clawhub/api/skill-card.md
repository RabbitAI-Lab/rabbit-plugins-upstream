## Description: <br>
Integrates and debugs third-party REST and GraphQL APIs, covering auth, rate limits, pagination, webhooks, service-specific references, and safe request examples. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to consume and troubleshoot third-party APIs, choose authentication and integration patterns, and generate safe request examples or client snippets for external services. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated POST, PATCH, DELETE, payment, or message examples can affect live services if copied with live credentials. <br>
Mitigation: Use sandbox credentials by default, confirm the target environment before live use, and review mutating requests before running them. <br>
Risk: API examples may involve secrets, customer data, transcripts, or regulated content. <br>
Mitigation: Use environment variable names instead of secret values and avoid adding sensitive data to examples without authorization. <br>
Risk: Provider API behavior, versions, and deprecation status can change after the skill is published. <br>
Mitigation: Check provider documentation and version or deprecation headers before relying on examples for production changes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ivangdavila/skills/api) <br>
- [Clawic API skill page](https://clawic.com/skills/api) <br>
- [Skill definition](artifact/SKILL.md) <br>
- [Authentication guide](artifact/auth.md) <br>
- [API debugging guide](artifact/debug.md) <br>
- [Rate limits guide](artifact/rate-limits.md) <br>
- [Webhook guide](artifact/webhooks.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline code blocks, curl examples, and configuration notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference local preferences in ~/Clawic/data/api/config.yaml and uses sandbox examples by default unless live use is explicitly requested.] <br>

## Skill Version(s): <br>
1.3.7 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
