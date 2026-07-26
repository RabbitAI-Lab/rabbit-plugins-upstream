## Description: <br>
Provides sanitization guidelines for external content in skills and hooks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and skill authors use this guidance to sanitize untrusted external content before an agent processes it, reducing prompt-injection and unsafe code-execution risk. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The artifact describes automatic sanitization, but the referenced hook is not included in this release artifact. <br>
Mitigation: Do not assume automatic sanitization is active; install and verify the full plugin or hook separately, or apply the checklist manually. <br>
Risk: Guidance-only content can reduce mistakes but cannot enforce safe handling of untrusted input by itself. <br>
Mitigation: Review workflows that consume external content and confirm they follow the sanitization checklist before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-leyline-content-sanitization) <br>
- [Leyline plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/leyline) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown] <br>
**Output Format:** [Markdown guidance and checklist text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only guidance; automatic sanitization is not active unless the separate hook or full plugin is installed and verified.] <br>

## Skill Version(s): <br>
1.9.16 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
