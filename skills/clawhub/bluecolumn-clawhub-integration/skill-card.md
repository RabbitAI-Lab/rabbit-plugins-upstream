## Description: <br>
BlueColumn ClawHub Integration helps agents configure ClawHub audio ingest, memory, and semantic retrieval through BlueColumn AI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bluecolumnconsulting-lgtm](https://clawhub.ai/user/bluecolumnconsulting-lgtm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Use this skill when an agent needs to wire ClawHub audio workflows to BlueColumn AI, including recorded audio ingest, live streaming setup, request metadata, mode selection, webhook handling, and retrieval-related endpoint compatibility. <br>

### Deployment Geography for Use: <br>
Use where ClawHub and BlueColumn AI are available and where the operator can meet local consent, data protection, retention, and webhook security requirements for audio and derived transcripts. <br>

## Known Risks and Mitigations: <br>
Risk: The security evidence flags sensitive audio storage and sensitive derived data handling. <br>
Mitigation: Enable the integration only with user consent, clear retention expectations, and secure webhook endpoints; treat audio, transcripts, summaries, entities, sentiment, embeddings, identifiers, and webhook payloads as sensitive. <br>
Risk: The security evidence flags insecure API-key storage guidance in the artifact. <br>
Mitigation: Store the BlueColumn API key only in the platform secret store and do not place secrets in markdown files or logs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/bluecolumnconsulting-lgtm/skills/bluecolumn-clawhub-integration) <br>
- [Publisher profile](https://clawhub.ai/user/bluecolumnconsulting-lgtm) <br>
- [BlueColumn AI](https://bluecolumn.ai) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown guidance with endpoint paths, JSON request examples, required-field lists, and configuration notes.] <br>
**Output Parameters:** [Audio URL, namespace, session ID, user reference, source/channel/agent metadata, mode, tier, processing options, webhook URL, and API-key secret reference.] <br>
**Other Properties Related to Output:** [Generated guidance may describe handling for uploaded audio, transcripts, summaries, entities, sentiment, embeddings, identifiers, and webhook payloads; operators should treat those outputs as sensitive.] <br>

## Skill Version(s): <br>
1.0.0 <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
