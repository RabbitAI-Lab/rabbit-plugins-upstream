## Description: <br>
General Video guides an agent through creating or editing custom HyperFrames video compositions when no specialized workflow fits. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[heygen-com](https://clawhub.ai/user/heygen-com) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and creative operators use this skill to plan, build, validate, preview, and optionally render custom HyperFrames video projects, including multi-scene compositions, brand reels, sizzle reels, montages, title cards, footage remixes, and companion-guided edits. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Authenticated media providers or render actions can trigger paid or external operations. <br>
Mitigation: Run the documented authentication status check, review provider sign-in output, and require render approval before paid or external actions. <br>
Risk: Generated video compositions can diverge from project scope, brand truth, or user-approved assets. <br>
Mitigation: Follow the skill's brief, storyboard, design-truth, validation, and final preview gates before rendering. <br>
Risk: Large multi-scene builds can introduce scene-boundary or motion-ledger errors. <br>
Mitigation: Use the frame-packet workflow only when justified by scale, collect composition and motion sidecar outputs, run HyperFrames checks, and inspect multi-scene previews or animation maps. <br>


## Reference(s): <br>
- [General Video on ClawHub](https://clawhub.ai/heygen-com/skills/general-video) <br>
- [Publisher profile: heygen-com](https://clawhub.ai/user/heygen-com) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and generated HyperFrames project files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces project artifacts such as BRIEF.md, STORYBOARD.md, composition HTML, motion sidecars, validation output, preview handoff, and render guidance when approved.] <br>

## Skill Version(s): <br>
1.0.12 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
