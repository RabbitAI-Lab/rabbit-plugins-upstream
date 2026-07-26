## Description: <br>
Search and download ready-to-print 3D model files (STL/3MF/ZIP) for a concept or specific part by querying Printables first, capturing license and attribution, downloading source files, and outputting a local folder with a manifest for quoting or printing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ajmwagar](https://clawhub.ai/user/ajmwagar) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, makers, and agents use this skill to search Printables for existing 3D models, download selected STL/3MF/ZIP assets, and preserve attribution, license identifiers, file paths, and hashes in a manifest. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill contacts Printables and its API during search and download operations. <br>
Mitigation: Run it only in environments where external access to Printables is acceptable. <br>
Risk: Downloaded STL, 3MF, and ZIP files are external content saved to a local output directory. <br>
Mitigation: Use a dedicated downloads folder and inspect or scan downloaded models and archives before opening them in slicer or printer software. <br>


## Reference(s): <br>
- [Printables](https://www.printables.com) <br>
- [Printables GraphQL API endpoint](https://api.printables.com/graphql/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Files, JSON] <br>
**Output Format:** [CLI text output, downloaded model files, ZIP archives when available, and manifest.json] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The manifest records source URL, author, license ID, downloaded file paths, file hashes, and fetch timestamp.] <br>

## Skill Version(s): <br>
0.1.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
