## Description: <br>
Code quality and safety linter for OpenClaw skills that runs six analysis passes before installation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mohibshaikh](https://clawhub.ai/user/mohibshaikh) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use clawvet to scan OpenClaw skills for code quality, safety, metadata, dependency, typosquat, and semantic-analysis issues before installation or during CI review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Review before execution as proposals could introduce incorrect or misleading guidance into skills. <br>
Mitigation: Review and scan skill before deployment. <br>

## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mohibshaikh/skills/clawvet) <br>
- [Server-resolved GitHub provenance](https://github.com/MohibShaikh/clawvet) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash commands and optional JSON scanner output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires node and npm. Security evidence says the tool may inspect local skill folders and installed skills; enable watch mode, feedback, telemetry, alerts, badges, or remote scan features only when the related local access or network calls are acceptable, and prefer pinned npm versions in automated environments.] <br>

## Skill Version(s): <br>
0.8.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
