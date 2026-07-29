## Description: <br>
flickies helps agents use a self-hosted video REST and MCP service for lipsync, face restoration, ffmpeg video operations, metadata probing, async jobs, and file delivery. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psyb0t](https://clawhub.ai/user/psyb0t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use flickies to submit video processing requests to a trusted Flickies server from REST, MCP, curl, or the bundled shell helper. It is suited for lipsync, face restore, trim, concat, transcode, scale, mux or extract audio, thumbnail grids, metadata probing, and async job workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: An unauthenticated or broadly exposed Flickies server can give network users access to the video API and MCP surface. <br>
Mitigation: Use the skill only with a Flickies server you control or trust, set FLICKIES_AUTH_TOKEN beyond localhost, and prefer loopback binding or an authenticated proxy. <br>
Risk: file_url, output_url, and webhook_url can cause the server to fetch from or send data to external or internal network locations. <br>
Mitigation: Avoid untrusted internal-network URLs and confirm destinations before using URL fetches, presigned output delivery, or webhooks. <br>
Risk: Staged-file removal and engine eviction are state-changing operations that can affect shared server instances. <br>
Mitigation: Only remove staged files or evict engines when the user asked and the resource belongs to the current task, especially on shared instances. <br>
Risk: Wav2Lip and Wav2Lip-GAN are gated as non-commercial engines and may be inappropriate for normal commercial workflows. <br>
Mitigation: Use the commercial-safe LatentSync default unless the server operator intentionally enabled FLICKIES_ENABLE_NONCOMMERCIAL for an allowed use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/flickies) <br>
- [flickies setup](references/setup.md) <br>
- [docker-flickies homepage](https://github.com/psyb0t/docker-flickies) <br>
- [Model Context Protocol](https://modelcontextprotocol.io) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, API calls, Code] <br>
**Output Format:** [Markdown guidance with bash commands, JSON request bodies, REST and MCP examples, and configuration values] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May direct a trusted Flickies server to create, fetch, upload, download, or remove staged video files depending on the requested operation.] <br>

## Skill Version(s): <br>
0.3.15 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
