## Description: <br>
Generate a plain-English weekly clinic activity report for a veterinary clinic owner from NxVET data, including total recordings, per-device and per-day/hour breakdowns, week-over-week trend, and health flags for silent devices, outdated firmware, and failing webhooks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[talnirnx](https://clawhub.ai/user/talnirnx) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Clinic owners, managers, and their supporting agents use this skill to generate a recurring local weekly summary of NxVET clinic activity, trends, and operational health flags. The skill is intended for read-only reporting from existing NxVET data and does not send, edit, or delete clinic information. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The NxVET API key can grant access to clinic data if exposed. <br>
Mitigation: Store the key only in NXVET_API_KEY or a local .env file, mask it in logs, and keep .env out of git and cloud-synced folders. <br>
Risk: Generated reports may contain business-sensitive clinic activity data. <br>
Mitigation: Write reports locally, keep output/ out of git and unapproved cloud sync, and let the clinic owner decide whether to share reports. <br>
Risk: Optional scheduling can create recurring local report generation that the user may not expect. <br>
Mitigation: Enable the weekly scheduler only after explicit user approval and document where the scheduled job writes reports. <br>
Risk: Incorrect interpretation of clinic data could create misleading operational flags. <br>
Mitigation: Report only API-returned numbers, preserve traceability to collected JSON, and avoid flagging non-hardware devices as silent. <br>


## Reference(s): <br>
- [NxVET Clinic Activity Skill Homepage](https://api.nx.vet/skills.html#clinic-activity) <br>
- [NxVET API Documentation](https://api.nx.vet/) <br>
- [NxVET API Guide for Agents](https://api.nx.vet/llms-full.txt) <br>
- [NxVET OpenAPI Specification](https://api.nx.vet/openapi/nxvet-api.yaml) <br>
- [NxVET MCP Setup](https://api.nx.vet/mcp.html) <br>
- [NxHUB Product Information](https://nx.vet/products/nxhub) <br>
- [NxVET API Reference Notes](reference/nxvet-api.md) <br>
- [Security and Privacy Notes](reference/security.md) <br>
- [Caching and State Notes](reference/caching-and-state.md) <br>
- [Good Practices](reference/good-practices.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports, JSON statistics, Python scripts, shell commands, and setup guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local files such as output/ClinicReport_YYYY-Www.md and optional local scheduler configuration; requires NXVET_API_KEY.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
