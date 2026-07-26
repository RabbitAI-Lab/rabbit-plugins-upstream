## Description: <br>
flickies helps agents drive a self-hosted video REST and MCP API for lipsync, face restoration, ffmpeg video operations, metadata probing, async jobs, and staged file workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psyb0t](https://clawhub.ai/user/psyb0t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to call a trusted flickies instance for video generation and processing tasks, including lipsync, face restoration, trim, concat, transcode, scale, mux, audio extraction, thumbnails, and ffprobe metadata. It is also useful when an LLM needs to operate the same video pipeline through MCP. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The flickies API and MCP surface are unauthenticated when FLICKIES_AUTH_TOKEN is not set. <br>
Mitigation: Use only a flickies instance you operate or trust; set FLICKIES_AUTH_TOKEN before network exposure and prefer loopback binding or an authenticated proxy. <br>
Risk: Video inputs, staged files, logs, model weights, output URLs, and webhook destinations may contain sensitive content. <br>
Mitigation: Treat all media paths and callback destinations as sensitive, avoid untrusted endpoints, and review storage, log, and webhook handling before use. <br>
Risk: Staged-file removal and engine eviction can affect shared instances or another active caller. <br>
Mitigation: Run state-changing cleanup only against resources created for the current task and only when the user asks. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/flickies) <br>
- [flickies setup](references/setup.md) <br>
- [Project homepage](https://github.com/psyb0t/docker-flickies) <br>
- [Model Context Protocol](https://modelcontextprotocol.io) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, API Calls, Code] <br>
**Output Format:** [Markdown with JSON and bash examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a reachable FLICKIES_URL and commonly uses docker and curl; optional bearer-token auth is configured with FLICKIES_AUTH_TOKEN.] <br>

## Skill Version(s): <br>
0.3.11 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
