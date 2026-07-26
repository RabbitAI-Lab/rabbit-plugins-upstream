## Description: <br>
Records browser sessions via Playwright and converts video to GIF. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to record automated browser interactions with Playwright for UI demos, tutorials, and documentation, then locate WebM output and convert it to GIF when needed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Browser recordings may capture sensitive page content and are saved to disk as WebM or GIF files. <br>
Mitigation: Use test accounts and sanitized data, store generated recordings in an appropriate location, and review videos before sharing. <br>
Risk: Automated browser specs can exercise live web applications and create misleading demos if pages are not fully loaded or actions are flaky. <br>
Mitigation: Use explicit waits, stable test data, and validate the generated recording before using it as documentation or a tutorial asset. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-scry-browser-recording) <br>
- [Source homepage](https://github.com/athola/claude-night-market/tree/master/plugins/scry) <br>
- [Spec execution module](modules/spec-execution.md) <br>
- [Video capture module](modules/video-capture.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with bash and TypeScript code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces Playwright commands, configuration examples, and output path guidance; recordings are WebM files that may be converted to GIF by a dependent gif-generation skill.] <br>

## Skill Version(s): <br>
1.9.16 (source: ClawHub release evidence; artifact frontmatter reports 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
