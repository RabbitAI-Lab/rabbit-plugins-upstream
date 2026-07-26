## Description: <br>
Helps developers integrate and administer Yandex SmartCaptcha across websites, React, Vue, and mobile apps, including server-side token validation, Yandex Cloud setup, troubleshooting, and examples. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rekryt](https://clawhub.ai/user/rekryt) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to add Yandex SmartCaptcha to web, SPA, and mobile application flows and to configure the related Yandex Cloud resources. It provides implementation guidance, reusable snippets, validation patterns, troubleshooting steps, and operational references. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Documented fail-open behavior can weaken bot-protection controls when SmartCaptcha validation is unavailable. <br>
Mitigation: Review generated code before production use and consider fail-closed or risk-based fallback for sensitive actions. <br>
Risk: Unexpected or empty host values can weaken protection when domain checks are disabled. <br>
Mitigation: Reject unexpected hosts and handle empty host values deliberately in server-side validation. <br>
Risk: Exposed server keys can compromise SmartCaptcha validation. <br>
Mitigation: Keep server keys only in backend secrets or environment variables and never ship them in frontend code. <br>
Risk: Example dependencies may become stale over time. <br>
Mitigation: Pin or update dependencies and run normal dependency scanning before production use. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/rekryt/skills/skill-smartcaptcha) <br>
- [Server-Resolved Source Repository](https://github.com/rekryt/skill-smartcaptcha) <br>
- [Yandex SmartCaptcha Documentation](https://yandex.cloud/ru/docs/smartcaptcha/) <br>
- [Yandex SmartCaptcha User Validation](https://yandex.cloud/ru/docs/smartcaptcha/concepts/validation) <br>
- [Yandex SmartCaptcha Keys](https://yandex.cloud/ru/docs/smartcaptcha/concepts/keys) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with code snippets, configuration examples, shell commands, and reusable templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated outputs should be reviewed before production use, especially validation fallback behavior, host handling, secret management, and example dependencies.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
