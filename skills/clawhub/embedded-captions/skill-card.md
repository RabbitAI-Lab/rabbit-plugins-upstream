## Description: <br>
Adds captions or subtitles to an existing single-subject talking-head video, including readable lower-third captions, cinematic embedded captions, VFX-style captions, and catalog-driven visual identities. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[heygen-com](https://clawhub.ai/user/heygen-com) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators, developers, and video production agents use this skill to add readable or art-directed captions to single-speaker talking-head clips while preserving the source footage except for caption overlays and documented theme reactions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Silent update instructions can change shared tooling before the user reviews the release. <br>
Mitigation: Require explicit confirmation before running skill-update commands and pin the reviewed release in controlled environments. <br>
Risk: The workflow may perform network fetches or run package tools through npx or uvx. <br>
Mitigation: Run it only in environments where those fetches and package executions are permitted, or preinstall and pin the required tools. <br>
Risk: The artifact can load GSAP from a CDN. <br>
Mitigation: Prefer a bundled, reviewed local GSAP asset when network-loaded browser scripts are not acceptable. <br>
Risk: Generated files can overwrite project outputs. <br>
Mitigation: Use an isolated project directory for each render and review generated files before preserving or publishing them. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/heygen-com/skills/embedded-captions) <br>
- [Catalog](CATALOG.md) <br>
- [Rail Reference](references/rail.md) <br>
- [Composition Craft](references/composition-craft.md) <br>
- [DNA Registry](dna/README.md) <br>
- [Themes Guide](themes/README.md) <br>
- [Reference Bar](references/reference-bar.md) <br>
- [Aesthetic Principles](references/aesthetic-principles.md) <br>
- [GSAP CDN Script](https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, code, files] <br>
**Output Format:** [Markdown guidance with shell commands, JSON configuration, and generated project files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create caption planning JSON, preview assets, rendered caption layers, and final video files inside the selected project directory.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
