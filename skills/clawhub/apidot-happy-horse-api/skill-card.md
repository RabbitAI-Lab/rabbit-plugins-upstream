## Description: <br>
Use APIDot for Happy Horse API workflows, including Alibaba Happy Horse video generation, text-to-video API, image-to-video API, reference-to-video API, video editing API, async task submission, task_id handling, polling, task status, and webhook integration based on APIDot docs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiehao71727](https://clawhub.ai/user/jiehao71727) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to route Happy Horse API integration questions to APIDot documentation, examples, and async workflow guidance for text-to-video, image-to-video, reference-to-video, and video editing tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: APIDOT_API_KEY could be exposed if copied into client code, logs, screenshots, public repositories, or chat output. <br>
Mitigation: Keep the key only in server-side environment variables or a backend secret manager, and avoid echoing credentials in generated examples or diagnostics. <br>
Risk: Live Happy Horse requests may include sensitive prompts, private media URLs, callback URLs, or generated video links. <br>
Mitigation: Make live API calls only when explicitly requested in a trusted server-side environment, and treat prompts, media URLs, callback URLs, and output links as sensitive data. <br>
Risk: Outdated or guessed model-specific payload fields could cause incorrect integration guidance. <br>
Mitigation: Use current APIDot model pages, API docs, and examples for request fields, availability, limits, and commercial terms. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jiehao71727/skills/apidot-happy-horse-api) <br>
- [APIDot documentation](https://apidot.ai/docs) <br>
- [APIDot Happy Horse model page](https://apidot.ai/models/happy-horse) <br>
- [APIDot Happy Horse API docs](https://apidot.ai/docs/happy-horse) <br>
- [APIDot quickstart](https://apidot.ai/docs/quickstart) <br>
- [APIDot webhooks](https://apidot.ai/docs/webhooks) <br>
- [Local API reference](references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, configuration, guidance] <br>
**Output Format:** [Markdown guidance with documentation links, workflow notes, and integration planning details.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only; no executable behavior, bundled API client, network calls, stored credentials, or install-time automation.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
