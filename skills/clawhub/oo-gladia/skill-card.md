## Description: <br>
Gladia lets an agent operate an OOMOL-connected Gladia account for pre-recorded transcription jobs, uploads, downloads, listing, retrieval, and deletion. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to manage Gladia transcription workflows through an OOMOL-connected account, including starting jobs from public media URLs, uploading media, retrieving results, downloading original audio, listing jobs, and deleting transcription data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can start transcription jobs and upload media through the connected Gladia account. <br>
Mitigation: Review the proposed action, payload, media source, and expected account impact before approving write actions. <br>
Risk: The delete_transcription action can remove a transcription job and its associated data. <br>
Mitigation: Require explicit user confirmation of the target transcription before running destructive actions. <br>
Risk: The one-time oo CLI installer and connector access depend on trusting OOMOL as the connector provider. <br>
Mitigation: Install and authenticate the oo CLI only when the user intends to let Codex operate their connected Gladia account through OOMOL. <br>


## Reference(s): <br>
- [Gladia homepage](https://app.gladia.io/) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub Gladia skill page](https://clawhub.ai/oomol/skills/oo-gladia) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Files, Guidance] <br>
**Output Format:** [Markdown guidance with oo CLI shell commands and JSON connector responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create transcription jobs, upload media up to 100 MiB, download audio files, or delete transcription data after user confirmation.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
