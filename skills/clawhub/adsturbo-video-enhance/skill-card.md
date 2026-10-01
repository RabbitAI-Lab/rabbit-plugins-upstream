## Description:

Cleans up existing video by removing watermarks, logos, or burnt-in subtitles, upscaling to 2K or 4K, and adding or translating subtitles without changing the underlying scene.

This skill is ready for commercial/non-commercial use.

## Publisher:

[adsturbo](https://clawhub.ai/user/adsturbo)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and teams use this skill to clean up existing videos, improve resolution, and add or translate subtitles through AdsTurbo. It requires an AdsTurbo API key and a public video URL or an uploaded video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Media URLs, uploaded videos, and task metadata are sent to AdsTurbo; uploaded files may become publicly accessible links.

Mitigation: Do not upload confidential media unless AdsTurbo processing and public-link exposure are acceptable.

Risk: Watermark or logo removal can alter media without the necessary rights.

Mitigation: Only remove watermarks or logos when authorized to modify the video.

Risk: Processing uses API-key-authenticated requests to AdsTurbo.

Mitigation: Keep the API key in the environment and do not include it in replies or shared media links.

## Reference(s):

- [AdsTurbo Video Cleanup on ClawHub](https://clawhub.ai/adsturbo/skills/adsturbo-video-enhance)
- [Video enhancement options](references/video_enhance.md)
- [Media upload instructions](references/upload.md)
- [Async task status and results](references/work.md)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown with a processed-video link]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video processing is asynchronous; the agent can report progress and provide the finished video link.]

## Skill Version(s):

1.2.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
