## Description: <br>
Generate AI videos with Google Veo, Seedance, Wan, Grok and 40+ models via the inference.sh CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[okaris](https://clawhub.ai/user/okaris) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, creators, and external teams use this skill to generate and transform video assets through inference.sh, including text-to-video, image-to-video, avatar animation, lipsync, upscaling, and foley sound workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a remote inference.sh CLI installer. <br>
Mitigation: Install only when inference.sh is trusted, prefer manual checksum verification where practical, and use the intended inference.sh account. <br>
Risk: Prompts, private media, internal URLs, or regulated content may be sent to inference.sh-backed services for external processing. <br>
Mitigation: Avoid submitting confidential or regulated inputs unless external processing by inference.sh and its providers is acceptable. <br>


## Reference(s): <br>
- [inference.sh](https://inference.sh) <br>
- [Running Apps](https://inference.sh/docs/apps/running) <br>
- [Streaming Results](https://inference.sh/docs/api/sdk/streaming) <br>
- [Content Pipeline Example](https://inference.sh/docs/examples/content-pipeline) <br>
- [CLI Checksums](https://dist.inference.sh/cli/checksums.txt) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands target the infsh CLI and may submit prompts or media URLs to inference.sh-backed services.] <br>

## Skill Version(s): <br>
0.1.5 (source: server evidence release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
