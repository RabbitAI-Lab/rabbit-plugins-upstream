## Description: <br>
Use APIDot async workflow for AI generation APIs, including task submission, task_id handling, polling API, task status API, callback_url, webhook API, retry guidance, idempotent webhook handling, image generation, video generation, music generation, and 3D generation based on APIDot docs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiehao71727](https://clawhub.ai/user/jiehao71727) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to design APIDot async generation integrations that submit tasks, persist task IDs, choose polling or webhook delivery, handle retries, and route to current APIDot documentation and examples. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: API keys or private generation data could be exposed while adapting APIDot examples. <br>
Mitigation: Keep APIDOT_API_KEY in backend secrets, avoid browser bundles and logs, and do not log private prompts, source media URLs, result URLs, or callback URLs. <br>
Risk: Model-specific request fields, webhook behavior, statuses, or product details may change over time. <br>
Mitigation: Verify current APIDot docs and model pages before making real API calls or publishing copyable integration code. <br>
Risk: Webhook or retry handling could attach duplicate or incorrect results to user records. <br>
Mitigation: Persist task IDs, verify task ownership, make webhook handlers idempotent, and keep submit retries separate from status polling retries. <br>


## Reference(s): <br>
- [APIDot Docs](https://apidot.ai/docs) <br>
- [APIDot Quickstart](https://apidot.ai/docs/quickstart) <br>
- [APIDot Webhooks](https://apidot.ai/docs/webhooks) <br>
- [APIDot Models](https://apidot.ai/models) <br>
- [APIDot Examples](https://github.com/APIDotAI/apidot-examples) <br>
- [APIDot Async Workflow on ClawHub](https://clawhub.ai/jiehao71727/skills/apidot-async-workflow) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with inline examples and links to current APIDot documentation] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only; no bundled executable files, setup automation, API clients, automatic network calls, or stored credentials.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
