## Description: <br>
Ships a complete album in one run by writing or reusing lyrics, rendering tracks, generating cover art, building a 1080p karaoke-subtitled album film, publishing the video, deploying audio to a radio host, and supporting on-air premiere timing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nickflach](https://clawhub.ai/user/nickflach) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Artists, producers, and release operators use this skill to coordinate an album release workflow across music rendering, cover generation, film assembly, video publishing, radio deployment, and timed premiere operations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Publishing and deployment phases can affect live media channels and hosted radio services. <br>
Mitigation: Scope credentials to the intended provider accounts and host, verify targets before publish and deploy phases, and use phase skips or manual confirmation for premieres and production releases. <br>
Risk: Operator-specific runner behavior may not match another release environment. <br>
Mitigation: Supply a local runner and provider credentials, run preflight checks, and confirm the album is registered before deployment. <br>
Risk: Uploads or scheduled audio segments may appear successful while no media is available. <br>
Mitigation: Verify the uploaded video exists and monitor radio journal markers before triggering premiere steps. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON configuration shape and operational steps] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Covers phase gating, provider credentials, deployment checks, and recovery gotchas; does not provide a reusable runner.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
