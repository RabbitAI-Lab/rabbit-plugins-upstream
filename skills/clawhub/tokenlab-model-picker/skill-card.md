## Description: <br>
Pick TokenLab models for chat, coding, image, video, audio, embeddings, reranking, and translation by reading public model catalog signals before recommending concrete model IDs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hedging8563](https://clawhub.ai/user/hedging8563) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agents use this skill to choose TokenLab model IDs for coding, chat, multimodal, embedding, reranking, translation, audio, image, and video workloads based on public catalog, contract, and pricing signals. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses the public TokenLab model catalog, so catalog lookups may contact api.tokenlab.sh and expose query details. <br>
Mitigation: Review whether external catalog access is acceptable and avoid including private prompts, secrets, or account data in catalog query parameters. <br>
Risk: Model availability, pricing, and benchmark relevance can change over time. <br>
Mitigation: Rerun the catalog and pricing lookups before relying on a recommendation for production routing or cost-sensitive work. <br>


## Reference(s): <br>
- [TokenLab model catalog](https://api.tokenlab.sh/v1/models) <br>
- [TokenLab task shortlist endpoint](https://api.tokenlab.sh/v1/models?recommended_for=<scene>) <br>
- [TokenLab model contract endpoint](https://api.tokenlab.sh/v1/models/:model) <br>
- [TokenLab pricing endpoint](https://api.tokenlab.sh/v1/models/:model/pricing) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown with a compact recommendation table and one runnable catalog command when useful.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include workload assumptions, fallback models, and caveats about volatile availability, pricing, or benchmark data.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
