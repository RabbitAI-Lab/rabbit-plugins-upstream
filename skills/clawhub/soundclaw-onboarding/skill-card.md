## Description: <br>
Run the OpenClaw-first SoundClaw readiness check and route operators to the next owned step. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[catholicbeer](https://clawhub.ai/user/catholicbeer) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Operators use this skill to check whether SoundClaw is installed and ready inside an OpenClaw workspace, then receive the next safe step when the backend is missing, degraded, or ready for normal flows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A readiness check could be mistaken for a completed backend installation or host repair. <br>
Mitigation: The skill distinguishes missing backend markers, degraded runtime status, and readiness, and directs operators to rerun checks or use runtime diagnostics instead of claiming repairs. <br>
Risk: Installer or runtime commands could affect the host if executed without review. <br>
Mitigation: The skill keeps onboarding non-mutating, points to documented release and installer help surfaces, and limits local execution to marker checks and runtime status commands. <br>
Risk: Users could rely on unsupported provenance for repository origin. <br>
Mitigation: The card does not infer GitHub provenance because server-resolved provenance is unavailable. <br>


## Reference(s): <br>
- [SoundClaw Onboarding](https://clawhub.ai/catholicbeer/skills/soundclaw-onboarding) <br>
- [SoundClaw release bundles](https://github.com/catholicbeer/soundclaw-release/releases) <br>
- [Skill homepage](https://github.com/catholicbeer/soundclaw-skills/tree/main/skills/soundclaw-onboarding) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Summarizes backend marker and runtime readiness state without performing host-changing actions.] <br>

## Skill Version(s): <br>
1.0.0 (source: release metadata and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
