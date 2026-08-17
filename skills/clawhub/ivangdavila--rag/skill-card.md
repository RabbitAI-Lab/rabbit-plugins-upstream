## Description: <br>
Designs, tunes, and debugs retrieval-augmented generation pipelines, including chunking, embeddings, hybrid retrieval, reranking, grounded answers, evaluation, production operations, and security concerns. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to design, tune, debug, evaluate, and operate RAG systems. It helps diagnose retrieval versus generation failures, choose pipeline components, handle difficult source formats, manage cost and latency, and apply access-control, privacy, and prompt-injection safeguards. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local RAG notes can include corpus inventories, query and evaluation diagnostics, cost records, and shared infrastructure rows. <br>
Mitigation: Keep records in the disclosed local paths, avoid verbose logging with sensitive production queries, and apply access controls, retention limits, and erasure handling where needed. <br>
Risk: Credentials or confidential corpus content could be exposed if copied into persistent notes. <br>
Mitigation: Store credential pointers instead of secret values, and keep document identifiers and source paths rather than confidential chunk text. <br>


## Reference(s): <br>
- [ClawHub RAG Skill Page](https://clawhub.ai/ivangdavila/skills/rag) <br>
- [Clawic RAG Skill](https://clawic.com/skills/rag) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with inline code, commands, tables, and configuration notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May update local notes under configured ~/Clawic/data/ paths when a session produces durable RAG decisions, diagnostics, or operational records.] <br>

## Skill Version(s): <br>
1.0.2 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
