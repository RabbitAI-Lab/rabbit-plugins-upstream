## Description: <br>
Create a reusable music persona on PoYo / poyo.ai via `https://api.poyo.ai/api/generate/submit`; use for `generate-persona`, completed music task ids, audio ids, persona names and descriptions, persona_id workflows, callbacks, music detail polling, and consistent follow-up music generation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to prepare, validate, and optionally submit PoYo Generate Persona requests for completed eligible music tracks, then guide result retrieval for the resulting persona_id. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Persona generation sends PoYo task IDs, audio IDs, persona descriptions, and any callback URL to PoYo. <br>
Mitigation: Submit only data the user is comfortable sharing with PoYo and the callback receiver. <br>
Risk: The helper script requires POYO_API_KEY and performs a live curl request when run. <br>
Mitigation: Run it only from a trusted server-side shell with POYO_API_KEY stored securely. <br>
Risk: Source audio may contain private content or rights-restricted material. <br>
Mitigation: Confirm the user has the right to process the source audio and create a reusable persona from it before submission. <br>


## Reference(s): <br>
- [PoYo Generate Persona API Reference](references/api.md) <br>
- [PoYo Generate Persona model page](https://poyo.ai/models/generate-persona) <br>
- [PoYo Generate Persona API docs](https://docs.poyo.ai/api-manual/music-series/generate-persona) <br>
- [PoYo query music detail API docs](https://docs.poyo.ai/api-manual/music-series/query-music-detail) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, API calls] <br>
**Output Format:** [Markdown guidance with JSON payload examples and optional bash/curl commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include a final payload or parameter summary, returned task id, polling or webhook next steps, and resulting persona_id when available.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
