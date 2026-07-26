## Description: <br>
Creates topic-driven narrated explainer, podcast, and knowledge-summary videos through research, scripting, TTS, Remotion composition, 4K rendering, background music, subtitles, publishing metadata, and optional design learning from references. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[agents365-ai](https://clawhub.ai/user/agents365-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators and developers use this skill to turn a topic or edited narration plan into a structured video project with scripts, assets, TTS timing, Remotion components, preview gates, 4K MP4 output, BGM, subtitles, thumbnails, and optional shorts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill writes local video project files and runs ffmpeg, npx, and Remotion commands. <br>
Mitigation: Run it in a project workspace you are comfortable modifying, review generated files before publishing, and keep required tools and dependencies updated. <br>
Risk: Topic, script, or asset prompts may be sent to external research, stock-asset, and TTS providers. <br>
Mitigation: Avoid confidential scripts unless the configured providers are acceptable for the content and their privacy terms have been reviewed. <br>
Risk: Preference resets or migrations can affect future video-generation behavior. <br>
Mitigation: Back up user_prefs.json before resetting or migrating preferences. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/agents365-ai/skills/video-podcast-maker) <br>
- [Project homepage](https://github.com/Agents365-ai/video-podcast-maker) <br>
- [Video Podcast Maker - Workflow Phase 1: Scripting](references/workflow-script.md) <br>
- [Step 5: Asset Plan & Resolve](references/workflow-assets.md) <br>
- [Video Podcast Maker - Workflow Phase 2: Production](references/workflow-production.md) <br>
- [Video Podcast Maker - Workflow Phase 3: Publish](references/workflow-publish.md) <br>
- [Video Podcast Maker - Design Guide](references/design-guide.md) <br>
- [Natural Narration - Anti-Slop Rules for Spoken Scripts](references/natural-narration.md) <br>
- [Video Podcast Maker - Troubleshooting & Reference](references/troubleshooting.md) <br>
- [Azure TTS Pitfalls](references/azure-tts-pitfalls.md) <br>
- [Design Learning](references/design-learning.md) <br>
- [Hyperframes Overlays](references/hyperframes-overlays.md) <br>
- [Chinese Polyphone Reference (zh-CN)](references/zh-polyphones.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands, JSON configuration, TypeScript/Remotion code, and generated local video project files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs can include narration scripts, asset manifests, TTS audio and timing files, thumbnails, MP4 videos, subtitles, publishing metadata, and optional shorts.] <br>

## Skill Version(s): <br>
3.0.2 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
