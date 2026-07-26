## Description: <br>
Create AI avatar and talking head videos with OmniHuman, Fabric, PixVerse via inference.sh CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[okaris](https://clawhub.ai/user/okaris) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and content teams use this skill to generate AI presenters, talking head videos, lipsync videos, dubbed videos, virtual influencers, marketing videos, educational videos, and corporate training videos through inference.sh CLI workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill recommends installing and using the inference.sh CLI, and installer integrity matters before running local commands. <br>
Mitigation: Prefer manual download and checksum verification for the inference.sh CLI instead of piping curl directly to sh. <br>
Risk: Avatar and lipsync workflows may process portraits, voices, audio, or videos that include sensitive likeness or media rights. <br>
Mitigation: Use an inference.sh account you trust, and only submit portraits, voices, audio, or videos you own or are authorized to process. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/okaris/skills/ai-avatar-video) <br>
- [inference.sh](https://inference.sh) <br>
- [inference.sh CLI Checksums](https://dist.inference.sh/cli/checksums.txt) <br>
- [Running Apps](https://inference.sh/docs/apps/running) <br>
- [Content Pipeline Example](https://inference.sh/docs/examples/content-pipeline) <br>
- [Streaming Results](https://inference.sh/docs/api/sdk/streaming) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline bash and JSON command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill provides inference.sh CLI commands and workflow guidance; users provide authorized image, audio, and video URLs.] <br>

## Skill Version(s): <br>
0.1.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
