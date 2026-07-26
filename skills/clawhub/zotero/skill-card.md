## Description: <br>
Manage Zotero reference libraries via the Web API. Search, list, add items by DOI/ISBN/PMID with duplicate detection, delete or trash items, update metadata and tags, export in BibTeX/RIS/CSL-JSON, batch-add from files, check PDF attachments, cross-reference citations, find missing DOIs via CrossRef, and fetch open-access PDFs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[terwox](https://clawhub.ai/user/terwox) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External researchers, students, developers, and agents use this skill to manage personal or group Zotero libraries, automate bibliography workflows, find citation metadata, and export references through the Zotero Web API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read and change a Zotero library when given an API key. <br>
Mitigation: Use a least-privilege Zotero API key and verify whether it targets a personal or group library before running commands. <br>
Risk: Bulk or mutating commands can affect many records or attachments. <br>
Mitigation: Scope operations with --limit or --collection, run dry-run modes first where available, and review destructive or mutating flags such as --yes, --permanent, --apply, --upload, --download-dir, --force, and --output. <br>


## Reference(s): <br>
- [Zotero skill troubleshooting](references/troubleshooting.md) <br>
- [Zotero Web API](https://api.zotero.org) <br>
- [Zotero API key settings](https://www.zotero.org/settings/keys/new) <br>
- [Zotero status](https://status.zotero.org) <br>
- [CrossRef](https://www.crossref.org) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, JSON, files, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, JSON command output, and bibliography files such as BibTeX, RIS, and CSL-JSON] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Zotero API credentials; mutating operations can change library metadata, attachments, tags, or items.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
