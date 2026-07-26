## Description: <br>
Analyze a portrait photo with MiniMax-M3 and generate a playful camera-presence report with highlights, tips, social copy, and a shareable report-card image. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[airbai](https://clawhub.ai/user/airbai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, creators, and developers use Beauty Karma to turn a selfie, avatar, or portrait into light entertainment feedback for profile-photo selection, social sharing, and portrait presentation improvements. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Portrait photos may be sent to MiniMax or a configured endpoint and saved into generated local report files. <br>
Mitigation: Use mock mode for local demos, avoid untrusted image URLs or endpoint overrides, and delete generated reports when they are no longer needed. <br>
Risk: The lens score and report copy could be mistaken for a personal, professional, or sensitive-attribute assessment. <br>
Mitigation: Keep the output framed as entertainment, review report text before sharing, and avoid identity, age, ethnicity, health, wealth, or other sensitive inferences. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Text, Files, Guidance] <br>
**Output Format:** [JSON status plus generated JSON, HTML, and SVG report files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a portrait image input; real analysis requires MINIMAX_API_KEY, while mock mode supports local demos without a model call.] <br>

## Skill Version(s): <br>
1.0.3 (source: SKILL.md frontmatter, package.json, skill.json, server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
