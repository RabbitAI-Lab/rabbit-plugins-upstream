## Description: <br>
拾光册记忆手帐 is a tool-agnostic workflow for turning key frames, user stories, and optional layout references into editable visual memory journals with provenance, staged review, collection management, and semantic recall. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[legithubhh](https://clawhub.ai/user/legithubhh) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Agents use this skill to analyze source images, plan 1-5 redrawn keepsake elements, separate content assets from layout references, compose editable scrapbook-style journals, write factual artistic copy, archive memory records, and retrieve them later by natural-language meaning. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow may involve personal photos, personal stories, source links, and searchable memory records. <br>
Mitigation: Use it only in agent environments where those inputs may be processed, and decide where archives and indexes are stored before enabling persistence or recall. <br>
Risk: Saved journals, reusable assets, or memory indexes could retain sensitive material longer than intended. <br>
Mitigation: Define deletion behavior up front, require explicit confirmation before destructive actions, and exclude sensitive journals or sources when appropriate. <br>
Risk: A missing original source link could be mistaken for verified provenance. <br>
Mitigation: Record unavailable source links explicitly and do not infer or fabricate external provenance. <br>
Risk: Flattened images can be misrepresented as fully recoverable editable projects. <br>
Mitigation: Treat flattened PNG, JPG, WebP, PDF, or screenshot inputs as a single visual layer unless a structured editable journal package is also available. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/legithubhh/skills/shiguang-memory-journal) <br>
- [Publisher profile](https://clawhub.ai/user/legithubhh) <br>
- [Product principles](artifact/references/product-principles.md) <br>
- [Workflow playbook](artifact/references/workflow-playbook.md) <br>
- [Journal style profiles](artifact/references/style-profiles.md) <br>
- [Tool-agnostic prompt pack](artifact/references/prompt-pack.md) <br>
- [Portable data contracts](artifact/references/data-contracts.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with structured JSON manifests, prompts, layout specifications, quality reports, and recall results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce editable journal records, portable interchange plans, source ledgers, archive manifests, deletion plans, and source-link availability status; no bundled runtime is required.] <br>

## Skill Version(s): <br>
1.3.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
