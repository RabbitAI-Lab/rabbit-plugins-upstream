## Description: <br>
xClaw02 helps agents generate NVIDIA-compatible skill card context and governance documentation from skill source evidence. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[primer-dev](https://clawhub.ai/user/primer-dev) <br>

### License/Terms of Use: <br>
Creative Commons Zero (CCO) License for AI Transparency Card Templates; Apache-2.0 and CC-BY-4.0 for the bundled generator materials <br>


## Use Case: <br>
Developers and governance reviewers use this skill to prepare concise transparency-card context for an agent skill release before public rendering and review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can produce governance context from incomplete or publisher-controlled source files. <br>
Mitigation: Review generated context against server evidence, source files, and security findings before rendering or publishing. <br>
Risk: Generated guidance or commands may be incorrect for a target repository. <br>
Mitigation: Review proposed commands and generated text before execution or release. <br>


## Reference(s): <br>
- [NVIDIA Trustworthy AI repository](https://github.com/NVIDIA/Trustworthy-AI) <br>
- [NVIDIA Trustworthy AI overview](https://www.nvidia.com/en-us/ai-data-science/trustworthy-ai/) <br>
- [Model Card++ templates](https://github.com/NVIDIA/Trustworthy-AI/tree/main/Model%20Card%2B%2B%20Templates) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [JSON context, Markdown guidance, and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated content should be reviewed before use; final public Markdown is rendered by the worker.] <br>

## Skill Version(s): <br>
0.1.0 (source: target metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
