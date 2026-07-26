## Description: <br>
Generate complete YouTube videos from a single prompt, including script, voiceover, stock footage, captions, and thumbnail assets. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mayank8290](https://clawhub.ai/user/mayank8290) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External creators, marketers, and developers use this skill to generate draft YouTube or short-form video packages from a topic prompt, including narration, B-roll, captions, thumbnails, and metadata. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends video topics, search phrases, and narration content to external services, including Pexels and Microsoft Edge TTS. <br>
Mitigation: Avoid confidential, regulated, or proprietary prompts unless those third-party data flows are acceptable. <br>
Risk: The skill depends on local media tools, Python packages, and a Pexels API key, and may create large media files under the configured output directory. <br>
Mitigation: Install only the listed dependencies, provide a scoped Pexels API key, and monitor disk usage in the output directory. <br>
Risk: The documentation describes the skill as self-contained even though it relies on external tools and services. <br>
Mitigation: Review dependency and service requirements before deployment and communicate those requirements to users. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/mayank8290/skills/youtube-factory) <br>
- [Pexels API](https://www.pexels.com/api/) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Markdown, JSON, Shell commands, Configuration instructions] <br>
**Output Format:** [Generated media files with Markdown script output, JSON metadata, and setup or execution commands.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates video, audio, captioned video, thumbnail, script, and metadata files under the configured output directory.] <br>

## Skill Version(s): <br>
1.3.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
