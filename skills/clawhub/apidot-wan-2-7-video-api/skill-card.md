## Description: <br>
Use APIDot for Wan 2.7 Video API workflows, including text-to-video API, image-to-video API, reference-to-video, edit-video, async task submission, task_id handling, polling, task status, webhook integration, and APIDot docs routing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiehao71727](https://clawhub.ai/user/jiehao71727) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and integration teams use this documentation-only skill to find APIDot Wan 2.7 Video docs, plan async video generation or edit workflows, and handle task IDs, polling, webhooks, media persistence, and API-key hygiene. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: APIDot API keys could be exposed if copied into browser code, public repositories, logs, screenshots, or chat output. <br>
Mitigation: Keep APIDOT_API_KEY in a server-side secret store or environment variable and avoid displaying or logging it. <br>
Risk: Wan 2.7 Video request fields, model availability, limits, or commercial terms may change outside this static skill. <br>
Mitigation: Use the live APIDot docs and model page as the source of truth before preparing requests or making product claims. <br>
Risk: Unintended live API calls can consume external API resources or submit private media. <br>
Mitigation: Make live APIDot calls only when intentionally building an integration in a safe server-side environment. <br>
Risk: Video workflows may mishandle private prompts, media URLs, generated video URLs, callback URLs, retries, or duplicate webhook deliveries. <br>
Mitigation: Validate source media URLs, persist task state, avoid logging sensitive values, retry transient failures with backoff, and make webhook handlers idempotent. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jiehao71727/skills/apidot-wan-2-7-video-api) <br>
- [APIDot Wan 2.7 Video Reference](references/api.md) <br>
- [APIDot docs](https://apidot.ai/docs) <br>
- [APIDot Wan 2.7 Video docs](https://apidot.ai/docs/wan-2-7-video) <br>
- [APIDot Wan 2.7 Video model page](https://apidot.ai/models/wan-2-7-video) <br>
- [APIDot examples](https://github.com/APIDotAI/apidot-examples) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, configuration] <br>
**Output Format:** [Markdown guidance with links and configuration notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only; no executable files, bundled API client, automatic network calls, or stored credentials.] <br>

## Skill Version(s): <br>
1.0.2 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
