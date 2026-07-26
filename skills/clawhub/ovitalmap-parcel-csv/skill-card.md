## Description: <br>
Generate and archive Ovitalmap parcel vertex/boundary CSVs for users who provide parcel coordinates or images and request 奥维地图 CSV export, archive re-export, or coordinate correction. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jeromeex](https://clawhub.ai/user/jeromeex) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to turn confirmed parcel coordinates into Ovitalmap-compatible vertex and boundary CSV files, then maintain local per-country and master parcel archives. It is intended for workflows that need provider matching, code assignment, archive re-export, or coordinate correction with explicit confirmation gates before writes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill writes generated CSVs and can update local parcel archives. <br>
Mitigation: Set OVITALMAP_WORKSPACE to the intended project folder, review coordinate, provider, and code confirmations before allowing writes, and keep backups of important archives. <br>
Risk: Incorrect country, provider, parcel code, or coordinate confirmation could create misleading Ovitalmap exports or archive records. <br>
Mitigation: Treat script-reported error and needs_input states as blocking, require explicit confirmation for non-exact matches and generated codes, and do not guess missing geographic or identity fields. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/jeromeex/skills/ovitalmap-parcel-csv) <br>
- [CSV Compatibility Contract](references/csv-contract.md) <br>
- [Interaction and Edge Cases](references/interaction-and-edge-cases.md) <br>
- [OpenClaw Reply Contract](references/reply-contract.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files, Guidance] <br>
**Output Format:** [Chinese user-facing replies with generated CSV files, file paths, JSON-driven script calls, and concise Markdown guidance when needed] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces Ovitalmap vertex and boundary CSVs and can update local parcel archive CSVs after required user confirmations.] <br>

## Skill Version(s): <br>
3.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
