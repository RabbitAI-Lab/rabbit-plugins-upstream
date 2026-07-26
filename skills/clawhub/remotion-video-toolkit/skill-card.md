## Description: <br>
Provides Remotion and React guidance for programmatic video creation, including animations, timing, rendering, captions, media handling, charts, 3D, text effects, transitions, and data-driven templates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shreefentsar](https://clawhub.ai/user/shreefentsar) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and video automation builders use this skill to write Remotion components, render video assets, and build data-driven video generation pipelines for social clips, ads, captions, product videos, education, and API-based rendering. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Example HTTP render APIs may be copied into production without access controls. <br>
Mitigation: Add authentication, authorization, and rate limits before exposing render endpoints. <br>
Risk: Unvalidated composition IDs, render props, or inputProps can create unreliable renders or expose sensitive values. <br>
Mitigation: Validate composition IDs and props with an allowlist or schema, and do not place secrets in inputProps. <br>
Risk: Cloud rendering, remote media URLs, and cloud transcription can share media or metadata with third-party services. <br>
Mitigation: Review privacy requirements and service terms before use, and prefer local or controlled processing for sensitive media. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/shreefentsar/skills/remotion-video-toolkit) <br>
- [Remotion Tailwind documentation](https://www.remotion.dev/docs/tailwind) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with TypeScript, TSX, and bash examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guidance covers Remotion composition code, rendering commands, media utilities, cloud rendering, captions, animations, and visual effects.] <br>

## Skill Version(s): <br>
1.4.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
