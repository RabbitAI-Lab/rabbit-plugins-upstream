## Description: <br>
Expand concise music-style ideas on PoYo / poyo.ai via `https://api.poyo.ai/api/generate/submit`; use for `boost-music-style`, music prompt enhancement, genre and mood expansion, instrumentation direction, production descriptors, Generate Music preparation, callbacks, and music detail retrieval. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and music creators use this skill to turn concise genre, mood, instrumentation, tempo, or production notes into richer PoYo style descriptions before a Generate Music workflow. The skill also guides reviewed asynchronous submission, callback handling, and music-detail retrieval when live calls are explicitly requested in a trusted environment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Live PoYo requests send style prompt content to an external API and require a POYO_API_KEY. <br>
Mitigation: Keep the API key server-side, make live calls only in trusted environments, and avoid confidential campaign or customer data unless sharing it with PoYo is acceptable. <br>
Risk: The enhanced style description may drift from the user's intended genre, mood, instrumentation, or production direction. <br>
Mitigation: Review the returned description before using it in Generate Music and keep only details that match the user's intent. <br>
Risk: Unreviewed payload files or callback URLs can submit unintended content or route results to the wrong endpoint. <br>
Mitigation: Review the payload file, callback URL, and shell command before submission, then save the returned task_id for controlled result retrieval. <br>


## Reference(s): <br>
- [PoYo Boost Music Style model page](https://poyo.ai/models/boost-music-style) <br>
- [PoYo Boost Music Style API docs](https://docs.poyo.ai/api-manual/music-series/boost-music-style) <br>
- [PoYo query music detail docs](https://docs.poyo.ai/api-manual/music-series/query-music-detail) <br>
- [PoYo music webhook docs](https://docs.poyo.ai/api-manual/music-series/music-webhook) <br>
- [PoYo Boost Music Style API Reference](references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with JSON payload summaries and optional bash or curl commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include a PoYo task_id, result retrieval method, and notes for using the enhanced style description in the next music-generation step.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
