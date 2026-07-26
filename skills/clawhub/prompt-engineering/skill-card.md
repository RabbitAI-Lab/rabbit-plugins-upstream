## Description: <br>
Guides agents through prompt engineering techniques for LLMs, image generators, and video models, with examples for role prompting, few-shot prompting, structured output, negative prompts, and iterative refinement. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[okaris](https://clawhub.ai/user/okaris) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, content creators, and AI practitioners use this skill to structure prompts for LLM, image, and video generation tasks and to run examples through inference.sh. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The quick-start installer pipes a remote script into a shell. <br>
Mitigation: Install only if the inference.sh installer is trusted; prefer manual download or checksum verification before running it. <br>
Risk: Prompt examples send user-provided content to external model providers. <br>
Mitigation: Avoid including secrets or sensitive private data in prompts submitted through external providers. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/okaris/skills/prompt-engineering) <br>
- [inference.sh](https://inference.sh) <br>
- [inference.sh CLI checksums](https://dist.inference.sh/cli/checksums.txt) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with bash command examples and prompt templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Examples target the inference.sh CLI and external model providers; generated results depend on the selected provider.] <br>

## Skill Version(s): <br>
0.1.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
