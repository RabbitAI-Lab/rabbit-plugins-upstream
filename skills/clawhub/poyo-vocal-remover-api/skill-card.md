## Description: <br>
Separate vocals and instrument stems on PoYo / poyo.ai via https://api.poyo.ai/api/generate/submit for separate-vocals, stem-split, upload-and-separate-vocals, vocal remover workflows, stem isolation, callbacks, and music detail retrieval. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to prepare PoYo vocal-removal or stem-separation requests, choose the appropriate model id, submit trusted payloads, and plan result retrieval through music detail polling or callbacks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can submit audio-processing requests to an external PoYo API using POYO_API_KEY. <br>
Mitigation: Install only when PoYo processing is intended, keep POYO_API_KEY in a server-side environment or secret manager, and submit requests only after reviewing the payload. <br>
Risk: Audio URLs, callback URLs, task IDs, audio IDs, and generated stem URLs may expose private workflow or media details if logged or shared. <br>
Mitigation: Avoid logging or displaying private URLs, identifiers, raw authorization headers, and generated stem URLs unless the product policy explicitly allows it. <br>


## Reference(s): <br>
- [PoYo Vocal Remover API Reference](references/api.md) <br>
- [PoYo Vocal Remover API model page](https://poyo.ai/models/vocal-remover-api) <br>
- [PoYo separate vocals documentation](https://docs.poyo.ai/api-manual/music-series/vocal-remover/separate-vocals) <br>
- [PoYo stem split documentation](https://docs.poyo.ai/api-manual/music-series/vocal-remover/stem-split) <br>
- [PoYo upload and separate vocals documentation](https://docs.poyo.ai/api-manual/music-series/vocal-remover/upload-and-separate-vocals) <br>
- [PoYo query music detail documentation](https://docs.poyo.ai/api-manual/music-series/query-music-detail) <br>
- [PoYo music webhook documentation](https://docs.poyo.ai/api-manual/music-series/music-webhook) <br>
- [ClawHub skill page](https://clawhub.ai/coolhackboy/skills/poyo-vocal-remover-api) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown with JSON payload examples and inline bash commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include selected model id, required input fields, payload summary, returned task id when submitted, and next-step retrieval guidance.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
