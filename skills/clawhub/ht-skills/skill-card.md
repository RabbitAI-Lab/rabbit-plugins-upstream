## Description: <br>
ht-skills helps an agent manage 灏天文库 collections, documents, images, and RAG retrieval workflows through authenticated client scripts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[1044197988](https://clawhub.ai/user/1044197988) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to create, read, update, move, and organize 灏天文库 personal garden content, upload images, inspect account quotas, request collection promotion, and retrieve snippets from public collection indexes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a 灏天文库 API token that can authorize account-level API actions. <br>
Mitigation: Install only from a trusted publisher, prefer environment variables for tokens, avoid sharing token-bearing config files, and rotate the token if exposure is suspected. <br>
Risk: Write operations can rename collections, add or update documents, move documents, upload images, or submit promotion requests that affect user account content. <br>
Mitigation: Review and approve write actions before execution, confirm target collection and document IDs, and check quotas before large or irreversible changes. <br>
Risk: Garden-to-featured promotion changes how a collection is managed after approval. <br>
Mitigation: Use the quota check first, explain the documented promotion consequences, and submit only after explicit user confirmation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/1044197988/skills/ht-skills) <br>
- [灏天文库](https://aiknowledge.cn) <br>
- [灏天文库 public collection directory](https://aiknowledge.cn/article/66521-%E7%81%8F%E5%A4%A9%E6%96%87%E5%BA%93%E6%96%87%E9%9B%86%E5%AE%8C%E6%95%B4%E7%9B%AE%E5%BD%95%E5%85%AC%E5%BC%80) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API Calls, JSON, Markdown, Guidance] <br>
**Output Format:** [JSON API responses with Markdown guidance and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a 灏天文库 API token and uses configured service endpoint settings.] <br>

## Skill Version(s): <br>
1.1.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
