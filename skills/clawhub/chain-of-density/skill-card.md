## Description: <br>
Chain of Density iteratively condenses long source text into information-dense summaries while preserving key entities. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[killerapp](https://clawhub.ai/user/killerapp) <br>

### License/Terms of Use: <br>
Apache-2.0 <br>


## Use Case: <br>
Developers, researchers, and content authors use this skill to compress verbose documentation, requirements, reports, or skill text into concise summaries. It is best suited for ordinary summarization where preserving named entities and source-grounded facts matters more than teaching step-by-step detail. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The original source text is passed through repeated summarization iterations. <br>
Mitigation: Use it only with content approved for the configured agent environment, and confirm the cod-iteration subagent before processing private or regulated documents. <br>
Risk: Dense summaries can omit nuance or compress away precision needed for legal, compliance, tutorial, or specification text. <br>
Mitigation: Avoid using this skill for precision-critical documents, or compare the final summary against the source before relying on it. <br>


## Reference(s): <br>
- [Chain of Density ClawHub listing](https://clawhub.ai/killerapp/skills/chain-of-density) <br>
- [From Sparse to Dense: GPT-4 Summarization with Chain of Density Prompting](https://arxiv.org/abs/2309.04269) <br>
- [HuggingFace chain_of_density dataset](https://huggingface.co/datasets/griffin/chain_of_density) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Plain text summary by default, with optional YAML-formatted iteration history and Markdown guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Maintains a target word count across serial density iterations and can use a local text metrics helper for deterministic word, character, and byte counts.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
