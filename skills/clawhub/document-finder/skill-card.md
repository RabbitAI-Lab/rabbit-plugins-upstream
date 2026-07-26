## Description: <br>
Scan a directory of documents, classify each file by compliance type, resolve version conflicts with the user, and produce a prioritized analysis plan mapping confirmed-current documents to Rote skills. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dangsllc](https://clawhub.ai/user/dangsllc) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Compliance teams and agents use this skill to inventory compliance document folders, identify current document versions, and route each confirmed document to the right downstream review skill. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad directory scans may expose unrelated sensitive documents through file discovery or short content peeks. <br>
Mitigation: Run the skill from a specific compliance-document directory and review the generated manifest before using downstream analysis skills. <br>
Risk: Ambiguous filenames or unresolved document versions can lead to incorrect routing recommendations. <br>
Mitigation: Confirm version-cluster choices when prompted and treat low-confidence or unknown classifications as items for manual review. <br>


## Reference(s): <br>
- [Document Finder on ClawHub](https://clawhub.ai/dangsllc/skills/document-finder) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, JSON, Guidance] <br>
**Output Format:** [Markdown summary table followed by a JSON manifest] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May ask the user to resolve version conflicts before producing the final manifest.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
