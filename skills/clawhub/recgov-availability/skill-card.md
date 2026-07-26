## Description: <br>
Check campsite availability on recreation.gov for federal campgrounds (National Parks, USFS, BLM). Requires campground ID(s) - get from ridb-search or recreation.gov URLs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[seanrea](https://clawhub.ai/user/seanrea) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and agents use this skill to check federal campsite availability on Recreation.gov for specified campground IDs, dates, stay lengths, site types, and amenities. It helps compare available, reserved, not-yet-released, and first-come-first-served campsite statuses before booking. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill makes outbound network requests to Recreation.gov to check campsite availability. <br>
Mitigation: Run it only where outbound access to Recreation.gov is acceptable and review command arguments before execution. <br>
Risk: The security evidence says the skill should not need credentials or private files. <br>
Mitigation: Do not provide personal account data or private files unless a future version clearly explains why they are needed. <br>
Risk: Availability can change quickly and may not reflect final booking status. <br>
Mitigation: Confirm availability on Recreation.gov before making travel or booking decisions. <br>


## Reference(s): <br>
- [Recreation.gov Availability API Notes](references/api-notes.md) <br>
- [Recreation.gov](https://www.recreation.gov) <br>
- [RIDB Portal](https://ridb.recreation.gov) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, JSON, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples; the CLI can return human-readable text or JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires campground IDs and date inputs. Amenity filters may make additional Recreation.gov requests.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
