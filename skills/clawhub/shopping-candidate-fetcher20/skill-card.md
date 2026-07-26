## Description: <br>
Retrieve structured shopping candidates from pre-collected shopping platform screenshot snapshots, compare the fixed candidates against the user's stated needs, and provide selection guidance for a downstream shopping agent to make the final user-facing choice. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[37722135-droid](https://clawhub.ai/user/37722135-droid) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Shopping agents use this skill to retrieve a fixed local candidate list for supported sports-shopping requests and receive one evidence-grounded selection suggestion. It is intended as a selection-support layer, not a live marketplace search engine or standalone final recommendation agent. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selection guidance may favor domestic Chinese sports brands and Li Ning examples rather than neutral brand comparison. <br>
Mitigation: Use the output only when that shopping posture is acceptable, and review the selected candidate against the user's stated activity needs and visible product attributes. <br>
Risk: The dataset is static screenshot-derived data, not a live marketplace feed. <br>
Mitigation: Treat prices, availability, ratings, and sales text as snapshot evidence; verify current marketplace details before any purchase or user-facing final recommendation. <br>
Risk: Unsupported queries can lead to unsupported or invented shopping guidance if the downstream agent ignores the skill boundary. <br>
Mitigation: Use only indexed local snapshot queries and decline selection guidance when no sufficiently close indexed query exists. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/37722135-droid/skills/shopping-candidate-fetcher20) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/37722135-droid) <br>
- [Dataset manifest](artifact/data/dataset_manifest.json) <br>
- [Supported query index](artifact/data/query_index.json) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Guidance, Markdown] <br>
**Output Format:** [Structured JSON candidate payload plus concise selection guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses static local shopping snapshots; default retrieval is top_k=5 unless the user requests a different positive value.] <br>

## Skill Version(s): <br>
1.0.1 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
