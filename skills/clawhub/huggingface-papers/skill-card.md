## Description: <br>
Look up and read Hugging Face paper pages in markdown, and use the papers API for structured metadata such as authors, linked models/datasets/spaces, Github repo and project page. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huggingface](https://clawhub.ai/user/huggingface) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, researchers, and external users use this skill when they need an agent to retrieve, summarize, explain, or analyze AI research papers from Hugging Face paper pages or arXiv identifiers. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Authenticated paper actions can change Hugging Face paper or account metadata. <br>
Mitigation: Use read-only lookup commands as the normal path, and only provide an HF token or allow POST requests when the user specifically intends to claim authorship, index a paper, or update links. <br>
Risk: An agent with access to HF_TOKEN could perform account-affecting paper actions described by the skill. <br>
Mitigation: Keep HF_TOKEN unavailable for ordinary paper lookup and require explicit user approval before using authenticated endpoints. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/huggingface/skills/huggingface-papers) <br>
- [Hugging Face Papers](https://huggingface.co/papers) <br>
- [Hugging Face Papers API](https://huggingface.co/api/papers/{PAPER_ID}) <br>
- [arXiv Abstract Page](https://arxiv.org/abs/{PAPER_ID}) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, API calls, shell commands, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON API response guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Hugging Face paper markdown, structured paper metadata, linked model/dataset/space references, paper summaries, and fallback arXiv links.] <br>

## Skill Version(s): <br>
1.0.10 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
