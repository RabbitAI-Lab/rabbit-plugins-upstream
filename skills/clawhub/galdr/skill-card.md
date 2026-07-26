## Description: <br>
OpenClaw skill for using galdr's ARC workflow to turn YouTube URLs or local audio files into grounded, time-ordered listening-experience prompts backed by listener-state traces: pattern, attention, pulse, heard pressure, surface balance/evidence, harmony, melody, overtones, and silence/re-entry structure. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sellemain](https://clawhub.ai/user/sellemain) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use Galdr to analyze music from YouTube URLs or local audio files, assemble grounded ARC listening-experience prompts, and extract structural evidence such as listener-state traces or video frames. It is best suited for song analysis, structural listening prose, and evidence packets for downstream model writing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: YouTube URLs, downloaded context, lyrics, frame descriptions, and assembled prompts can include information that may be shared with third-party services when fetch workflows or model CLI piping are used. <br>
Mitigation: Review assembled prompts before sending them to external model endpoints, and prefer local files or blind/metrics-only modes when less contextual data should be included. <br>
Risk: The skill depends on the separate galdr CLI and media tooling, so installation and execution inherit the trust and runtime risks of that CLI and its dependencies. <br>
Mitigation: Install galdr only from trusted sources, verify PyPI metadata or the listed project repository when provenance matters, and run diagnostic commands before use. <br>
Risk: Downloading copyrighted audio can create rights or policy issues when the operator lacks appropriate authorization. <br>
Mitigation: Use local files or fetch only content where the operator has appropriate rights or context, and avoid using the skill for unauthorized downloading. <br>


## Reference(s): <br>
- [Galdr Metric Reference](references/metrics.md) <br>
- [Galdr PyPI Project](https://pypi.org/project/galdr/) <br>
- [Galdr Project Repository Listed By Skill](https://github.com/sellemain/galdr) <br>
- [ClawHub Skill Page](https://clawhub.ai/sellemain/skills/galdr) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, code, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell and Python code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces prompts and guidance for running the separate galdr CLI; generated prompts may include metrics, lyrics, background context, or frame descriptions depending on mode.] <br>

## Skill Version(s): <br>
0.6.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
