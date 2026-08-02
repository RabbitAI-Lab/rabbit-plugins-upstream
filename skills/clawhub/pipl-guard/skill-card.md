## Description: <br>
PIPL Guardrail detects personal information in AI application inputs and outputs, then masks or blocks content according to risk level before an agent continues processing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wwumit](https://clawhub.ai/user/wwumit) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and AI application teams use this skill as a local runtime guardrail to inspect user input or model output for personal information, then return a structured decision, masked text, or a block decision. It is intended as a compliance aid for PIPL-oriented data handling, not as legal advice or a complete compliance guarantee. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Personal-information detection is best effort and may miss or incorrectly flag content. <br>
Mitigation: Use the skill as one control in a broader compliance process, and have qualified reviewers handle legal or high-impact compliance decisions. <br>
Risk: Detect mode can include the original input text in output. <br>
Mitigation: Use mask or block mode for workflows that handle sensitive content, and avoid logging raw detect-mode outputs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/wwumit/skills/pipl-guard) <br>
- [Project homepage](https://github.com/wwumit/pipl-guard) <br>
- [README](README.md) <br>
- [CHANGELOG](CHANGELOG.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, guidance] <br>
**Output Format:** [Plain text or structured JSON decision output from a local command-line guardrail] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [JSON results include decision, risk level, finding count, findings with masked previews, and processed output; blocked results return null output.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence, package.json, CHANGELOG released 2026-07-29) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
