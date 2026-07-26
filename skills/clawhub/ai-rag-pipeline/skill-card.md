## Description: <br>
Build RAG (Retrieval Augmented Generation) pipelines with web search and LLMs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[okaris](https://clawhub.ai/user/okaris) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, AI agents, research assistants, fact-checkers, and knowledge-base builders use this skill to design retrieval-augmented workflows that combine web search, content extraction, and LLM generation for grounded answers and research reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: RAG workflows may send prompts, retrieved context, URLs, or documents to inference.sh and third-party search or LLM providers. <br>
Mitigation: Use only approved data, avoid secrets and regulated information unless sharing is authorized, and confirm provider terms before use. <br>
Risk: Shell examples interpolate search results and user-provided values into JSON command inputs. <br>
Mitigation: Review and adapt examples with safer JSON construction and quoting before using them with untrusted or complex input. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/okaris/skills/ai-rag-pipeline) <br>
- [inference.sh](https://inference.sh) <br>
- [Adding Tools to Agents](https://inference.sh/docs/agents/adding-tools) <br>
- [Building a Research Agent](https://inference.sh/blog/guides/research-agent) <br>
- [CLI checksums](https://dist.inference.sh/cli/checksums.txt) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, code, markdown] <br>
**Output Format:** [Markdown with inline bash code blocks and pipeline examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Examples call inference.sh apps for search, extraction, and LLM generation through infsh.] <br>

## Skill Version(s): <br>
0.1.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
