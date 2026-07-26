## Description: <br>
Use APIDot for Generate Music API workflows, including prompt-to-song generation, instrumental generation, vocal music planning, async task submission, task_id handling, music detail polling, callback_url planning, webhook integration, and APIDot docs routing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiehao71727](https://clawhub.ai/user/jiehao71727) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to route APIDot Generate Music questions to the correct docs and plan prompt-to-song, instrumental, vocal, polling, callback, and webhook integration workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: APIDot API keys or sensitive callback, webhook, prompt, or generated audio data could be exposed in client code, logs, screenshots, repositories, or chat output. <br>
Mitigation: Keep APIDOT_API_KEY in server-side secrets only and avoid logging private prompts, callback URLs, webhook payloads, API keys, or generated audio URLs. <br>
Risk: Generated API guidance may become stale as APIDot model fields, pricing, limits, or availability change. <br>
Mitigation: Review current APIDot docs, model pages, and pricing before making live API calls or committing integration behavior. <br>
Risk: Agents could make unintended live API calls while assisting with integration planning. <br>
Mitigation: Make live APIDot calls only when the user explicitly asks and provides a safe server-side environment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jiehao71727/skills/apidot-generate-music-api) <br>
- [APIDot documentation](https://apidot.ai/docs) <br>
- [APIDot Generate Music model page](https://apidot.ai/models/generate-music) <br>
- [APIDot Generate Music docs](https://apidot.ai/docs/generate-music) <br>
- [APIDot music detail docs](https://apidot.ai/docs/music-detail) <br>
- [APIDot webhooks docs](https://apidot.ai/docs/webhooks) <br>
- [APIDot Generate Music reference](references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, configuration, guidance] <br>
**Output Format:** [Markdown guidance with API planning notes and optional code or configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only; no executable behavior, bundled API client, automatic network calls, or stored credentials.] <br>

## Skill Version(s): <br>
1.0.3 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
