## Description:

Helps social-media creators adapt the structure and emotional hook of a reference video to promote their own product, then generate a new short video through Qinghu AI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Social-media marketers and short-video creators use this skill to analyze a reference video's structure, rewrite its script for their product, and generate a promotional short video after approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent may install or upgrade Node and npm packages or change its executable search path.

Mitigation: Review package installation, upgrades, and PATH changes before allowing them.

Risk: The skill asks for a raw API key in chat.

Mitigation: Configure QHKIT_TOKEN or qhkit locally instead of sharing the key in chat.

Risk: Local media may be uploaded to Qinghu services, and video generation spends paid credits.

Mitigation: Review the media and estimated credit cost, then explicitly approve each generation before submission.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/linkpix-grok-clone)
- [Qinghu qhkit package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Video links]

**Output Format:** [Markdown script comparison, generation status, and video URL]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes the generated video's credit cost when available.]

## Skill Version(s):

0.1.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
