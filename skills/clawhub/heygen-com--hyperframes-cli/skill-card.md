## Description: <br>
Guides agents through HyperFrames CLI workflows for scaffolding, checking, previewing, rendering, publishing, cloud rendering, diagnostics, upgrades, telemetry, and related video asset operations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[heygen-com](https://clawhub.ai/user/heygen-com) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to operate the HyperFrames CLI during video project creation, validation, preview, rendering, publishing, and troubleshooting across local, HeyGen cloud, AWS Lambda, and Google Cloud Run workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Publish and cloud rendering commands can upload project source and assets. <br>
Mitigation: Confirm the user wants a publish or cloud workflow, use dry-run and ignore-file checks where available, and review included assets before upload. <br>
Risk: HeyGen cloud, AWS Lambda, and Google Cloud Run workflows can use credentials and incur usage or infrastructure costs. <br>
Mitigation: Confirm the target provider, credential source, project or stack, region, and cost-sensitive settings before executing cloud or infrastructure commands. <br>
Risk: Feedback and telemetry can send diagnostics outside the local workspace. <br>
Mitigation: Respect telemetry opt-out or disabled states, obtain consent for public issue filing, and strip absolute paths or identifying machine details from feedback. <br>
Risk: Rendering or publishing can produce final deliverables before the user has approved the preview. <br>
Mitigation: Run the HyperFrames check and final preview workflow, then wait for explicit user approval before final render or publish commands. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/hyperframes-cli) <br>
- [HeyGen CLI repository](https://github.com/heygen-com/heygen-cli) <br>
- [HyperFrames CLI skill](SKILL.md) <br>
- [Cloud rendering](references/cloud.md) <br>
- [AWS Lambda rendering](references/lambda.md) <br>
- [Google Cloud Run rendering](references/cloudrun.md) <br>
- [Preview, render, publish, and feedback](references/preview-render.md) <br>
- [Lint, check, and snapshot](references/lint-validate-inspect.md) <br>
- [Init and scaffold](references/init-and-scaffold.md) <br>
- [Compare and batch rendering](references/compare-and-batch.md) <br>
- [Doctor and browser management](references/doctor-browser.md) <br>
- [Beats utility](references/beats.md) <br>
- [Info, upgrade, docs, benchmark, telemetry, and asset preprocessing](references/upgrade-info-misc.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline shell commands and command-specific guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May recommend JSON output modes, dry runs, preview gates, and provider-specific cloud or infrastructure settings.] <br>

## Skill Version(s): <br>
1.0.20 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
