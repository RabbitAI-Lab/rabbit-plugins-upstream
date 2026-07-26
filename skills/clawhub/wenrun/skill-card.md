## Description: <br>
文润 detects template-like patterns in Chinese AI-generated text and provides optimization suggestions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wwumit](https://clawhub.ai/user/wwumit) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Writers, editors, and agents working with Chinese text use this skill to analyze AI-like writing patterns, score naturalness, and receive targeted revision suggestions before publishing or handing off content. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Analysis output may display excerpts from the submitted text. <br>
Mitigation: Use it only with text that is acceptable to show in local terminal output. <br>
Risk: AI-text detection and naturalness scoring can produce false positives or false negatives. <br>
Mitigation: Treat scores and suggestions as review aids, and make final editorial decisions manually. <br>


## Reference(s): <br>
- [README.md](README.md) <br>
- [features/ai-patterns.json](features/ai-patterns.json) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Guidance, Shell commands] <br>
**Output Format:** [Terminal text with optional JSON output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Findings may include excerpts from the analyzed text.] <br>

## Skill Version(s): <br>
1.1.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
