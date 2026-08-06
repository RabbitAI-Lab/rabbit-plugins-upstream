## Description: <br>
Flickies helps agents use a self-hosted video REST and MCP service for lipsync, face restoration, ffmpeg video operations, metadata probing, async jobs, and file staging. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psyb0t](https://clawhub.ai/user/psyb0t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use Flickies to send video-processing requests to a trusted Flickies server, including lipsync, face restoration, trimming, concatenation, transcoding, scaling, audio extraction or muxing, thumbnail generation, and metadata inspection. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The Flickies API can be exposed without authentication if FLICKIES_AUTH_TOKEN is unset. <br>
Mitigation: Use a trusted server, set FLICKIES_AUTH_TOKEN, and bind the service to localhost or place it behind an authenticated proxy before network exposure. <br>
Risk: file_url, output_url, and webhook_url cause server-side network actions. <br>
Mitigation: Use only trusted endpoints, avoid sending sensitive media to untrusted URLs, and treat webhook receivers as security-sensitive integrations. <br>
Risk: Lipsync and face-restoration workflows can create synthetic media with consent, licensing, or non-commercial-use constraints. <br>
Mitigation: Confirm media rights and consent before processing, and enable non-commercial engines only when their usage terms fit the deployment. <br>
Risk: File staging and engine management can remove files or evict resident models on a shared instance. <br>
Mitigation: Run state-changing operations only against resources created for the current task and only when explicitly requested. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/flickies) <br>
- [Setup guide](references/setup.md) <br>
- [Model Context Protocol](https://modelcontextprotocol.io) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, JSON API payloads] <br>
**Output Format:** [Markdown guidance with bash and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces client-side instructions and request payloads for an operator-managed Flickies server; generated media is produced by the configured server.] <br>

## Skill Version(s): <br>
0.3.16 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
